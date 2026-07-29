# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PaymentCreateParams", "Merchant"]


class PaymentCreateParams(TypedDict, total=False):
    amount_cents: Required[int]

    currency: Required[str]

    handle: Required[str]
    """Customer phone (E.164) or email."""

    description: str

    merchant: Merchant

    metadata: Dict[str, str]


class Merchant(TypedDict, total=False):
    name: str

    url: str
