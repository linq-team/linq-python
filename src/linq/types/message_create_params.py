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
