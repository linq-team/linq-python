# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MessageUpdateStickerPlacementResponse"]


class MessageUpdateStickerPlacementResponse(BaseModel):
    status: Optional[str] = None

    success: Optional[bool] = None

    trace_id: Optional[str] = None
