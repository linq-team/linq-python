# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SetContactCard"]


class SetContactCard(BaseModel):
    first_name: str
    """First name on the contact card"""

    is_active: bool
    """Whether the contact card was successfully applied to the device"""

    phone_number: str
    """The phone number the contact card is associated with"""

    image_url: Optional[str] = None
    """Image URL on the contact card"""

    last_name: Optional[str] = None
    """Last name on the contact card"""
