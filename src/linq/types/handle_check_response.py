# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["HandleCheckResponse"]


class HandleCheckResponse(BaseModel):
    address: str
    """The recipient address that was checked"""

    available: bool
    """Whether the recipient supports the checked messaging service"""
