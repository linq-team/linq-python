# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = ["ChatGroupIconUpdatedWebhookEvent", "Data"]


class Data(BaseModel):
    """Payload for chat.group_icon_updated webhook events"""

    chat_id: str
    """Chat identifier (UUID) of the group chat"""

    updated_at: datetime
    """When the update occurred"""

    changed_by_handle: Optional[ChatHandle] = None
    """The handle who made the change."""

    new_value: Optional[str] = None
    """New icon URL (null if the icon was removed)"""

    old_value: Optional[str] = None
    """Previous icon URL (null if no previous icon)"""


class ChatGroupIconUpdatedWebhookEvent(BaseModel):
    """Complete webhook payload for chat.group_icon_updated events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for chat.group_icon_updated webhook events"""

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: WebhookEventType
    """Valid webhook event types that can be subscribed to.

    **Note:** `message.edited` is only delivered to subscriptions using
    `webhook_version: "2026-02-03"`. Subscribing to this event on a v2025
    subscription will not produce any deliveries.
    """

    partner_id: str
    """Partner identifier. Present on all webhooks for cross-referencing."""

    trace_id: str
    """Trace ID for debugging and correlation across systems."""

    webhook_version: str
    """
    Date-based webhook payload version. Determined by the `?version=` query
    parameter in your webhook subscription URL. If no version parameter is
    specified, defaults based on subscription creation date.
    """
