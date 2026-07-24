# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .payment_request import PaymentRequest

__all__ = ["PaymentRequestListResponse"]


class PaymentRequestListResponse(BaseModel):
    data: List[PaymentRequest]

    has_more: bool
    """Whether more results exist beyond this page."""

    object: Literal["list"]
