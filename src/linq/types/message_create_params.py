# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .message_content_param import MessageContentParam

__all__ = ["MessageCreateParams", "ContinuationMessage"]


class MessageCreateParams(TypedDict, total=False):
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
    """Recipient handles (E.164 phone numbers or email addresses).

    One handle is a direct chat; multiple handles a group chat. Order-independent —
    the set identifies the chat.
    """

    continuation_message: ContinuationMessage
    """
    Text-only fallback that **replaces** `message` ONLY on the failover branch —
    when a chat with these recipients already existed but its line was flagged, so a
    new chat is created on a fresh line. On that branch this text is sent as the
    single message instead of `message` (the recipient is on a new number, so you
    typically want a fresh-number-appropriate opener rather than the original
    content). Ignored otherwise (a healthy reuse, or genuine first contact). Carries
    no parts, media, or effects — exactly one message is ever sent.
    """

    exclude_from: SequenceNotStr[str]
    """Lines (E.164) not to pick for this send.

    Applies for this request only — nothing is remembered between calls.

    **Exclusion only affects picking a line for a new chat.** If `to` already has a
    chat, that chat is reused on its own line, and a chat on a non-excluded line is
    preferred when there is more than one. If the only chat these recipients have is
    on an excluded line, it is still reused — an exclusion never abandons a live
    chat or moves it to a new number. Check `from` in the response to see the line
    that was actually used.

    Numbers that are not your lines are ignored. Every entry must be E.164 — a value
    like `4155551234` is rejected rather than silently skipped. Excluding every one
    of your available lines returns 400 when a line has to be picked.
    """

    override_optout: bool
    """Send even though the recipient asked you to stop (`403`, error code `2024`).

    Applies to this request only: the opt-out stays in place, so the next send
    without this flag is rejected again. Every override is recorded against your API
    key.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class ContinuationMessage(TypedDict, total=False):
    """
    Text-only fallback that **replaces** `message` ONLY on the failover branch —
    when a chat with these recipients already existed but its line was flagged,
    so a new chat is created on a fresh line. On that branch this text is sent as
    the single message instead of `message` (the recipient is on a new number, so
    you typically want a fresh-number-appropriate opener rather than the original
    content). Ignored otherwise (a healthy reuse, or genuine first contact).
    Carries no parts, media, or effects — exactly one message is ever sent.
    """

    text: Required[str]
    """The replacement message text, sent as the single message on failover."""
