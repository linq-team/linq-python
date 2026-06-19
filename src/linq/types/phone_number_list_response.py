# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberListResponse", "PhoneNumber", "PhoneNumberHealthStatus", "PhoneNumberReputation"]


class PhoneNumberHealthStatus(BaseModel):
    """**[BETA]** Current reputation for a phone line.

    Always present — lines start at `HEALTHY` and may shift based on aggregate engagement and delivery signals across all conversations on the line.

    Unlike chat health, line reputation does not include `opted_out` — opt-out applies to individual recipients, not the whole line.

    See the [Phone Health guide](/guides/phone-numbers/phone-health) for what each status means and how to react.
    """

    doc_url: str
    """Deep-link to the relevant section of the Phone Health guide for this status."""

    status: Literal["HEALTHY", "AT_RISK", "CRITICAL"]
    """Current reputation of this phone line as assessed by risk-service.

    - `HEALTHY` — No elevated risk detected.
    - `AT_RISK` — Elevated risk indicators present; consider reducing send volume or
      reviewing messaging patterns.
    - `CRITICAL` — High risk; further sending may result in line flagging or
      restriction.

    Defaults to `HEALTHY` for lines that have not yet been scored.
    """


class PhoneNumberReputation(BaseModel):
    """**[BETA]** Current reputation for a phone line.

    Always present — lines start at `HEALTHY` and may shift based on aggregate engagement and delivery signals across all conversations on the line.

    Unlike chat health, line reputation does not include `opted_out` — opt-out applies to individual recipients, not the whole line.

    See the [Phone Health guide](/guides/phone-numbers/phone-health) for what each status means and how to react.
    """

    doc_url: str
    """Deep-link to the relevant section of the Phone Health guide for this status."""

    status: Literal["HEALTHY", "AT_RISK", "CRITICAL"]
    """Current reputation of this phone line as assessed by risk-service.

    - `HEALTHY` — No elevated risk detected.
    - `AT_RISK` — Elevated risk indicators present; consider reducing send volume or
      reviewing messaging patterns.
    - `CRITICAL` — High risk; further sending may result in line flagging or
      restriction.

    Defaults to `HEALTHY` for lines that have not yet been scored.
    """


class PhoneNumber(BaseModel):
    id: str
    """Unique identifier for the phone number"""

    health_status: PhoneNumberHealthStatus
    """**[BETA]** Current reputation for a phone line.

    Always present — lines start at `HEALTHY` and may shift based on aggregate
    engagement and delivery signals across all conversations on the line.

    Unlike chat health, line reputation does not include `opted_out` — opt-out
    applies to individual recipients, not the whole line.

    See the [Phone Health guide](/guides/phone-numbers/phone-health) for what each
    status means and how to react.
    """

    phone_number: str
    """Phone number in E.164 format"""

    reputation: PhoneNumberReputation
    """**[BETA]** Current reputation for a phone line.

    Always present — lines start at `HEALTHY` and may shift based on aggregate
    engagement and delivery signals across all conversations on the line.

    Unlike chat health, line reputation does not include `opted_out` — opt-out
    applies to individual recipients, not the whole line.

    See the [Phone Health guide](/guides/phone-numbers/phone-health) for what each
    status means and how to react.
    """


class PhoneNumberListResponse(BaseModel):
    phone_numbers: List[PhoneNumber]
    """List of phone numbers assigned to the partner"""
