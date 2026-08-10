# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["BlockedHandleEntry"]


class BlockedHandleEntry(BaseModel):
    blocked_at: datetime
    """When the handle was blocked"""

    handle: str
    """
    The blocked handle, normalized (E.164 phone, lowercased email, short code, or
    sender ID)
    """

    reason: Optional[str] = None
    """Optional note recorded when the handle was blocked"""
