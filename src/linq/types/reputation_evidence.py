# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .reputation_opt_out_chat import ReputationOptOutChat
from .reputation_unhealthy_chat import ReputationUnhealthyChat

__all__ = ["ReputationEvidence"]


class ReputationEvidence(BaseModel):
    """
    The specific conversations behind the drivers, so partners can verify every claim against their own send logs. Each `chat_id` can be fetched via `GET /v3/chats/{chatId}` — its current health appears there.
    """

    opt_out_chats: Optional[List[ReputationOptOutChat]] = None
    """
    Worst first — most messages sent after the stop request; honor these
    immediately.
    """

    unhealthy_chats: Optional[List[ReputationUnhealthyChat]] = None
    """Up to 15, worst first."""
