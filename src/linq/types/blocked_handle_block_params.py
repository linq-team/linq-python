# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlockedHandleBlockParams"]


class BlockedHandleBlockParams(TypedDict, total=False):
    handle: Required[str]
    """
    The handle to block: an E.164 phone number, an email address, an SMS short code
    (3-8 digits), or an alphanumeric sender ID.
    """

    reason: str
    """Optional free-text note on why the handle was blocked"""
