# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..message_content_param import MessageContentParam

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    message: Required[MessageContentParam]
    """Message content container.

    Groups all message-related fields together, separating the "what" (message
    content) from the "where" (routing fields like from/to).

    A message carries EITHER `parts` — text and attachments, which compose into one
    bubble — or a single `action`, which invokes an experience inside Linq's
    iMessage app. Never both: an app card is the whole message (Apple's `MSMessage`
    cannot coexist with text), so copy and a card are two sends, not one.
    """

    override_optout: bool
    """Send even though the recipient asked you to stop (`403`, error code `2024`).

    Applies to this request only: the opt-out stays in place, so the next send
    without this flag is rejected again. Every override is recorded against your API
    key.
    """
