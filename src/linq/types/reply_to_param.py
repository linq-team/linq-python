# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReplyToParam"]


class ReplyToParam(TypedDict, total=False):
    """Indicates this message is a threaded reply to another message"""

    message_id: Required[str]
    """The ID of the message to reply to"""

    part_index: int
    """
    The specific message part to reply to (0-based index). Defaults to 0 (first
    part) if not provided. Use this when replying to a specific part of a multipart
    message.
    """
