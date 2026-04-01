# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .webhook_event_type import WebhookEventType

__all__ = ["WebhookSubscriptionCreateParams"]


class WebhookSubscriptionCreateParams(TypedDict, total=False):
    subscribed_events: Required[List[WebhookEventType]]
    """List of event types to subscribe to"""

    target_url: Required[str]
    """URL where webhook events will be sent. Must be HTTPS."""

    phone_numbers: SequenceNotStr[str]
    """Optional list of phone numbers to filter events for.

    Only events originating from these phone numbers will be delivered to this
    subscription. If omitted or empty, events from all phone numbers are delivered.
    Phone numbers must be in E.164 format.
    """
