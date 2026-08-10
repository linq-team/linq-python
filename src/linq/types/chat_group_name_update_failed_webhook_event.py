# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .webhook_event_type import WebhookEventType

__all__ = ["ChatGroupNameUpdateFailedWebhookEvent", "Data"]


class Data(BaseModel):
    """
    Error details for chat.group_name_update_failed webhook events.
    See [WebhookErrorCode](#/components/schemas/WebhookErrorCode) for the full error code reference.
    """

    chat_id: str
    """Chat identifier (UUID) of the group chat"""

    error_code: int
    """Error codes in webhook failure events.

    The possible set varies by event: message.failed can carry 3007, 4001, 4002,
    4005, 4006, 4007, or 4008; the group update failure events
    (chat.group_name_update_failed, chat.group_icon_update_failed) carry 3007
    or 4001.
    """

    failed_at: datetime
    """When the failure was detected"""


class ChatGroupNameUpdateFailedWebhookEvent(BaseModel):
    """Complete webhook payload for chat.group_name_update_failed events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """
    Error details for chat.group_name_update_failed webhook events. See
    [WebhookErrorCode](#/components/schemas/WebhookErrorCode) for the full error
    code reference.
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
