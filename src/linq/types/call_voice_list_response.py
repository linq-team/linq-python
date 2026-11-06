# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .call_voice_record import CallVoiceRecord

__all__ = ["CallVoiceListResponse"]


class CallVoiceListResponse(BaseModel):
    call_voice: List[CallVoiceRecord]
    """Calls for the phone number, newest first."""

    next_cursor: Optional[str] = None
    """Cursor for the next page of results.

    Null when there are no more. Pass this value as the `cursor` parameter in the
    next request.
    """
