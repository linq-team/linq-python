# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ParticipantRemoveResponse"]


class ParticipantRemoveResponse(BaseModel):
    message: Optional[str] = None

    status: Optional[str] = None

    trace_id: Optional[str] = None
