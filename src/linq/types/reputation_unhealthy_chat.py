# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .reputation_driver_key import ReputationDriverKey

__all__ = ["ReputationUnhealthyChat"]


class ReputationUnhealthyChat(BaseModel):
    chat_id: Optional[str] = None

    driver_keys: Optional[List[ReputationDriverKey]] = None
    """
    What is dragging this conversation down, in the same vocabulary as the report's
    drivers. Each key's meaning and the fix for it are documented on
    `ReputationDriverKey`.
    """

    status: Optional[Literal["AT_RISK", "CRITICAL", "OPTED_OUT"]] = None
    """
    The conversation's current health — the same value `GET /v3/chats/{chatId}`
    reports for it.
    """
