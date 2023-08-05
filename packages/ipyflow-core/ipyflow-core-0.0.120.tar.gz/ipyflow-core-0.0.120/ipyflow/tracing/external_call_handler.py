# -*- coding: utf-8 -*-
import ast
import logging
from types import ModuleType
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Set, Type

from ipyflow.data_model.timestamp import Timestamp
from ipyflow.singletons import flow, tracer
from ipyflow.types import IMMUTABLE_PRIMITIVE_TYPES

if TYPE_CHECKING:
    from ipyflow.data_model.data_symbol import DataSymbol
    from ipyflow.data_model.namespace import Namespace
    from ipyflow.tracing.ipyflow_tracer import ExternalCallArgument


logger = logging.getLogger(__name__)


class HasGetitem(type):
    """
    Mixin for indicating that a class has a __getitem__ method
    """

    def __getitem__(cls, item):
        return NotImplemented


class ExternalCallHandler(metaclass=HasGetitem):
    not_yet_defined = object()
    module: Optional[ModuleType] = None
    caller_self: Any = None
    function_or_method: Any = None
    args: List["ExternalCallArgument"] = None
    _arg_dsyms: Optional[Set["DataSymbol"]] = None
    return_value: Any = not_yet_defined
    stmt_node: ast.stmt = None

    def __new__(cls, *args, **kwargs):
        if cls is ExternalCallHandler:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)

    @classmethod
    def create(cls, **kwargs) -> "ExternalCallHandler":
        module = kwargs.pop("module", None)
        caller_self = kwargs.pop("caller_self", None)
        function_or_method = kwargs.pop("function_or_method", None)
        return cls(
            module=module,
            caller_self=caller_self,
            function_or_method=function_or_method,
        )._initialize_impl(**kwargs)

    def _initialize_impl(self, **kwargs) -> "ExternalCallHandler":
        ret = self
        for cls in self.__class__.mro():
            if not hasattr(cls, "initialize"):
                break
            ret = cls.initialize(ret, **kwargs) or ret  # type: ignore
        return ret

    def initialize(self, **_) -> Optional["ExternalCallHandler"]:
        return self

    def __init__(
        self,
        *,
        module: Optional[ModuleType] = None,
        caller_self: Any = None,
        function_or_method: Any = None,
    ) -> None:
        self.module = module
        self.caller_self = caller_self
        self.function_or_method = function_or_method
        self.args: List["ExternalCallArgument"] = []
        self._arg_dsyms: Optional[Set["DataSymbol"]] = None
        self.return_value: Any = self.not_yet_defined
        self.stmt_node = tracer().prev_trace_stmt_in_cur_frame.stmt_node

    def __init_subclass__(cls):
        external_call_handler_by_name[cls.__name__] = cls

    @property
    def caller_self_obj_id(self) -> Optional[int]:
        return None if self.caller_self is None else id(self.caller_self)

    @property
    def arg_dsyms(self) -> Set["DataSymbol"]:
        if self._arg_dsyms is None:
            self._arg_dsyms = set().union(*(arg[1] for arg in self.args))
        return self._arg_dsyms

    def process_arg(self, arg: Any) -> None:
        pass

    def _process_arg_impl(self, arg: "ExternalCallArgument") -> None:
        self.args.append(arg)
        self.process_arg(arg[0])

    def process_args(self, args: List["ExternalCallArgument"]) -> None:
        for arg in args:
            self._process_arg_impl(arg)

    def process_return(self, return_value: Any) -> None:
        self.return_value = return_value

    def _handle_impl(self) -> None:
        Timestamp.update_usage_info(self.arg_dsyms)
        self.handle()

    def mutate_caller(self, should_propagate: bool) -> None:
        if self.caller_self is None:
            return
        self.mutate_aliases(self.caller_self_obj_id, should_propagate=should_propagate)

    def mutate_module(self, should_propagate: bool) -> None:
        if self.module is None:
            return
        self.mutate_aliases(id(self.module), should_propagate=should_propagate)

    def mutate_aliases(self, obj_id: Optional[int], should_propagate: bool) -> None:
        mutated_syms = flow().aliases.get(obj_id, set())
        Timestamp.update_usage_info(mutated_syms)
        for mutated_sym in mutated_syms:
            mutated_sym.update_deps(
                self.arg_dsyms,
                overwrite=False,
                mutated=True,
                propagate_to_namespace_descendents=should_propagate,
                refresh=should_propagate,
            )

    def handle(self) -> None:
        pass


