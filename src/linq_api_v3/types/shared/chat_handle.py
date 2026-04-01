# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .service_type import ServiceType

__all__ = ["ChatHandle"]


class ChatHandle(BaseModel):
    id: str
    """Unique identifier for this handle"""

    handle: str
    """Phone number (E.164) or email address of the participant"""

    joined_at: datetime
    """When this participant joined the chat"""

    service: ServiceType
    """Messaging service type"""

    is_me: Optional[bool] = None
    """Whether this handle belongs to the sender (your phone number)"""

    left_at: Optional[datetime] = None
    """When they left (if applicable)"""

    status: Optional[Literal["active", "left", "removed"]] = None
    """Participant status"""
