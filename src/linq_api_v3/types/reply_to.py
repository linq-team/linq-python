# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReplyTo"]


class ReplyTo(BaseModel):
    """Indicates this message is a threaded reply to another message"""

    message_id: str
    """The ID of the message to reply to"""

    part_index: Optional[int] = None
    """
    The specific message part to reply to (0-based index). Defaults to 0 (first
    part) if not provided. Use this when replying to a specific part of a multipart
    message.
    """
