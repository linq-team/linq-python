# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlockedHandleUnblockParams"]


class BlockedHandleUnblockParams(TypedDict, total=False):
    handle: Required[str]
    """The handle to unblock"""
