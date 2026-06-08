# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["LocationRequestResponse"]


class LocationRequestResponse(BaseModel):
    message: str

    success: bool
