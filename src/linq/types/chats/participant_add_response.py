# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ParticipantAddResponse"]


class ParticipantAddResponse(BaseModel):
    message: Optional[str] = None

    status: Optional[str] = None

    trace_id: Optional[str] = None
