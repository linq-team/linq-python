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
    image/tiff, image/bmp

    **Videos:** video/mp4, video/quicktime, video/mpeg, video/3gpp

    **Audio:** audio/mpeg, audio/mp4, audio/x-m4a, audio/x-caf, audio/wav,
    audio/aiff, audio/aac, audio/amr

    **Documents:** application/pdf, text/plain, text/markdown, text/vcard, text/rtf,
    text/csv, text/html, text/calendar, application/msword,
    application/vnd.openxmlformats-officedocument.wordprocessingml.document,
    application/vnd.ms-excel,
    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,
    application/vnd.ms-powerpoint,
    application/vnd.openxmlformats-officedocument.presentationml.presentation,
    application/vnd.apple.pages, application/vnd.apple.numbers,
    application/vnd.apple.keynote, application/epub+zip, application/zip

    **Unsupported:** WebP, SVG, FLAC, OGG, and executable files are explicitly
    rejected.
    """

    created_at: datetime
    """When the attachment was created"""

    filename: str
    """Original filename of the attachment"""

    size_bytes: int
    """Size of the attachment in bytes"""

    status: Literal["pending", "complete", "failed"]
    """Current upload/processing status"""

    download_url: Optional[str] = None
    """URL to download the attachment"""
