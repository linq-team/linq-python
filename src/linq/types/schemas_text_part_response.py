# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.text_decoration import TextDecoration

__all__ = ["SchemasTextPartResponse"]


class SchemasTextPartResponse(BaseModel):
    """A text message part"""

    type: Literal["text"]
    """Indicates this is a text message part"""

    value: str
    """The text content"""

    mention: Optional[str] = None
    """
    Handle (E.164 phone number or Apple ID email) of the @mentioned chat
    participant, as sent. `null` when the part carries no mention.
    """

    mention_range: Optional[List[int]] = None
    """
    Character range `[start, end)` in `value` highlighted as the mention, as sent.
    `null` when the send omitted it (the whole `value` is highlighted) or the part
    carries no mention. _Characters are measured as UTF-16 code units. Most
    characters count as 1; some emoji count as 2._
    """

    text_decorations: Optional[List[TextDecoration]] = None
    """Text decorations applied to character ranges in the value"""
