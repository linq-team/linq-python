# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BackgroundSetParams"]


class BackgroundSetParams(TypedDict, total=False):
    type: Required[Literal["color", "dynamic", "photo"]]
    """The background family."""

    image_url: str
    """Photo: the image URL to embed in the background.

    Must be an absolute `https` URL pointing at an image (`.jpg`, `.png`, `.heic`,
    `.webp`), and the image is fetched and re-hosted on our CDN before the request
    is accepted — the same way `group_chat_icon` works. A URL we cannot fetch, or
    one that isn't an image, is rejected with a `400` (`5007`/`5006`) rather than
    failing later on the device.

    Example: `https://cdn.linqapp.com/u/bg.jpg`.
    """

    shades: SequenceNotStr[str]
    """
    Color with `variant: custom`: the two gradient stops as hex, top then bottom —
    e.g. `["#F2C4E1", "#F5A623"]`. Ignored for named color variants (they carry
    their own two colors).
    """

    style: Literal["sky", "water", "aurora"]
    """Dynamic: the animated style — `sky`, `water`, or `aurora`."""

    variant: str
    """
    Color: a named swatch — `mango`, `ice`, `plum`, `deep_sea`, `green_apple`,
    `cherry`, `bubblegum`, `tangerine`, `magenta`, `lime`, `silver`, `carbon`,
    `stone` — or `custom` (supply `shades`). Omitting `variant` is equivalent to
    `custom`, so it still requires `shades`.

    Dynamic: required — the variant within the `style`. `sky`: `dusk`, `haze`,
    `sunset`, `clear`, `sunrise`, `dawn`. `water`: `light`, `dark`. `aurora`:
    `green`, `purple`, `pink`.

    An unrecognized value is rejected with `400`.
    """
