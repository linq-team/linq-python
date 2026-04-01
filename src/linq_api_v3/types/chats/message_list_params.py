# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous next_cursor response"""

    limit: int
    """Maximum number of messages to return"""
