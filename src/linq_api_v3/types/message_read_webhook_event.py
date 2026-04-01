# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .message_event_v2 import MessageEventV2
from .webhook_event_type import WebhookEventType

__all__ = ["MessageReadWebhookEvent"]


class MessageReadWebhookEvent(BaseModel):
    """Complete webhook payload for message.read events (2026-02-03 format)"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: MessageEventV2
    """Unified payload for message webhooks when using `webhook_version: "2026-02-03"`.

    This schema is used for message.sent, message.received, message.delivered, and
    message.read events when the subscription URL includes `?version=2026-02-03`.

    Key differences from V1 (2025-01-01):

    - `direction`: "inbound" or "outbound" instead of `is_from_me` boolean
    - `sender_handle`: Full handle object for the sender
    - `chat`: Nested object with `id`, `is_group`, and `owner_handle`
    - Message fields (`id`, `parts`, `effect`, etc.) are at the top level, not
      nested in `message`

    Timestamps indicate the message state:

    - `message.sent`: sent_at set, delivered_at=null, read_at=null
    - `message.received`: sent_at set, delivered_at=null, read_at=null
    - `message.delivered`: sent_at set, delivered_at set, read_at=null
    - `message.read`: sent_at set, delivered_at set, read_at set
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
