# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentHandleVerifyParams"]


class PaymentHandleVerifyParams(TypedDict, total=False):
    code: Required[str]
    """The one-time code the customer received."""

    connect_id: Required[str]
    """The id returned by `connect`."""
