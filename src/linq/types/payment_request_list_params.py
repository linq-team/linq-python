# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PaymentRequestListParams"]


class PaymentRequestListParams(TypedDict, total=False):
    limit: int
    """Max results to return (default 20, max 100)."""

    offset: int
    """Number of results to skip."""

    status: Literal["requested", "authorized", "succeeded", "canceled", "expired", "declined"]
    """Filter by lifecycle status."""
