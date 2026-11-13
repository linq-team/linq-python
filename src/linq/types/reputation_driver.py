# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .reputation_driver_key import ReputationDriverKey

__all__ = ["ReputationDriver"]


class ReputationDriver(BaseModel):
    key: Optional[ReputationDriverKey] = None
    """
    Stable driver-category identifier — what is dragging the line, or one of its
    conversations, down.

    - `low_engagement` — The conversation is one-sided: several messages sent, few
      or no replies back. Pause or rework outreach where recipients are not
      replying, and lead with messages that invite a response. Conversation-level:
      it appears on `evidence.unhealthy_chats[].driver_keys`, never in `drivers`.
    - `overall_conversation_health` — A large share of the line's active
      conversations are trending unhealthy. Fix the unhealthy conversations first —
      review their content and timing, and whether recipients are engaging.
    - `volume_spike` — The line's daily sending volume jumped far above its own
      normal level while few recipients were replying, or exceeded the recommended
      daily volume for a single line. Ramp volume gradually instead of spiking,
      prioritize people who have already engaged with you, and spread sustained high
      volume across additional lines.
    - `new_conversation_rate` — The line is starting too many brand-new
      conversations in a single day. Spread new conversations out over time instead
      of starting many at once.
    - `opt_out_handling` — Recipients asked this line to stop. Honor every stop
      request immediately: send nothing further to that recipient unless they opt
      back in. Every send to them is rejected with `403` (error code `2024`),
      including a final courtesy message — to send one telling them they can reply
      to resume, set `override_optout: true` on that single request.
    - `flagged` — This line has a delivery problem. Add a line or contact support.
      Our team can help move your conversations to a working line. On a line with no
      recent conversations: This line has a delivery problem. It has no recent
      conversations, so nothing needs to move. Our team can help you get a working
      line.
    - `other` — Fallback for a signal without dedicated partner copy.
    """

    metric: Optional[str] = None
    """A specific observed figure when available; otherwise a short qualitative note."""

    summary: Optional[str] = None
    """One plain-English sentence."""
