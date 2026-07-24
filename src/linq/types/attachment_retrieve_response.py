# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .supported_content_type import SupportedContentType

__all__ = ["AttachmentRetrieveResponse"]


class AttachmentRetrieveResponse(BaseModel):
    id: str
    """Unique identifier for the attachment (UUID)"""

    content_type: SupportedContentType
    """Supported MIME types for file attachments and media URLs.

    **Images:** image/jpeg, image/png, image/gif, image/heic, image/heif,
    image/tiff, image/bmp, image/svg+xml, image/webp, image/x-icon

    **Videos:** video/mp4, video/quicktime, video/mpeg, video/mpeg2,
    video/x-msvideo, video/3gpp

    **Audio:** audio/mpeg, audio/x-m4a, audio/x-caf, audio/x-wav, audio/x-aiff,
    audio/aac, audio/midi, audio/amr

    **Wallet passes:** application/vnd.apple.pkpass

    **Documents:** application/pdf, text/plain, text/markdown, text/vcard, text/rtf,
    text/csv, text/html, text/calendar, text/xml, application/json,
    application/msword,
    application/vnd.openxmlformats-officedocument.wordprocessingml.document,
    application/vnd.ms-excel,
    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,
    application/vnd.ms-powerpoint,
    application/vnd.openxmlformats-officedocument.presentationml.presentation,
    application/x-iwork-pages-sffpages, application/x-iwork-numbers-sffnumbers,
    application/x-iwork-keynote-sffkey, application/epub+zip, application/zip,
    application/x-gzip

    **Transcoded on delivery:**

    - `audio/x-caf` — CAF files are transcoded to `audio/mp4` for delivery.

    **Deprecated (accepted but transcoded):**

    - `audio/mp3` — Deprecated. Use `audio/mpeg` instead. Files sent as audio/mp3
      will be delivered as audio/mpeg.
    - `audio/mp4` — Deprecated. Use `audio/x-m4a` instead. Files sent as audio/mp4
      will be delivered as audio/x-m4a.
    - `audio/aiff` — Deprecated. Use `audio/x-aiff` instead. Files sent as
      audio/aiff will be delivered as audio/x-aiff.
    - `image/tiff` — Accepted, but TIFF images are transcoded to JPEG for delivery.

    **Unsupported:** FLAC, OGG, and executable files are explicitly rejected.
    """

    created_at: datetime
    """When the attachment was created"""

    filename: str
    """Original filename of the attachment"""

    size_bytes: int
    """Size of the attachment in bytes"""

    status: Literal["pending", "complete", "failed"]
    """
    **DEPRECATED:** This field is deprecated and will be removed in a future API
    version.
    """

    download_url: Optional[str] = None
    """URL to download the attachment"""
