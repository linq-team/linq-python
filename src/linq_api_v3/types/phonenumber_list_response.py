# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PhonenumberListResponse", "PhoneNumber", "PhoneNumberCapabilities"]


class PhoneNumberCapabilities(BaseModel):
    mms: bool
    """Whether MMS messaging is supported"""

    sms: bool
    """Whether SMS messaging is supported"""

    voice: bool
    """Whether voice calls are supported"""


class PhoneNumber(BaseModel):
    id: str
    """Unique identifier for the phone number"""

    phone_number: str
    """Phone number in E.164 format"""

    capabilities: Optional[PhoneNumberCapabilities] = None

    country_code: Optional[str] = None
    """Deprecated. Always null."""

    type: Optional[str] = None
    """Deprecated. Always null."""


class PhonenumberListResponse(BaseModel):
    phone_numbers: List[PhoneNumber]
    """List of phone numbers assigned to the partner"""
