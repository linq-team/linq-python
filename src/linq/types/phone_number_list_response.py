# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["PhoneNumberListResponse", "PhoneNumber"]


class PhoneNumber(BaseModel):
    id: str
    """Unique identifier for the phone number"""

    phone_number: str
    """Phone number in E.164 format"""


class PhoneNumberListResponse(BaseModel):
    phone_numbers: List[PhoneNumber]
    """List of phone numbers assigned to the partner"""
