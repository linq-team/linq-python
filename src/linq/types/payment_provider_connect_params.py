# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentProviderConnectParams"]


class PaymentProviderConnectParams(TypedDict, total=False):
    return_url: Required[str]
    """Where to send the admin after they authorize the connection."""
