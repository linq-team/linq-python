# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .poll import Poll
from ..._models import BaseModel
from ..shared.reaction import Reaction

__all__ = ["PollEnvelope"]


class PollEnvelope(BaseModel):
    """Message-level envelope returned by every poll endpoint."""

    chat_id: str

    created_at: datetime

    message_id: str
    """The poll-definition message's ID — reference this poll by it."""

    poll: Poll
    """Poll content — options and the aggregate voter count."""

    reactions: List[Reaction]
    """Tapbacks/stickers on the whole poll (message part 0)."""

    updated_at: datetime
