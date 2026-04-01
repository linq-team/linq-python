# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactCardUpdateParams"]


class ContactCardUpdateParams(TypedDict, total=False):
    phone_number: Required[str]
    """E.164 phone number of the contact card to update"""

    first_name: str
    """Updated first name. If omitted, the existing value is kept."""

    image_url: str
    """Updated profile image URL. If omitted, the existing image is kept."""

    last_name: str
    """Updated last name. If omitted, the existing value is kept."""
