# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .sip_profile import SipProfile

__all__ = ["SipProfileListResponse"]


class SipProfileListResponse(BaseModel):
    sip_profiles: List[SipProfile]
    """The partner's SIP profiles"""
