# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .webhook_subscription import WebhookSubscription

__all__ = ["WebhookSubscriptionListResponse"]


class WebhookSubscriptionListResponse(BaseModel):
    subscriptions: List[WebhookSubscription]
    """List of webhook subscriptions"""
