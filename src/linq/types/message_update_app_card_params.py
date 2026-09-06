# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["MessageUpdateAppCardParams", "Layout", "App", "Experience"]


class MessageUpdateAppCardParams(TypedDict, total=False):
    layout: Required[Layout]
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

    app: App
    """Identifies the iMessage app (Messages app extension) that backs the card."""

    experience: Experience
    """
    Invokes an action on an experience — a third party that renders inside Linq's
    iMessage app. Linq resolves the recipient's connection, mints any session the
    action needs, composes the card and sends it; none of that is visible to you.

    Call `GET /v3/experiences/{experience}` for the actions you may invoke and the
    fields each accepts.
    """

    fallback_text: str
    """Text shown on surfaces that cannot render the card (notifications, lock screen).

    Defaults to the caption when omitted.
    """

    interactive: bool
    """
    Whether the updated card renders as your app's interactive balloon for
    recipients who have your iMessage app installed. `true` (default) lets your
    installed extension draw its live view; `false` always shows the static `layout`
    card. Recipients without your app always see the static card regardless of this
    flag.

    Defaults to `true` when omitted — it is **not** inherited from the original
    card. To keep a card static across updates, re-send `interactive: false` on each
    update.
    """

    url: str
    """URL the recipient's app opens when they tap the updated card.

    Mutually exclusive with `experience` and `raw_payload_data`.
    """


class Layout(TypedDict, total=False):
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


class App(TypedDict, total=False):
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