external_call_handler_by_name: Dict[str, Type[ExternalCallHandler]] = {}
REGISTERED_HANDLER_BY_FUNCTION: Dict[Callable, Type[ExternalCallHandler]] = {}


class NoopCallHandler(ExternalCallHandler):
    pass


# TODO: use dsl for these instead
ARG_MUTATION_EXCEPTED_MODULES = {
    "alt",
    "altair",
    "display",
    "logging",
    "matplotlib",
    "pyplot",
    "plot",
    "plt",
    "seaborn",
    "sns",
    "widget",
}


class StandardMutation(ExternalCallHandler):
    def _maybe_mutate_caller(self) -> None:
        if self.return_value is not None and self.caller_self is not self.return_value:
            return
        self.mutate_caller(should_propagate=True)

    def handle(self) -> None:
        if self.caller_self is not None:
            self._maybe_mutate_caller()
        elif self.module is not None and self.return_value is None:
            self.mutate_module(should_propagate=True)
            if len(self.args) == 0:
                return
            # FIXME: extremely hacky
            if (self.module.__name__ or "").split(".")[
                0
            ] in ARG_MUTATION_EXCEPTED_MODULES:
                return
            # FIXME: extremely hacky here too
            first_arg_obj, first_arg_syms = self.args[0]
            if isinstance(first_arg_obj, (list, set, dict) + IMMUTABLE_PRIMITIVE_TYPES):
                return
            depending_on_first_arg = []
            for obj, dsyms in self.args[1:]:
                filtered_dsyms = {
                    dsym
                    for dsym in dsyms
                    if any(first_sym in dsym.parents for first_sym in first_arg_syms)
                }
                if len(filtered_dsyms) > 0:
                    depending_on_first_arg.append((obj, filtered_dsyms))
            self.args = [self.args[0]] + depending_on_first_arg
            self._arg_dsyms = None
            ArgMutate.handle(self)  # type: ignore


class CallerMutation(ExternalCallHandler):
    def handle(self) -> None:
        self.mutate_caller(should_propagate=True)


class ModuleMutation(ExternalCallHandler):
    def handle(self) -> None:
        self.mutate_module(should_propagate=True)


class NamespaceClear(StandardMutation):
    def handle(self) -> None:
        super().handle()
        mutated_sym = flow().get_first_full_symbol(self.caller_self_obj_id)
        if mutated_sym is None:
            return
        namespace = mutated_sym.namespace
        if namespace is None:
            return
        for name in sorted(
            (
                dsym.name
                for dsym in namespace.all_data_symbols_this_indentation(
                    exclude_class=True, is_subscript=True
                )
            ),
            reverse=True,
        ):
            namespace.delete_data_symbol_for_name(name, is_subscript=True)


class MutatingMethodEventNotYetImplemented(ExternalCallHandler):
    pass


class ArgMutate(ExternalCallHandler):
    def handle(self) -> None:
        for mutated_sym in self.arg_dsyms:
            if mutated_sym is None or mutated_sym.is_anonymous:
                continue
            # TODO: happens when module mutates args
            #  should we add module as a dep in this case?
            mutated_sym.update_deps(set(), overwrite=False, mutated=True)


