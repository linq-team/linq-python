# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SipProfile"]


class SipProfile(BaseModel):
    id: str
    """Unique identifier for the SIP profile"""

    assigned_number_count: int
    """How many phone numbers reference this profile"""

    created_at: datetime

    name: str
    """Human-readable name"""

    primary_uri: str
    """
    Your SIP endpoint as scheme + host (`sip:` UDP / `sips:` TLS); no user part — we
    set it to the called number on each call.
    """

    updated_at: datetime

    version: int
    """Monotonic version, incremented on each update"""

    backup_uri: Optional[str] = None
    """Optional failover SIP URI. Null when unset."""
