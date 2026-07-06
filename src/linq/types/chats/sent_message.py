# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..reply_to import ReplyTo
from ..message_effect import MessageEffect
from ..shared.reaction import Reaction
from ..shared.chat_handle import ChatHandle
from ..shared.service_type import ServiceType
from ..shared.link_part_response import LinkPartResponse
from ..shared.text_part_response import TextPartResponse
from ..shared.media_part_response import MediaPartResponse

__all__ = [
    "SentMessage",
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

    `image_url` displays a preview image at the top of the card. The image renders on the
    recipient's card whether or not they have your app installed. The small icon beside the
    caption is the app's own icon and is not settable here.

    `* Note - requires a trusted chat w/ inbound activity`

    `image_title` and `image_subtitle` render as text overlaid on the image (title bold, subtitle
    beneath it). They only appear when `image_url` is set — without an image there is nothing to
    overlay — so setting either without `image_url` is rejected.
    """

    caption: Optional[str] = None
    """Primary label, top-left and bold."""

    image_subtitle: Optional[str] = None
    """Text shown below `image_title`, overlaid on the card image.

    Requires `image_url`.
    """

    image_title: Optional[str] = None
    """Bold text overlaid on the card image.

    Requires `image_url` (rejected without it).
    """

    image_url: Optional[str] = None
    """
    URL of an image (JPEG, PNG, HEIF, or WebP) to display as the card's preview
    image; an unreachable or non-image URL returns a validation error. Renders for
    all recipients regardless of whether they have the app. Note - requires a
    trusted chat w/ inbound activity. In responses, this is the re-hosted
    `cdn.linqapp.com` copy of the image you supplied, not your original URL.
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

    `image_url` displays a preview image at the top of the card. The image renders
    on the recipient's card whether or not they have your app installed. The small
    icon beside the caption is the app's own icon and is not settable here.

    `* Note - requires a trusted chat w/ inbound activity`

    `image_title` and `image_subtitle` render as text overlaid on the image (title
    bold, subtitle beneath it). They only appear when `image_url` is set — without
    an image there is nothing to overlay — so setting either without `image_url` is
    rejected.
    """

    reactions: Optional[List[Reaction]] = None
    """Reactions on this message part"""

    type: Literal["imessage_app"]
    """Indicates this is an iMessage app card part."""

    url: str
    """The URL delivered to the iMessage app on tap."""

    fallback_text: Optional[str] = None
    """Fallback text for surfaces that cannot render the card."""


Part: TypeAlias = Union[TextPartResponse, MediaPartResponse, LinkPartResponse, PartIMessageAppPartResponse]


class SentMessage(BaseModel):
    """A message that was sent (used in CreateChat and SendMessage responses)"""

    id: str
    """Message identifier (UUID)"""

    created_at: datetime
    """When the message was created"""

    delivery_status: Literal["pending", "queued", "sent", "delivered", "received", "read", "failed"]
    """Current delivery status of a message"""

    is_read: bool
    """DEPRECATED: Use `delivery_status == "read"` instead.

    Whether the message has been read.
    """

    parts: List[Part]
    """Message parts in order (text, media, and link)"""

    sent_at: Optional[datetime] = None
    """When the message was actually sent (null if still queued)"""

    delivered_at: Optional[datetime] = None
    """When the message was delivered"""

    effect: Optional[MessageEffect] = None
    """iMessage effect applied to a message (screen or bubble effect)"""

    from_handle: Optional[ChatHandle] = None
    """The sender of this message as a full handle object"""

    preferred_service: Optional[ServiceType] = None
    """Messaging service type"""

    reply_to: Optional[ReplyTo] = None
    """Indicates this message is a threaded reply to another message"""

    service: Optional[ServiceType] = None
    """Messaging service type"""
