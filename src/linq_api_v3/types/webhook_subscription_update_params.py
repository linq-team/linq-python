# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .webhook_event_type import WebhookEventType

__all__ = ["WebhookSubscriptionUpdateParams"]


class WebhookSubscriptionUpdateParams(TypedDict, total=False):
    is_active: bool
    """Activate or deactivate the subscription"""

    phone_numbers: Optional[SequenceNotStr[str]]
    """Updated list of phone numbers to filter events for.

    Set to a non-empty array to filter events to specific phone numbers. Set to an
    empty array or null to remove the filter and receive events from all phone
    numbers. Phone numbers must be in E.164 format.
    """

    subscribed_events: List[WebhookEventType]
    """Updated list of event types to subscribe to"""

    target_url: str
    """New target URL for webhook events"""
