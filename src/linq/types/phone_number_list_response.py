# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberListResponse", "PhoneNumber", "PhoneNumberReputation"]


class PhoneNumberReputation(BaseModel):
    """**[BETA]** Current reputation for a phone line.

    Always present — lines start at `HEALTHY` and may shift based on aggregate engagement and delivery signals across all conversations on the line.

    Unlike chat health, line reputation does not include `opted_out` — opt-out applies to individual recipients, not the whole line.

    See the [Phone Reputation guide](/guides/phone-numbers/phone-reputation) for what each status means and how to react.
    """

    doc_url: str
    """
    Deep-link to the relevant section of the Phone Reputation guide for this status.
    """

    status: Literal["HEALTHY", "AT_RISK", "CRITICAL"]
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


class PhoneNumber(BaseModel):
    id: str
    """Unique identifier for the phone number"""

    phone_number: str
    """Phone number in E.164 format"""

    reputation: PhoneNumberReputation
    """**[BETA]** Current reputation for a phone line.

    Always present — lines start at `HEALTHY` and may shift based on aggregate
    engagement and delivery signals across all conversations on the line.

    Unlike chat health, line reputation does not include `opted_out` — opt-out
    applies to individual recipients, not the whole line.

    See the [Phone Reputation guide](/guides/phone-numbers/phone-reputation) for
    what each status means and how to react.
    """

    forwarding_number: Optional[str] = None
    """The forwarding number associated with this phone number, in E.164 format.

    Null when no forwarding number is configured.
    """


class PhoneNumberListResponse(BaseModel):
    phone_numbers: List[PhoneNumber]
    """List of phone numbers assigned to the partner"""
