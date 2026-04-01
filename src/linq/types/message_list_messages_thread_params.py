# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessageListMessagesThreadParams"]


class MessageListMessagesThreadParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous next_cursor response"""

    limit: int
    """Maximum number of messages to return"""

    order: Literal["asc", "desc"]
    """Sort order for messages (asc = oldest first, desc = newest first)"""
