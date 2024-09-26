from typing import overload

__all__: list[str]

class ComplexWarning(RuntimeWarning): ...
class ModuleDeprecationWarning(DeprecationWarning): ...
class VisibleDeprecationWarning(UserWarning): ...
class RankWarning(RuntimeWarning): ...
class TooHardError(RuntimeError): ...
class DTypePromotionError(TypeError): ...

class AxisError(ValueError, IndexError):
    axis: None | int
    ndim: None | int
    @overload
    def __init__(self, axis: str, ndim: None = ..., msg_prefix: None = ...) -> None: ...
    @overload
    def __init__(self, axis: int, ndim: int, msg_prefix: None | str = ...) -> None: ...
    def __str__(self) -> str: ...
