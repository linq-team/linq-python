# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CapabilityCheckRCSParams"]


class CapabilityCheckRCSParams(TypedDict, total=False):
    address: Required[str]
    """The recipient address to check.

    `check_imessage` accepts an E.164 phone number or an email address; `check_rcs`
    accepts an E.164 phone number only and rejects an email with a `400`, since RCS
    has no email addressing.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Optional sender phone number.

    If omitted, an available phone from your pool is used automatically.
    """
