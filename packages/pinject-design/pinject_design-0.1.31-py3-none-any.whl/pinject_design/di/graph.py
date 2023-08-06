import inspect
from types import FunctionType
from typing import Union, Type, Callable, TypeVar, List

from loguru import logger
from makefun import create_function
from pinject import binding_keys, locations, SINGLETON
from pinject.bindings import default_get_arg_names_from_class_name, BindingMapping, new_binding_to_instance
from pinject.errors import NothingInjectableForArgError
from pinject.object_graph import ObjectGraph
from pinject.object_providers import ObjectProvider
from rx.subject import Subject

from pinject_design.di.injected import Injected
from pinject_design.di.session import OverridenBindableScopes
from pinject_design.exceptions import DependencyResolutionFailure

T = TypeVar("T")


class MissingDependencyException(Exception):
    @staticmethod
    def create_message(deps: List[DependencyResolutionFailure]):
        msgs = [item.explanation_str() for item in deps]
        lines = '\n'.join(msgs)
        return f"Missing dependency. failures:\n {lines}."

    @staticmethod
    def create(deps: List[DependencyResolutionFailure]):
        return MissingDependencyException(MissingDependencyException.create_message(deps))


class ExtendedObjectGraph:
    """
    an object graph which can also provide instances based on its name not only from class object.
    """

    def __init__(self, design: "Design", src: ObjectGraph):
        self.design = design
        # TODO override ObjectGraph vars to have 'session' as special name to be injected.
        # TODO use new_binding_to_instance to bind self as session
        back_frame = locations.get_back_frame_loc()
        session_binding = new_binding_to_instance(
            binding_keys.new("session"),
            to_instance=self,
            in_scope=SINGLETON,
            get_binding_loc_fn=lambda: back_frame
        )
        src._obj_provider._binding_mapping._binding_key_to_binding.update(
            {session_binding.binding_key: session_binding}
        )
        self.src = src

    def _provide(self, target: Union[str, Type[T], Injected[T], Callable]) -> Union[object, T]:
        """
        Hacks pinject to provide from string. by creating a new class.
        :param target:
        :return:
        """
        if isinstance(target, str):
            assert target != "self", f"provide target:{target}"
            code = compile(f"""def __init__(self,{target}):self.res={target}""", "<string>", "exec")
            fn = FunctionType(code.co_consts[0], globals(), "__init__")
            Request = type("Request", (object,), dict(__init__=fn))
            return self.src.provide(Request).res
        elif isinstance(target, type):
            return self.src.provide(target)
        elif isinstance(target, Injected):
            deps = target.dependencies()
            if 'self' in deps:
                deps.remove('self')
            signature = f"""__init__(self,{','.join(deps)})"""

            def impl(self, **kwargs):
                self.data = target.get_provider()(**kwargs)

            __init__ = create_function(signature, func_impl=impl)
            Request = type("Request", (object,), dict(__init__=__init__))
            return self.src.provide(Request).data
        elif isinstance(target, Callable):
            return self.run(target)
        else:
            raise TypeError(f"target must be either class or a string or Injected. got {target}")

    def provide(self, target: Union[str, Type[T], Injected[T], Callable]) -> Union[object, T]:
        try:
            return self._provide(target)
        except NothingInjectableForArgError as e:
            # preventing circular import
            from pinject_design.visualize_di import DIGraph
            match target:
                case type():
                    deps = [default_get_arg_names_from_class_name(target.__name__)[0]]
                case Injected():
                    deps = target.dependencies()
                case str():
                    deps = [target]
                case other:
                    raise e

            missings = DIGraph(self.design).find_missing_dependencies(deps)
            if missings:
                for missing in missings:
                    logger.error(f"failed to find dependency:{missing}")
                raise MissingDependencyException.create(missings)
            else:
                raise e

    def run(self, f):
        argspec = inspect.getfullargspec(f)
        assert "self" not in argspec.args, f"self in {argspec.args}, of {f}"
        # logger.info(self)
        assert argspec.varargs is None
        kwargs = {k: self.provide(k) for k in argspec.args}
        return f(**kwargs)

    def __repr__(self):
        return f"ExtendedObjectGraph of a design:\n{self.design}"

    def __getitem__(self, item):
        return self.provide(item)

    def child_session(self, overrides: "Design") -> "ExtendedObjectGraph":
        """
        1, make binding_keys from design
        2. make a scope
        3.
        :param overrides:
        :return:
        """
        # binding_mapping:BindingMapping = design_to_binding_keys(overrides)
        child_graph = overrides.to_graph().src
        override_keys = set(child_graph._obj_provider._binding_mapping._binding_key_to_binding.keys())
        new_mapping = self._merged_binding_mapping(child_graph)
        new_scopes = OverridenBindableScopes(self.src._obj_provider._bindable_scopes,override_keys)
        # now we need overriden child scope

        child_obj_provider = ObjectProvider(
            binding_mapping=new_mapping,
            bindable_scopes=new_scopes,
            allow_injecting_none=self.src._obj_provider._allow_injecting_none
        )
        child_obj_graph = ObjectGraph(
            obj_provider=child_obj_provider,
            injection_context_factory=self.src._injection_context_factory,
            is_injectable_fn=self.src._is_injectable_fn,
            use_short_stack_traces=self.src._use_short_stack_traces
        )
        return ExtendedObjectGraph(
            self.design + overrides,
            child_obj_graph,
        )

    def _merged_binding_mapping(self, child_graph: ObjectGraph):
        src: BindingMapping = self.src._obj_provider._binding_mapping
        child: BindingMapping = child_graph._obj_provider._binding_mapping
        return BindingMapping(
            {**src._binding_key_to_binding, **child._binding_key_to_binding},
            {**src._collided_binding_key_to_bindings, **child._collided_binding_key_to_bindings}
        )
