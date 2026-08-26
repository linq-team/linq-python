# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .webhook_event_type import WebhookEventType

__all__ = ["ChatBackgroundUpdatedWebhookEvent", "Data", "DataChat", "DataBackground"]


class DataChat(BaseModel):
    """Chat information"""

    id: str
    """Chat identifier"""

    is_group: Optional[bool] = None
    """Whether this is a group chat"""

    owner_handle: Optional[ChatHandle] = None
    """Your phone number's handle. Always has is_me=true."""


class DataBackground(BaseModel):
    """A chat transcript background. Fields are populated per `type`."""

    type: Literal["color", "dynamic", "photo"]
    """The background family."""

    image_url: Optional[str] = None
    """
    Photo: a hosted URL for the background image, whether you set it or a
    participant did. Apple stores the image, not the URL it came from, so the image
    is re-hosted and this is our URL rather than the one you supplied. `null` only
    if the image could not be hosted.
    """

    shades: Optional[List[str]] = None
    """Color: the two gradient stops as hex, top then bottom."""

    style: Optional[Literal["sky", "water", "aurora", "glitter"]] = None
    """Dynamic: the animated style."""

    variant: Optional[str] = None
    """Color: `custom` (the stored two colors) or a named swatch.

    Dynamic: the variant within the `style` (e.g. `sunrise`).
    """


class Data(BaseModel):
    """Payload for chat.background_updated webhook events."""

    chat: DataChat
    """Chat information"""

    actor_handle: Optional[ChatHandle] = None
    """Who changed it. `is_me` is true when your own number set it."""

    background: Optional[DataBackground] = None
    """A chat transcript background. Fields are populated per `type`."""


class ChatBackgroundUpdatedWebhookEvent(BaseModel):
    """Complete webhook payload for chat.background_updated events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for chat.background_updated webhook events."""

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
