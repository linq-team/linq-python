# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .reply_to_param import ReplyToParam
from .link_part_param import LinkPartParam
from .text_part_param import TextPartParam
from .media_part_param import MediaPartParam
from .shared.service_type import ServiceType
from .message_effect_param import MessageEffectParam

__all__ = [
    "MessageContentParam",
    "Experience",
    "Part",
    "PartIMessageAppPart",
    "PartIMessageAppPartApp",
    "PartIMessageAppPartLayout",
    "PartAppClipPart",
]


class Experience(TypedDict, total=False):
    """
    Invokes an action on an experience — a third party that renders inside
    Linq's iMessage app. Linq resolves the recipient's connection, mints any
    session the action needs, composes the card and sends it; none of that
    is visible to you.

    Call `GET /v3/experiences/{experience}` for the actions you may invoke
    and the fields each accepts.
    """

    action: Required[str]
    """Which of its actions, e.g. `attach_card`."""

    name: Required[str]
    """The experience to invoke, e.g. `agentcard` or `agentpay`."""

    params: Dict[str, object]
    """Values for the fields this action exposes.

    Keys are exactly the field names listed for the action — no mapping, no nesting.

    Display copy only, except a `url`-type field — that value sets the destination,
    and must be an absolute `https` URL.

    Some fields are read rather than sent: `agentpay`'s `request_payment` takes only
    a `checkout_url` and resolves the amount and reason from that payment request
    itself, so the card cannot state a figure the checkout will not charge.
    """


class PartIMessageAppPartApp(TypedDict, total=False):
    """Identifies the iMessage app (Messages app extension) that backs the card."""

    bundle_id: Required[str]
    """Bundle identifier of the Messages app extension. Must not contain `:`."""

    name: Required[str]
    """Display name of the app, shown by Messages' fallback UI."""

    team_id: Required[str]
    """The app's 10-character uppercase alphanumeric team identifier."""

    app_store_id: int
    """The owning app's App Store id (optional).

    When set, recipients without the iMessage app installed see a "Get the app"
    affordance.
    """


class PartIMessageAppPartLayout(TypedDict, total=False):
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

    caption: str
    """Primary label, top-left and bold."""

    image_subtitle: str
    """Text shown below `image_title`, overlaid on the card image.

    Requires `image_url`.
    """

    image_title: str
    """Bold text overlaid on the card image.

    Requires `image_url` (rejected without it).
    """

    image_url: str
    """
    URL of an image (JPEG, PNG, HEIF, or WebP) to display as the card's preview
    image; an unreachable or non-image URL returns a validation error. Renders for
    all recipients regardless of whether they have the app. Note - requires a
    trusted chat w/ inbound activity. In responses, this is the re-hosted
    `cdn.linqapp.com` copy of the image you supplied, not your original URL.
    """

    subcaption: str
    """Secondary label, below `caption` on the left."""

    trailing_caption: str
    """Label shown top-right."""

    trailing_subcaption: str
    """Label shown below `trailing_caption`, on the right."""


class PartIMessageAppPart(TypedDict, total=False):
    """An iMessage app card, backed by a Messages app extension.

    iMessage only —
    an `imessage_app` part must be the **only** part in the message and is never delivered over
    SMS/RCS. See the IMessageAppServiceUnsupported (2018) and RecipientUnsupportedMessageType
    (4005) error codes.
    """

    app: Required[PartIMessageAppPartApp]
    """Identifies the iMessage app (Messages app extension) that backs the card."""

    layout: Required[PartIMessageAppPartLayout]
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

    type: Required[Literal["imessage_app"]]
    """Indicates this is an iMessage app card part."""

    fallback_text: str
    """Text shown on surfaces that cannot render the card (notifications, lock screen).

    Defaults to the caption when omitted.
    """

    interactive: bool
    """
    Whether the card renders as your app's interactive balloon for recipients who
    have your iMessage app installed. `true` (default) lets your installed extension
    draw its live, interactive view for those recipients; everyone else sees the
    static card built from `layout`. `false` always shows the static `layout` card,
    even to recipients who have the app installed. Recipients without your app
    always see the static card regardless of this flag.
    """

    url: str
    """URL the recipient's app opens when they tap the card.

    Either an absolute `https://` URL (capped at 2048 characters) or a `data:` URL
    carrying inline app state, e.g. a game's encoded state (capped at 16384
    characters).
    """


