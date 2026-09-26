# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ZeroDayRetentionUpdatedWebhookEvent",
    "Data",
    "DataActor",
    "DataAPIToken",
    "DataChange",
    "DataChangeName",
    "DataContactCard",
    "DataEnvironment",
    "DataTeamMember",
    "DataWebhookSubscription",
]


class DataActor(BaseModel):
    """Who made the change.

    `team_member` carries the member's id, name and email; other types carry no identity. `system` is a change made by Linq, matching "System" on your Activity page. `unknown` means the actor could not be identified.
    """

    type: Literal["team_member", "api", "system", "unknown"]

    id: Optional[str] = None
    """Team member's user ID. Only for `team_member`."""

    email: Optional[str] = None
    """Team member's email. Only for `team_member`."""

    name: Optional[str] = None
    """Team member's name. Only for `team_member`."""


class DataAPIToken(BaseModel):
    """The API token that changed."""

    id: str

    expires_at: Optional[datetime] = None
    """When the token expires.

    On `api_token.created`, `api_token.expired` and `api_token.deleted`; absent if
    it never expires.
    """

    name: Optional[str] = None
    """Absent when the token has no name."""

    token_prefix: Optional[str] = None
    """The token's visible prefix. On `api_token.created` and `api_token.deleted`."""


class DataChangeName(BaseModel):
    """A contact card name change.

    Only on `contact_card.updated`, when the name changed.
    """

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The name before the change; null when the card had no name."""

    to: Optional[str] = None
    """The name after the change; null when it was removed."""


class DataChange(BaseModel):
    """
    The transition an update event describes: `from` is the value before and `to` the value after. Present only on update events (`*.updated`, `*.renamed`, `*_changed`, `api_token.expiry_scheduled`, `environment.line_moved`, `webhook_subscription.routing_headers_*`); created, deleted, enabled, disabled, expired and activated events never carry it. `null` means none: `to: null` means cleared and `from: null` means first set. The value type depends on the event and is given in each event's description. `contact_card.updated` uses `name` instead of `from` and `to`.
    """

    from_: Optional[object] = FieldInfo(alias="from", default=None)
    """The value before the change; null when there was none."""

    name: Optional[DataChangeName] = None
    """A contact card name change.

    Only on `contact_card.updated`, when the name changed.
    """

    to: Optional[object] = None
    """The value after the change; null when it was cleared."""


class DataContactCard(BaseModel):
    """The contact card that changed."""

    id: str

    name: Optional[str] = None
    """Display name. Absent when the card has no name."""

    photo_updated: Optional[bool] = None
    """True when the photo changed. Only on `contact_card.updated`."""


class DataEnvironment(BaseModel):
    """An environment.

    Production is `{"id": null, "name": "Production", "type": "production"}`; every other environment has an `id` and type `environment`.
    """

    id: Optional[str] = None
    """Null for Production."""

    type: Literal["production", "environment"]

    name: Optional[str] = None


class DataTeamMember(BaseModel):
    """The team member the event is about."""

    id: str
    """The team member's user ID."""

    name: Optional[str] = None
    """Absent when the member has no name."""

    role: Optional[Literal["admin", "manager", "member"]] = None
    """Role the member joined with. Only on `team_member.added`."""


class DataWebhookSubscription(BaseModel):
    """The webhook subscription that changed."""

    id: str

    events: Optional[List[str]] = None
    """Event types it listens for. Only on `webhook_subscription.created`."""

    target_url: Optional[str] = None
    """Sent without credentials, query string or fragment."""


class Data(BaseModel):
    """A change on your account, the same change shown on your Activity page.

    Every event carries `summary`, `occurred_at`, `actor` and `origin`. The object fields (`api_token`, `webhook_subscription`, `environment`, `contact_card`, `phone_number`, `team_member`) identify what changed; on update events `change` describes the transition. Created and deleted events carry only the object that was created or deleted. Fields are absent when they don't apply; `null` appears only inside `change` and as Production's environment `id`.
    """

    actor: DataActor
    """Who made the change.

    `team_member` carries the member's id, name and email; other types carry no
    identity. `system` is a change made by Linq, matching "System" on your Activity
    page. `unknown` means the actor could not be identified.
    """

    occurred_at: datetime
    """When the change happened."""

    origin: Literal["dashboard", "api", "linq"]
    """Where the change was made."""

    summary: str
    """Human-readable label, identical to the Activity page.

    For display only; the wording may change without a new webhook version.
    """

    api_token: Optional[DataAPIToken] = None
    """The API token that changed."""

    change: Optional[DataChange] = None
    """
    The transition an update event describes: `from` is the value before and `to`
    the value after. Present only on update events (`*.updated`, `*.renamed`,
    `*_changed`, `api_token.expiry_scheduled`, `environment.line_moved`,
    `webhook_subscription.routing_headers_*`); created, deleted, enabled, disabled,
    expired and activated events never carry it. `null` means none: `to: null` means
    cleared and `from: null` means first set. The value type depends on the event
    and is given in each event's description. `contact_card.updated` uses `name`
    instead of `from` and `to`.
    """

    contact_card: Optional[DataContactCard] = None
    """The contact card that changed."""

    environment: Optional[DataEnvironment] = None
    """An environment.

    Production is `{"id": null, "name": "Production", "type": "production"}`; every
    other environment has an `id` and type `environment`.
    """

    lines_moved_to_production: Optional[int] = None
    """Lines moved to Production when an environment was deleted."""

    method: Optional[Literal["code", "sso", "google", "apple", "linkedin"]] = None
    """How the team member signed in.

    `code` is a one-time code sent by email or text. Only on
    `team_member.signed_in`.
    """

    phone_number: Optional[str] = None
    """The line the change is about, in E.164 format."""

    team_member: Optional[DataTeamMember] = None
    """The team member the event is about."""

    tokens_revoked: Optional[int] = None
    """API tokens revoked when an environment was deleted."""

    webhook_subscription: Optional[DataWebhookSubscription] = None
    """The webhook subscription that changed."""


class ZeroDayRetentionUpdatedWebhookEvent(BaseModel):
    """Webhook payload for account events.

    One event type per kind of account change. `event_id` is the same on every retry and on every subscription the event is delivered to; use it to deduplicate. `created_at` is when the webhook was created and `data.occurred_at` when the change happened. Events are not guaranteed to arrive in order. Delivery is best-effort: if a delivery still fails after retries, the change remains on your Activity page. Changes to webhook subscriptions are account events too, so a subscription to `webhook_subscription.*` events receives an event about the subscription that was just created or edited.
    """

    api_version: str
    """API version for the webhook payload format"""

    created_at: datetime
    """When the event was created"""

    data: Data
    """A change on your account, the same change shown on your Activity page.

    Every event carries `summary`, `occurred_at`, `actor` and `origin`. The object
    fields (`api_token`, `webhook_subscription`, `environment`, `contact_card`,
    `phone_number`, `team_member`) identify what changed; on update events `change`
    describes the transition. Created and deleted events carry only the object that
    was created or deleted. Fields are absent when they don't apply; `null` appears
    only inside `change` and as Production's environment `id`.
    """

    event_id: str
    """Unique identifier for this event (for deduplication)"""

    event_type: Literal[
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
