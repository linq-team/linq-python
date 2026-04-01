# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .reaction import Reaction
from ..._models import BaseModel
from .text_decoration import TextDecoration

__all__ = ["TextPartResponse"]


class TextPartResponse(BaseModel):
    """A text message part"""

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    type: Literal["text"]
    """Indicates this is a text message part"""

    value: str
    """The text content"""

    text_decorations: Optional[List[TextDecoration]] = None
    """Text decorations applied to character ranges in the value"""
