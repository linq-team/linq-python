from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `linq.resources` module.

    This is used so that we can lazily import `linq.resources` only when
    needed *and* so that users can just import `linq` and reference `linq.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("linq.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
