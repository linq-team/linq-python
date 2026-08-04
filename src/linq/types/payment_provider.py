# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentProvider"]


class PaymentProvider(BaseModel):
    provider: Optional[str] = None

    status: Optional[Literal["onboarding", "ready", "disabled"]] = None
