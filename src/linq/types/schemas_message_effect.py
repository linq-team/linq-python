# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SchemasMessageEffect"]


class SchemasMessageEffect(BaseModel):
    """iMessage effect applied to a message (screen or bubble animation)"""

    name: Optional[str] = None
    """Effect name (confetti, fireworks, slam, gentle, etc.)"""

    type: Optional[Literal["screen", "bubble"]] = None
    """Effect category"""
