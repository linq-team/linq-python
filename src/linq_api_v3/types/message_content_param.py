# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .reply_to_param import ReplyToParam
from .link_part_param import LinkPartParam
from .text_part_param import TextPartParam
from .media_part_param import MediaPartParam
from .shared.service_type import ServiceType
from .message_effect_param import MessageEffectParam

__all__ = ["MessageContentParam", "Part"]

Part: TypeAlias = Union[TextPartParam, MediaPartParam, LinkPartParam]


class MessageContentParam(TypedDict, total=False):
    """Message content container.

    Groups all message-related fields together,
    separating the "what" (message content) from the "where" (routing fields like from/to).
    """

    parts: Required[Iterable[Part]]
    """Array of message parts.

    Each part can be text, media, or link. Parts are displayed in order. Text and
    media can be mixed freely, but a `link` part must be the only part in the
    message.

    **Rich Link Previews:**

    - Use a `link` part to send a URL with a rich preview card
    - A `link` part must be the **only** part in the message
    - To send a URL as plain text (no preview), use a `text` part instead

    **Supported Media:**

    - Images: .jpg, .jpeg, .png, .gif, .heic, .heif, .tif, .tiff, .bmp
    - Videos: .mp4, .mov, .m4v, .mpeg, .mpg, .3gp
    - Audio: .m4a, .mp3, .aac, .caf, .wav, .aiff, .amr
    - Documents: .pdf, .txt, .rtf, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx,
      .pages, .numbers, .key, .epub, .zip, .html, .htm
    - Contact & Calendar: .vcf, .ics

    **Audio:**

    - Audio files (.m4a, .mp3, .aac, .caf, .wav, .aiff, .amr) are fully supported as
      media parts
    - To send audio as an **iMessage voice memo bubble** (inline playback UI), use
      the dedicated `/v3/chats/{chatId}/voicememo` endpoint instead

    **Validation Rules:**

    - A `link` part must be the **only** part in the message. It cannot be combined
      with text or media parts.
    - Consecutive text parts are not allowed. Text parts must be separated by media
      parts. For example, [text, text] is invalid, but [text, media, text] is valid.
    - Maximum of **100 parts** total.
    - Media parts using a public `url` (downloaded by the server on send) are capped
      at **40**. Parts using `attachment_id` or presigned URLs are exempt from this
      sub-limit. For bulk media sends exceeding 40 files, pre-upload via
      `POST /v3/attachments` and reference by `attachment_id` or `download_url`.
    """

    effect: MessageEffectParam
    """iMessage effect to apply to this message (screen or bubble effect)"""

    idempotency_key: str
    """
    Optional idempotency key for this message. Use this to prevent duplicate sends
    of the same message.
    """

    preferred_service: ServiceType
    """Messaging service type"""

    reply_to: ReplyToParam
    """Reply to another message to create a threaded conversation"""
