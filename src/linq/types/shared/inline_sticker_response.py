# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["InlineStickerResponse"]


class InlineStickerResponse(BaseModel):
    """
    One sticker image placed inside the text of a part: `id`, `url` and the image details.
    """

    range: List[int]
    """Character range `[start, end)` in `value` that the sticker replaces.

    Those characters are hidden on iMessage and sent as written on SMS and RCS.
    _Characters are measured as UTF-16 code units. Most characters count as 1; some
    emoji count as 2._
    """

    id: Optional[str] = None
    """Attachment ID of the sticker image."""

    file_name: Optional[str] = None
    """Filename of the sticker"""

    mime_type: Optional[str] = None
    """MIME type of the sticker image"""

    url: Optional[str] = None
    """URL for downloading the sticker image.

    Permanent for a normal upload; a time-limited signed URL when the image is an
    ephemeral attachment.
    """
