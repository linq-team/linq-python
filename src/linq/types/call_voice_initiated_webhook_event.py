# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallVoiceInitiatedWebhookEvent", "Data"]


class Data(BaseModel):
    id: str
    """Carrier voice call ID"""

    direction: Literal["inbound"]

    from_: str = FieldInfo(alias="from")
    """External caller, E.164"""

    status: Optional[Literal["completed", "busy", "no_answer", "failed", "canceled"]] = None
    """Terminal call outcome.

    Null on progress events (initiated/ringing/answered); set once the call ends.
    """

    to: str
    """Your line that was called, E.164"""

    ended_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


class CallVoiceInitiatedWebhookEvent(BaseModel):
    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: Literal[
        "call_voice.initiated",
        "call_voice.ringing",
        "call_voice.answered",
        "call_voice.ended",
        "call_voice.failed",
        "call_voice.declined",
        "call_voice.no_answer",
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
        "phone_number.line_type_updated",
        "contact_card.received",
        "location.sharing.started",
        "location.sharing.stopped",
        "payment.succeeded",
        "payment.canceled",
        "payment.expired",
        "payment.declined",
        "payment.authorized",
        "connection.created",
        "connection.revoked",
        "zero_day_retention.updated",
        "phone_number.forwarding_updated",
        "environment.line_moved",
        "contact_card.created",
        "contact_card.updated",
        "contact_card.deleted",
        "api_token.created",
        "api_token.renamed",
        "api_token.expiry_scheduled",
        "api_token.expired",
        "api_token.activated",
        "api_token.deleted",
        "environment.created",
        "environment.renamed",
        "environment.deleted",
        "webhook_subscription.created",
        "webhook_subscription.deleted",
        "webhook_subscription.target_url_changed",
        "webhook_subscription.enabled",
        "webhook_subscription.disabled",
        "webhook_subscription.events.updated",
        "webhook_subscription.phone_numbers.updated",
        "webhook_subscription.routing_headers_set",
        "webhook_subscription.routing_headers_cleared",
        "team_member.added",
        "team_member.signed_in",
        "team_member.signed_out",
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
