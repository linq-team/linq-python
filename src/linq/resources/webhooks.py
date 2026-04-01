# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import cast

from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.events_webhook_event import EventsWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    def events(self, payload: str) -> EventsWebhookEvent:
        return cast(
            EventsWebhookEvent,
            construct_type(
                type_=EventsWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooksResource(AsyncAPIResource):
    def events(self, payload: str) -> EventsWebhookEvent:
        return cast(
            EventsWebhookEvent,
            construct_type(
                type_=EventsWebhookEvent,
                value=json.loads(payload),
            ),
        )
