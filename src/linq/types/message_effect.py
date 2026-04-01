# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageEffect"]


class MessageEffect(BaseModel):
    """iMessage effect applied to a message (screen or bubble effect)"""

    name: Optional[str] = None
    """Name of the effect. Common values:

    - Screen effects: confetti, fireworks, lasers, sparkles, celebration, hearts,
      love, balloons, happy_birthday, echo, spotlight
    - Bubble effects: slam, loud, gentle, invisible
    """

    type: Optional[Literal["screen", "bubble"]] = None
    """Type of effect"""