class ListMethod(ExternalCallHandler):
    def handle_namespace(self, namespace: "Namespace") -> None:
        pass

    def handle(self) -> None:
        caller_self_obj_id = self.caller_self_obj_id
        mutated_sym = flow().get_first_full_symbol(caller_self_obj_id)
        if mutated_sym is not None:
            namespace = mutated_sym.namespace
            if namespace is not None:
                self.handle_namespace(namespace)
        self.mutate_caller(should_propagate=False)


class ListExtend(ListMethod):
    orig_len: int = None

    def initialize(self, **kwargs) -> None:
        self.orig_len = len(self.caller_self)

    def handle_namespace(self, namespace: "Namespace") -> None:
        for upsert_pos in range(self.orig_len, len(namespace.obj)):
            namespace.upsert_data_symbol_for_name(
                upsert_pos,
                namespace.obj[upsert_pos],
                self.arg_dsyms,
                overwrite=False,
                is_subscript=True,
                propagate=False,
            )


class ListAppend(ListExtend):
    pass


class ListInsert(ListMethod):
    insert_pos: Optional[int] = None

    def handle_namespace(self, namespace: "Namespace") -> None:
        if self.insert_pos is None or len(self.args) < 2:
            return
        inserted_arg_obj, inserted_arg_dsyms = self.args[1]
        inserted_syms = {
            sym for sym in inserted_arg_dsyms if sym.obj is inserted_arg_obj
        }
        if len(inserted_syms) > 1:
            return
        namespace.shuffle_symbols_upward_from(self.insert_pos)
        namespace.upsert_data_symbol_for_name(
            self.insert_pos,
            namespace.obj[self.insert_pos],
            inserted_syms,
            self.stmt_node,
            overwrite=False,
            is_subscript=True,
            propagate=True,
        )

    def process_arg(self, insert_pos: int) -> None:
        self.insert_pos = insert_pos


class ListRemove(ListMethod):
    remove_pos: Optional[int] = None

    def handle_namespace(self, namespace: "Namespace") -> None:
        if self.remove_pos is None:
            return
        namespace.delete_data_symbol_for_name(self.remove_pos, is_subscript=True)

    def process_arg(self, remove_val: Any) -> None:
        try:
            self.remove_pos = self.caller_self.index(remove_val)
        except ValueError:
            pass


class ListPop(ListRemove):
    def process_arg(self, pop_pos: int) -> None:
        self.remove_pos = pop_pos


def _resolve_external_call_simple(
    module: Optional[ModuleType],
    caller_self: Optional[Any],
    function_or_method: Optional[Any],
    method: Optional[str],
    use_standard_default: bool = True,
) -> Optional[ExternalCallHandler]:
    if caller_self is not None and isinstance(caller_self, ModuleType):
        if module is None:
            module = caller_self
        caller_self = None
    if (
        module is logging
        or getattr(module, "__name__", None) == "__main__"
        or function_or_method == print
    ):
        return NoopCallHandler()
    if caller_self is logging or isinstance(caller_self, logging.Logger):
        return NoopCallHandler()
    elif caller_self is not None and id(type(caller_self)) in flow().aliases:
        return NoopCallHandler()
    # TODO: handle case where it's a function defined in-notebook
    elif caller_self is None:
        pass
    elif method is None:
        return None
    else:
        function_or_method = getattr(type(caller_self), method, function_or_method)
    external_call_type = REGISTERED_HANDLER_BY_FUNCTION.get(function_or_method, None)
    if external_call_type is None:
        if use_standard_default:
            external_call_type = StandardMutation
        else:
            return None
    if isinstance(caller_self, ModuleType):
        caller_self = None
    return external_call_type.create(
        module=module, caller_self=caller_self, function_or_method=function_or_method
    )


def resolve_external_call(
    module: Optional[ModuleType],
    caller_self: Optional[Any],
    function_or_method: Optional[Any],
    method: Optional[str],
    use_standard_default: bool = True,
) -> Optional[ExternalCallHandler]:
    return _resolve_external_call_simple(
        module,
        caller_self,
        function_or_method,
        method,
        use_standard_default=use_standard_default,
    )
