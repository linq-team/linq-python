# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SipProfileAssignParams"]


class SipProfileAssignParams(TypedDict, total=False):
    sip_profile_id: Required[Optional[str]]
    """The SIP profile to assign, or null to clear the number's current assignment."""
