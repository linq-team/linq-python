# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallVoiceRecord"]


class CallVoiceRecord(BaseModel):
    """A carrier (BYOC) inbound voice call. Mirrors the call_voice.* webhook payload."""

    id: str
    """Stable call id, identical to the id in the call_voice.\\** webhooks."""

    direction: Literal["inbound"]

    from_: str = FieldInfo(alias="from")
    """External caller, E.164."""

    status: Optional[Literal["completed", "busy", "no_answer", "failed", "canceled"]] = None
    """Terminal call outcome.

    Null while the call is still in progress; set once it ends.
    """

    to: str
    """Your line that was called, E.164."""

    ended_at: Optional[datetime] = None
    """When the call ended. Null while still in progress."""

    started_at: Optional[datetime] = None
    """When the call was answered. Null if it never connected."""
