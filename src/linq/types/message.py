# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .reply_to import ReplyTo
from .message_effect import MessageEffect
from .shared.reaction import Reaction
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType
from .shared.link_part_response import LinkPartResponse
from .shared.text_part_response import TextPartResponse
from .shared.media_part_response import MediaPartResponse

__all__ = [
    "Message",
    "Part",
    "PartIMessageAppPartResponse",
    "PartIMessageAppPartResponseApp",
    "PartIMessageAppPartResponseLayout",
]


class PartIMessageAppPartResponseApp(BaseModel):
    """Identifies the iMessage app (Messages app extension) that backs the card."""

    bundle_id: str
    """Bundle identifier of the Messages app extension. Must not contain `:`."""

    name: str
    """Display name of the app, shown by Messages' fallback UI."""

    team_id: str
    """The app's 10-character uppercase alphanumeric team identifier."""

    app_store_id: Optional[int] = None
    """The owning app's App Store id (optional).

    When set, recipients without the iMessage app installed see a "Get the app"
    affordance.
    """


class PartIMessageAppPartResponseLayout(BaseModel):
    """Visible layout of the card.

    At least one of
    `caption`, `subcaption`, `trailing_caption`, `trailing_subcaption`, or `image_url` must be
    set, otherwise the card renders as an empty bubble.
    """

    caption: Optional[str] = None
    """Primary label, top-left and bold."""

    image_subtitle: Optional[str] = None
    """Overlay text shown below `image_title`. Requires `image_url`."""

    image_title: Optional[str] = None
    """Overlay text shown above the image. Requires `image_url`."""

    image_url: Optional[str] = None
    """Optional HTTPS URL of a preview image.

    The server downloads it and embeds it in the card as JPEG (10MB max, same fetch
    rules as media parts).
    """

    subcaption: Optional[str] = None
    """Secondary label, below `caption` on the left."""

    trailing_caption: Optional[str] = None
    """Label shown top-right."""

    trailing_subcaption: Optional[str] = None
    """Label shown below `trailing_caption`, on the right."""


class PartIMessageAppPartResponse(BaseModel):
    """An iMessage app card part."""

    app: PartIMessageAppPartResponseApp
    """Identifies the iMessage app (Messages app extension) that backs the card."""

    layout: PartIMessageAppPartResponseLayout
    """Visible layout of the card.

    At least one of `caption`, `subcaption`, `trailing_caption`,
    `trailing_subcaption`, or `image_url` must be set, otherwise the card renders as
    an empty bubble.
    """

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    type: Literal["imessage_app"]
    """Indicates this is an iMessage app card part."""

    url: str
    """The URL delivered to the iMessage app on tap."""

    fallback_text: Optional[str] = None
    """Fallback text for surfaces that cannot render the card."""

    session_id: Optional[str] = None
    """Client-supplied session identifier, echoed back when provided."""


Part: TypeAlias = Union[TextPartResponse, MediaPartResponse, LinkPartResponse, PartIMessageAppPartResponse]


class Message(BaseModel):
    id: str
    """Unique identifier for the message"""

    chat_id: str
    """ID of the chat this message belongs to"""

    created_at: datetime
    """When the message was created"""

    delivery_status: Literal["pending", "queued", "sent", "delivered", "received", "read", "failed"]
    """Current delivery status of a message"""

    is_delivered: bool
    """
    DEPRECATED: Use `delivery_status` instead (true when `delivery_status` is
    `delivered` or `read`). Whether the message has been delivered.
    """

    is_from_me: bool
    """Whether this message was sent by the authenticated user"""

    is_read: bool
    """DEPRECATED: Use `delivery_status == "read"` instead.

    Whether the message has been read.
    """

    updated_at: datetime
    """When the message was last updated"""

    delivered_at: Optional[datetime] = None
    """When the message was delivered"""

    effect: Optional[MessageEffect] = None
    """iMessage effect applied to a message (screen or bubble effect)"""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """DEPRECATED: Use from_handle instead. Phone number of the message sender."""

    from_handle: Optional[ChatHandle] = None
    """The sender of this message as a full handle object"""

    parts: Optional[List[Part]] = None
    """Message parts in order (text, media, and link)"""

    preferred_service: Optional[ServiceType] = None
    """Messaging service type"""

    read_at: Optional[datetime] = None
    """When the message was read"""

    reply_to: Optional[ReplyTo] = None
    """Indicates this message is a threaded reply to another message"""

    sent_at: Optional[datetime] = None
    """When the message was sent"""

    service: Optional[ServiceType] = None
    """Messaging service type"""
