# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Payment", "Merchant"]


class Merchant(BaseModel):
    """The merchant the card is minted against, echoed from the request."""

    name: Optional[str] = None

    url: Optional[str] = None


class Payment(BaseModel):
    id: Optional[str] = None

    amount_cents: Optional[int] = None

    approval_url: Optional[str] = None
    """
    Present on `awaiting_user_action` once a card is on file and the charge needs
    the customer's passkey. Re-send the create request with the same
    `Idempotency-Key` to collect the payment after they approve.
    """

    attach_url: Optional[str] = None
    """Present on `awaiting_user_action` when the customer has no card on file yet.

    A hosted page — open it for them; it stays valid for about 48 hours. Not
    returned on `needs_connection`: connect the handle first.
    """

    currency: Optional[str] = None

    description: Optional[str] = None

    handle: Optional[str] = None

    merchant: Optional[Merchant] = None
    """The merchant the card is minted against, echoed from the request."""

    metadata: Optional[Dict[str, str]] = None
    """Your own key/values, echoed back from the request."""

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
