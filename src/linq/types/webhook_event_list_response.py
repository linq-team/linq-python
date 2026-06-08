# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .webhook_event_type import WebhookEventType

__all__ = ["WebhookEventListResponse"]


class WebhookEventListResponse(BaseModel):
    doc_url: Literal["https://docs.linqapp.com/guides/webhooks/events"]
    """URL to the webhook events documentation"""

    events: List[WebhookEventType]
    """List of all available webhook event types"""
