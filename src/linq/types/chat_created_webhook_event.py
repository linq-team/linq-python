# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType
from .shared.service_type import ServiceType

__all__ = ["ChatCreatedWebhookEvent", "Data"]


class Data(BaseModel):
    """Payload for chat.created webhook events.

    Matches GET /v3/chats/{chatId} response.
    """

    id: str
    """Unique identifier for the chat"""

    created_at: datetime
    """When the chat was created"""

    display_name: Optional[str] = None
    """Display name for the chat.

    Defaults to a comma-separated list of recipient handles. Can be updated for
    group chats.
    """

    handles: List[ChatHandle]
    """List of chat participants with full handle details.

    Always contains at least two handles (your phone number and the other
    participant).
    """

    is_group: bool
    """Whether this is a group chat"""

    updated_at: datetime
    """When the chat was last updated"""

    service: Optional[ServiceType] = None
    """Messaging service type"""


class ChatCreatedWebhookEvent(BaseModel):
    """Complete webhook payload for chat.created events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for chat.created webhook events.

    Matches GET /v3/chats/{chatId} response.
    """

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
