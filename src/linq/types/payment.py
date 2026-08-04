# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Payment"]


class Payment(BaseModel):
    id: Optional[str] = None

    amount_cents: Optional[int] = None

    approval_url: Optional[str] = None
    """Present when the customer must approve with a passkey."""

    attach_url: Optional[str] = None
    """Present when the customer must attach a card."""

    currency: Optional[str] = None

    description: Optional[str] = None

    handle: Optional[str] = None

    status: Optional[
        Literal[
            "needs_connection",
            "connecting",
            "awaiting_user_action",
            "ready",
            "authorized",
            "succeeded",
            "declined",
            "canceled",
            "expired",
        ]
    ] = None
