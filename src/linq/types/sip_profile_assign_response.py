# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SipProfileAssignResponse"]


class SipProfileAssignResponse(BaseModel):
    phone_number: str
    """The phone number whose assignment changed"""

    sip_profile_id: Optional[str] = None
    """The assigned SIP profile id, or null when cleared"""
