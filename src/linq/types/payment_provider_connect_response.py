# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaymentProviderConnectResponse"]


class PaymentProviderConnectResponse(BaseModel):
    hosted_url: Optional[str] = None
    """Send the admin here to authorize the connection."""

    session_id: Optional[str] = None

    status: Optional[str] = None
