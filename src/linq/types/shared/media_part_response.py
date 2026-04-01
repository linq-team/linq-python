# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .reaction import Reaction
from ..._models import BaseModel

__all__ = ["MediaPartResponse"]


class MediaPartResponse(BaseModel):
    """A media attachment part"""

    id: str
    """Unique attachment identifier"""

    filename: str
    """Original filename"""

    mime_type: str
    """MIME type of the file"""

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    size_bytes: int
    """File size in bytes"""

    type: Literal["media"]
    """Indicates this is a media attachment part"""

    url: str
    """Presigned URL for downloading the attachment (expires in 1 hour)."""
