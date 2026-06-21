# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType
from .schemas_message_effect import SchemasMessageEffect
from .schemas_text_part_response import SchemasTextPartResponse
from .schemas_media_part_response import SchemasMediaPartResponse

__all__ = [
    "MessageEventV2",
    "Chat",
    "ChatHealthStatus",
    "Part",
    "PartSchemasLinkPartResponse",
    "PartSchemasIMessageAppPartResponse",
    "PartSchemasIMessageAppPartResponseApp",
    "PartSchemasIMessageAppPartResponseLayout",
    "ReplyTo",
]


class ChatHealthStatus(BaseModel):
    """**[BETA]** Current health for a chat.

    Always present — chats start at `HEALTHY` and may shift based on engagement and delivery signals on the conversation. Many `AT_RISK` or `CRITICAL` chats on a single line increase the risk of line flagging.

    Switch on `status` to gate sends or surface line health in your UI — the enum is the long-term contract. Each status carries a `doc_url` that deep-links to the relevant section of the Chat Health guide.

    See the [Chat Health guide](/guides/chats/chat-health) for what each status means and how to react.
    """

    doc_url: str
    """Deep-link to the relevant section of the Chat Health guide for this status."""

    status: Literal["HEALTHY", "AT_RISK", "CRITICAL", "OPTED_OUT"]
    """Current health bucket for the chat.

    See the [Chat Health guide](/guides/chats/chat-health) for what each value means
    and how to react. `doc_url` deep-links to the relevant section.
    """

    updated_at: datetime
    """When this status last changed."""


class Chat(BaseModel):
    """Chat information"""

    id: str
    """Chat identifier"""

    health_status: ChatHealthStatus
    """**[BETA]** Current health for a chat.

    Always present — chats start at `HEALTHY` and may shift based on engagement and
    delivery signals on the conversation. Many `AT_RISK` or `CRITICAL` chats on a
    single line increase the risk of line flagging.

    Switch on `status` to gate sends or surface line health in your UI — the enum is
    the long-term contract. Each status carries a `doc_url` that deep-links to the
    relevant section of the Chat Health guide.

    See the [Chat Health guide](/guides/chats/chat-health) for what each status
    means and how to react.
    """

    is_group: Optional[bool] = None
    """Whether this is a group chat"""

    owner_handle: Optional[ChatHandle] = None
    """Your phone number's handle. Always has is_me=true."""


class PartSchemasLinkPartResponse(BaseModel):
    """A rich link preview part"""

    type: Literal["link"]
    """Indicates this is a rich link preview part"""

    value: str
    """The URL"""


class PartSchemasIMessageAppPartResponseApp(BaseModel):
    """Identifies the iMessage app (Messages app extension) that backs the card."""

    bundle_id: str
    """Bundle identifier of the Messages app extension."""

    name: str
    """Display name of the app."""

    team_id: str
    """The app's 10-character team identifier."""

    app_store_id: Optional[int] = None
    """The owning app's App Store id, when known."""


class PartSchemasIMessageAppPartResponseLayout(BaseModel):
    """Visible layout of the card."""

    caption: Optional[str] = None
    """Primary label, top-left and bold."""

    subcaption: Optional[str] = None
    """Secondary label, below caption on the left."""

    trailing_caption: Optional[str] = None
    """Label shown top-right."""

    trailing_subcaption: Optional[str] = None
    """Label shown below trailing_caption."""


class PartSchemasIMessageAppPartResponse(BaseModel):
    """An iMessage app card part."""

    app: PartSchemasIMessageAppPartResponseApp
    """Identifies the iMessage app (Messages app extension) that backs the card."""

    layout: PartSchemasIMessageAppPartResponseLayout
    """Visible layout of the card."""

    type: Literal["imessage_app"]
    """Indicates this is an iMessage app card part."""

    url: str
    """The URL delivered to the iMessage app on tap."""

    fallback_text: Optional[str] = None
    """Fallback text for surfaces that cannot render the card."""


Part: TypeAlias = Annotated[
    Union[
        SchemasTextPartResponse,
        SchemasMediaPartResponse,
        PartSchemasLinkPartResponse,
        PartSchemasIMessageAppPartResponse,
    ],
    PropertyInfo(discriminator="type"),
]


class ReplyTo(BaseModel):
    """Reference to the message this is replying to (for threaded replies)"""

    message_id: Optional[str] = None
    """ID of the message being replied to"""

    part_index: Optional[int] = None
    """Index of the part being replied to"""


class MessageEventV2(BaseModel):
    """Unified payload for message webhooks when using `webhook_version: "2026-02-03"`.

    This schema is used for message.sent, message.received, message.delivered, and message.read
    events when the subscription URL includes `?version=2026-02-03`.

    Key differences from V1 (2025-01-01):
    - `direction`: "inbound" or "outbound" instead of `is_from_me` boolean
    - `sender_handle`: Full handle object for the sender
    - `chat`: Nested object with `id`, `is_group`, and `owner_handle`
    - Message fields (`id`, `parts`, `effect`, etc.) are at the top level, not nested in `message`

    Timestamps indicate the message state:
    - `message.sent`: sent_at set, delivered_at=null, read_at=null
    - `message.received`: sent_at set, delivered_at=null, read_at=null
    - `message.delivered`: sent_at set, delivered_at set, read_at=null
    - `message.read`: sent_at set, delivered_at set, read_at set
    """

    id: str
    """Message identifier"""

    chat: Chat
    """Chat information"""

    direction: Literal["inbound", "outbound"]
    """Message direction - "outbound" if sent by you, "inbound" if received"""

    parts: List[Part]
    """Message parts (text and/or media)"""

    sender_handle: ChatHandle
    """The handle that sent this message"""

    service: ServiceType
    """Messaging service type"""

    delivered_at: Optional[datetime] = None
    """When the message was delivered. Null if not yet delivered."""

    effect: Optional[SchemasMessageEffect] = None
    """iMessage effect applied to a message (screen or bubble animation)"""

    idempotency_key: Optional[str] = None
    """Idempotency key for deduplication of outbound messages."""

    preferred_service: Optional[Literal["iMessage", "SMS", "RCS", "auto"]] = None
    """Preferred messaging service type.

    Includes "auto" for default fallback behavior.
    """

    read_at: Optional[datetime] = None
    """When the message was read. Null if not yet read."""

    reply_to: Optional[ReplyTo] = None
    """Reference to the message this is replying to (for threaded replies)"""

    sent_at: Optional[datetime] = None
    """When the message was sent. Null if not yet sent."""
