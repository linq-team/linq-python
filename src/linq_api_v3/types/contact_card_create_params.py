# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactCardCreateParams"]


class ContactCardCreateParams(TypedDict, total=False):
    first_name: Required[str]
    """First name for the contact card. Required."""

    phone_number: Required[str]
    """E.164 phone number to associate the contact card with"""

    image_url: str
    """URL of the profile image to rehost on the CDN.

    Only re-uploaded when a new value is provided.
    """

    last_name: str
    """Last name for the contact card. Optional."""
