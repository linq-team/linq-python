# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChatListChatsParams"]


class ChatListChatsParams(TypedDict, total=False):
    cursor: str
    """
    Pagination cursor from the previous response's `next_cursor` field. Omit this
    parameter for the first page of results.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Phone number to filter chats by.

    Returns chats made from this phone number. Must be in E.164 format (e.g.,
    `+13343284472`). The `+` is automatically URL-encoded by HTTP clients. If
    omitted, returns chats across all phone numbers owned by the partner.
    """

    limit: int
    """Maximum number of chats to return per page"""

    to: str
    """Filter chats by a participant handle.

    Only returns chats where this handle is a participant. Can be an E.164 phone
    number (e.g., `+13343284472`) or an email address (e.g., `user@example.com`).
    For phone numbers, the `+` is automatically URL-encoded by HTTP clients.
    """
