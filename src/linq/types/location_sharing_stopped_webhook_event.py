# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LocationSharingStoppedWebhookEvent", "Data"]


class Data(BaseModel):
    began_at: Optional[datetime] = None
    """When the sharing session started, matching began_at on its started event.

    Always present.
    """

    chat_id: Optional[str] = None
    """
    The chat the ended share was first sent to, matching the chat_id on its started
    event. Sharing always stops for the contact as a whole, never for a single chat,
    so this is the session's origin rather than the chat it stopped in. Null when
    the originating chat could not be determined.
    """

    ended_at: datetime
    """When the sharing session was observed to stop."""

    shared_by: str
    """Phone number of the person who stopped sharing"""

    shared_with: str
    """Your phone number that was receiving the location"""


class LocationSharingStoppedWebhookEvent(BaseModel):
    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: Literal[
        "location.sharing.stopped",
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
        "location.sharing.started",
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
