# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .message_content_param import MessageContentParam

__all__ = ["ChatCreateParams"]


class ChatCreateParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Sender phone number in E.164 format.

    Must be a phone number that the authenticated partner has permission to send
    from.
    """

    message: Required[MessageContentParam]
    """Message content container.

    Groups all message-related fields together, separating the "what" (message
    content) from the "where" (routing fields like from/to).

    A message carries EITHER `parts` — text and attachments, which compose into one
    bubble — or a single `action`, which invokes an experience inside Linq's
    iMessage app. Never both: an app card is the whole message (Apple's `MSMessage`
    cannot coexist with text), so copy and a card are two sends, not one.
    """

    to: Required[SequenceNotStr[str]]
    """
    Array of recipient handles (phone numbers in E.164 format or email addresses).
    For individual chats, provide one recipient. For group chats, provide multiple.
    """

    override_optout: bool
    """Send even though the recipient asked you to stop (`403`, error code `2024`).

    Applies to this request only: the opt-out stays in place, so the next send
    without this flag is rejected again. Every override is recorded against your API
    key.
    """
