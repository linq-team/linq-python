# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .reputation_driver import ReputationDriver
from .reputation_evidence import ReputationEvidence
from .reputation_action_item import ReputationActionItem

__all__ = ["ReputationReport"]


class ReputationReport(BaseModel):
    action_items: Optional[List[ReputationActionItem]] = None
    """Ordered by `priority`; 1 = do first."""

    drivers: Optional[List[ReputationDriver]] = None
    """Ranked, highest impact first."""

    evidence: Optional[ReputationEvidence] = None
    """
    The specific conversations behind the drivers, so partners can verify every
    claim against their own send logs. Each `chat_id` can be fetched via
    `GET /v3/chats/{chatId}` — its current health appears there.
    """

    primary_driver: Optional[str] = None
    """The `key` of the most important driver.

    Empty string when the line has nothing to act on — the report then carries a
    single reassurance action item. Its values are the `ReputationDriverKey`
    vocabulary — see that schema for what each means and what to do about it.
    """

    severity: Optional[Literal["HEALTHY", "AT_RISK", "CRITICAL"]] = None
    """Current reputation of this phone line.

    - `HEALTHY` — The line is in good standing. Send normally.
    - `AT_RISK` — Warning signs on the line: engagement is low across many of its
      conversations, or it's starting too many brand-new conversations in a single
      day — and a spike in send volume can add to either. Slow the line's send pace,
      avoid opening many new conversations at once, and review your messaging
      patterns.
    - `CRITICAL` — Strong signals that messages from this line aren't landing well.
      Pause outbound on the line until it recovers.

    Defaults to `HEALTHY` for lines that have not yet been scored.
    """

    summary_markdown: Optional[str] = None
    """
    Deterministic markdown rendering of this report, suitable for feeding directly
    to automated systems and AI agents as investigation context. Rendered from the
    structured fields above, which remain the source of truth.
    """
