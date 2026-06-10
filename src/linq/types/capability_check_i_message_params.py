# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CapabilityCheckIMessageParams"]


class CapabilityCheckIMessageParams(TypedDict, total=False):
    address: Required[str]
    """The recipient phone number or email address to check"""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Optional sender phone number.

    If omitted, an available phone from your pool is used automatically.
    """