class PartAppClipPart(TypedDict, total=False):
    """
    Sends a **registered App Clip** — not only Linq's Apple Pay checkout, but any
    partner's own App Clip. `caption` is optional.

    An `app_clip` part must be the **only** part in the message.

    **iMessage only**, and it never downgrades. A `service_preference` of
    `sms` or `rcs` is rejected (`AppClipServiceUnsupported`, 2028). A
    recipient who can't receive it fails the send rather than being sent a
    plain link in its place.
    """

    type: Required[Literal["app_clip"]]
    """Indicates this is an App Clip card"""

    value: Required[str]
    """An https link whose page is a registered App Clip — Linq's checkout link (e.g.

    the `checkout_url` from `POST /v3/payment_requests`) or a partner's own App Clip
    URL. A URL that doesn't resolve to a sendable App Clip page is rejected.
    """

    caption: str
    """Optional caption for the card's **Open** button row.

    Omit it and the card uses the App Clip's own default (`Tap open`). Set it to
    override that with your own short call to action.
    """


Part: TypeAlias = Union[TextPartParam, MediaPartParam, LinkPartParam, PartIMessageAppPart, PartAppClipPart]


class MessageContentParam(TypedDict, total=False):
    """Message content container.

    Groups all message-related fields together,
    separating the "what" (message content) from the "where" (routing fields like from/to).

    A message carries EITHER `parts` — text and attachments, which compose
    into one bubble — or a single `experience` invocation, which renders an
    experience inside Linq's iMessage app. Never both: an app card is the whole message
    (Apple's `MSMessage` cannot coexist with text), so copy and a card are
    two sends, not one.
    """

    effect: MessageEffectParam
    """iMessage effect to apply to this message (screen or bubble effect)"""

    experience: Experience
    """
    Invokes an action on an experience — a third party that renders inside Linq's
    iMessage app. Linq resolves the recipient's connection, mints any session the
    action needs, composes the card and sends it; none of that is visible to you.

    Call `GET /v3/experiences/{experience}` for the actions you may invoke and the
    fields each accepts.
    """

    idempotency_key: str
    """
    Optional idempotency key for this message. Use this to prevent duplicate sends
    of the same message. Reusing a key whose message was deleted — or was an
    ephemeral message that has since expired — returns 404; the message is never
    resent.
    """

    parts: Iterable[Part]
    """Array of message parts.

    Each part can be text, media, or link. Parts are displayed in order. Text and
    media can be mixed freely, but a `link` part must be the only part in the
    message.

    **Rich Link Previews:**

    - Use a `link` part to send a URL with a rich preview card
    - A `link` part must be the **only** part in the message
    - To send a URL as plain text (no preview), use a `text` part instead

    **App Clip Payment Cards:**

    - Use an `app_clip` part to send a Linq checkout link as an Apple Pay App Clip
      card (the payment preview with the Open button)
    - An `app_clip` part must be the **only** part in the message
    - iMessage-only: unlike `link`, it never downgrades to SMS/RCS — the send fails
      instead of delivering a bare URL

    **Supported Media:**

    - Images: .jpg, .jpeg, .png, .gif, .heic, .heif, .tif, .tiff, .bmp
    - Videos: .mp4, .mov, .m4v, .mpeg, .mpg, .3gp
    - Audio: .m4a, .mp3, .aac, .caf, .wav, .aiff, .amr
    - Documents: .pdf, .txt, .rtf, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx,
      .pages, .numbers, .key, .epub, .zip, .html, .htm
    - Contact & Calendar: .vcf, .ics

    **Audio:**

    - Audio files (.m4a, .mp3, .aac, .caf, .wav, .aiff, .amr) are fully supported as
      media parts
    - To send audio as an **iMessage voice memo bubble** (inline playback UI), use
      the dedicated `/v3/chats/{chatId}/voicememo` endpoint instead

    **Validation Rules:**

    - A `link` part must be the **only** part in the message. It cannot be combined
      with text or media parts.
    - An `app_clip` part must be the **only** part in the message. Its `value` must
      be a Linq checkout link (e.g. from `POST /v3/payment_requests`); any other URL
      is rejected.
    - Consecutive text parts are not allowed. Text parts must be separated by media
      parts. For example, [text, text] is invalid, but [text, media, text] is valid.
    - Maximum of **100 parts** total.
    - Media parts using a public `url` (downloaded by the server on send) are capped
      at **40**. Parts using `attachment_id` or presigned URLs are exempt from this
      sub-limit. For bulk media sends exceeding 40 files, pre-upload via
      `POST /v3/attachments` and reference by `attachment_id` or `download_url`.
    """

    preferred_service: ServiceType
    """Messaging service type"""

    reply_to: ReplyToParam
    """Reply to another message to create a threaded conversation"""
