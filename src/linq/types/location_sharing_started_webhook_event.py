# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LocationSharingStartedWebhookEvent", "Data"]


class Data(BaseModel):
    began_at: Optional[datetime] = None
    """When location sharing started.

    Always present: falls back to when the share was first observed if the device
    reported no start time.
    """

    chat_id: Optional[str] = None
    """The chat this share was first sent to.

    Location sharing is per-contact rather than per-chat, so the location may also
    be visible in other chats with the same handle; this identifies where the share
    originated and does not change if the contact later shares into another chat.
    Null when the originating chat could not be determined.
    """

    ends_at: Optional[datetime] = None
    """When location sharing will expire. Null when sharing indefinitely."""

    shared_by: str
    """Phone number of the person sharing their location"""

    shared_with: str
    """Your phone number receiving the location"""


class LocationSharingStartedWebhookEvent(BaseModel):
    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: Literal[
        "location.sharing.started",
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
        "contact_card.received",
        "call.initiated",
        "call.ringing",
        "call.answered",
        "call.ended",
        "call.failed",
        "call.declined",
        "call.no_answer",
        "location.sharing.stopped",
        "payment.succeeded",
        "payment.canceled",
        "payment.expired",
        "payment.declined",
        "payment.authorized",
        "connection.created",
        "connection.revoked",
    ]

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
