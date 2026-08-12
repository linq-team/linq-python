# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReputationEvidence", "OptOutChat", "UnhealthyChat"]


class OptOutChat(BaseModel):
    chat_id: Optional[str] = None

    messages_after_stop: Optional[int] = None
    """Outbound messages sent after the recipient asked to stop."""


class UnhealthyChat(BaseModel):
    chat_id: Optional[str] = None

    driver_keys: Optional[
        List[
            Literal[
                "low_engagement",
                "overall_conversation_health",
                "volume_spike",
                "new_conversation_rate",
                "opt_out_handling",
                "flagged",
                "other",
            ]
        ]
    ] = None
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


class ReputationEvidence(BaseModel):
    """
    The specific conversations behind the drivers, so partners can verify every claim against their own send logs. Each `chat_id` can be fetched via `GET /v3/chats/{chatId}` — its current health appears there.
    """

    opt_out_chats: Optional[List[OptOutChat]] = None
    """
    Worst first — most messages sent after the stop request; honor these
    immediately.
    """

    unhealthy_chats: Optional[List[UnhealthyChat]] = None
    """Up to 15, worst first."""
