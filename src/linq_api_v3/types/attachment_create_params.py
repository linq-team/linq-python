# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .supported_content_type import SupportedContentType

__all__ = ["AttachmentCreateParams"]


class AttachmentCreateParams(TypedDict, total=False):
    content_type: Required[SupportedContentType]
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

    filename: Required[str]
    """Name of the file to upload"""

    size_bytes: Required[int]
    """Size of the file in bytes (max 100MB)"""
