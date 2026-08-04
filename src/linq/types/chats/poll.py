# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from ..shared.chat_handle import ChatHandle

__all__ = ["Poll", "Option", "OptionVoter"]


class OptionVoter(BaseModel):
    handle: str

    voted_at: datetime


class Option(BaseModel):
    can_be_edited: bool

    creator_handle: ChatHandle
    """
    The participant who added this option (poll creator for the initial options;
    whoever added later ones).
    """

    option_id: str

    text: str

    voters: List[OptionVoter]
    """Participants who voted for this option (vote_count = voters.length)."""


class Poll(BaseModel):
    """Poll content — options and the aggregate voter count."""

    options: List[Option]

    total_voters: int
    """
    Distinct participants across the whole poll (a voter picking two options counts
    once).
    """
