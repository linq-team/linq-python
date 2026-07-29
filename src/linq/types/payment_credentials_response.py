# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaymentCredentialsResponse", "Handoff"]


class Handoff(BaseModel):
    """Fetch the card directly from the provider with these — never through Linq."""

    card_ref: Optional[str] = None

    fetch_url: Optional[str] = None

    provider: Optional[str] = None

    user_token: Optional[str] = None
    """Short-lived bearer to fetch the card from the provider."""


class PaymentCredentialsResponse(BaseModel):
    handoff: Optional[Handoff] = None
    """Fetch the card directly from the provider with these — never through Linq."""
