# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    forwarding_number: Required[Optional[str]]
    """The forwarding number in E.164 format. Set to null or empty string to clear."""
