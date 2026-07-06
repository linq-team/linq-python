# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PhoneNumberUpdateResponse"]


class PhoneNumberUpdateResponse(BaseModel):
    id: str
    """Unique identifier for the phone number"""

    forwarding_number: Optional[str] = None
    """The forwarding number after the update. Null when cleared."""

    phone_number: str
    """Phone number in E.164 format"""
