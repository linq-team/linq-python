# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .webhook_event_type import WebhookEventType

__all__ = ["WebhookSubscription"]


class WebhookSubscription(BaseModel):
    id: str
    """Unique identifier for the webhook subscription"""

    created_at: datetime
    """When the subscription was created"""

    is_active: bool
    """Whether this subscription is currently active"""

    subscribed_events: List[WebhookEventType]
    """List of event types this subscription receives"""

    target_url: str
    """URL where webhook events will be sent"""

    updated_at: datetime
    """When the subscription was last updated"""

    phone_numbers: Optional[List[str]] = None
    """Phone numbers this subscription filters for.

    If null or empty, events from all phone numbers are delivered.
    """
