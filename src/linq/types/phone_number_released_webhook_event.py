# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberReleasedWebhookEvent", "Data"]


class Data(BaseModel):
    """Payload for phone_number.assigned and phone_number.released webhook events"""

    changed_at: datetime
    """When the ownership change occurred"""

    phone_number: str
    """Phone number in E.164 format"""


class PhoneNumberReleasedWebhookEvent(BaseModel):
    """Complete webhook payload for phone_number.released events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for phone_number.assigned and phone_number.released webhook events"""

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: Literal[
        "message.sent",
        "message.received",
        "message.read",
        "message.delivered",
        "message.failed",
        "message.edited",
        "reaction.added",
        "reaction.removed",
        "poll.received",
        "poll.failed",
        "poll.sent",
        "poll.delivered",
        "poll.read",
        "poll.updated",
        "poll.vote.added",
        "poll.vote.removed",
        "poll.reaction.added",
        "participant.added",
        "participant.removed",
        "chat.created",
        "chat.group_name_updated",
        "chat.group_icon_updated",
        "chat.group_name_update_failed",
        "chat.group_icon_update_failed",
        "chat.background_updated",
        "chat.background_update_failed",
        "chat.typing_indicator.started",
        "chat.typing_indicator.stopped",
        "phone_number.status_updated",
        "phone_number.assigned",
        "phone_number.released",
        "contact_card.received",
        "call.initiated",
        "call.ringing",
        "call.answered",
        "call.ended",
        "call.failed",
        "call.declined",
        "call.no_answer",
        "location.sharing.started",
        "location.sharing.stopped",
        "payment.succeeded",
        "payment.canceled",
        "payment.expired",
        "payment.declined",
        "payment.authorized",
        "connection.created",
        "connection.revoked",
    ]
    """The type of event"""

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
