# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookEventType"]

WebhookEventType: TypeAlias = Literal[
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
]
