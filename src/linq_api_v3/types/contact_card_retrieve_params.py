# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContactCardRetrieveParams"]


class ContactCardRetrieveParams(TypedDict, total=False):
    phone_number: str
    """E.164 phone number to filter by.

    If omitted, all my cards for the partner are returned.
    """
