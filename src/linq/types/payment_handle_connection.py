# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentHandleConnection"]


class PaymentHandleConnection(BaseModel):
    connect_id: Optional[str] = None
    """
    Returned only by `connect`, and only while the ceremony is pending. Nothing on
    our side persists it — it comes back from the provider and is required again to
    verify — so hold it until you submit the code.
    """

    handle: Optional[str] = None

    status: Optional[Literal["not_connected", "pending", "connected", "revoked"]] = None
