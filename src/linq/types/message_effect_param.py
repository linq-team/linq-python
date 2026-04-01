# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessageEffectParam"]


class MessageEffectParam(TypedDict, total=False):
    """iMessage effect applied to a message (screen or bubble effect)"""

    name: str
    """Name of the effect. Common values:

    - Screen effects: confetti, fireworks, lasers, sparkles, celebration, hearts,
      love, balloons, happy_birthday, echo, spotlight
    - Bubble effects: slam, loud, gentle, invisible
    """

    type: Literal["screen", "bubble"]
    """Type of effect"""
