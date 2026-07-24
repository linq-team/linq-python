# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberStatusUpdatedWebhookEvent", "Data"]


class Data(BaseModel):
    """Payload for phone_number.status_updated webhook events"""

    changed_at: datetime
    """When the status change occurred"""

    new_reputation: Literal["HEALTHY", "AT_RISK", "CRITICAL"]
    """The new line reputation"""

    new_status: Literal["ACTIVE", "FLAGGED"]
    """The new service status"""

    phone_number: str
    """Phone number in E.164 format"""

    previous_reputation: Literal["HEALTHY", "AT_RISK", "CRITICAL"]
    """The previous line reputation"""

    previous_status: Literal["ACTIVE", "FLAGGED"]
    """The previous service status"""


class PhoneNumberStatusUpdatedWebhookEvent(BaseModel):
    """Complete webhook payload for phone_number.status_updated events"""

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """Payload for phone_number.status_updated webhook events"""

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
        "participant.added",
        "participant.removed",
        "chat.created",
        "chat.group_name_updated",
        "chat.group_icon_updated",
        "chat.group_name_update_failed",
        "chat.group_icon_update_failed",
        "chat.background_updated",
        "chat.typing_indicator.started",
        "chat.typing_indicator.stopped",
        "phone_number.status_updated",
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
