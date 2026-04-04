# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .reaction import Reaction
from ..._models import BaseModel

__all__ = ["LinkPartResponse"]


class LinkPartResponse(BaseModel):
    """A rich link preview part"""

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    type: Literal["link"]
    """Indicates this is a rich link preview part"""

    value: str
    """The URL"""
