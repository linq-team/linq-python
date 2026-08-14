# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BackgroundSetParams"]


class BackgroundSetParams(TypedDict, total=False):
    type: Required[Literal["color", "dynamic", "photo"]]
    """The background family."""

    image_url: str
    """Photo: the image URL to embed in the background."""

    shades: SequenceNotStr[str]
    """
    Color with `variant: custom`: the two gradient stops as hex, top then bottom.
    Ignored for named color variants (they carry their own two colors).
    """

    style: Literal["sky", "water", "aurora", "glitter"]
    """Dynamic: the animated style."""

    variant: str
    """
    Color: a named swatch — `mango`, `ice`, `plum`, `deep_sea`, `green_apple`,
    `cherry`, `bubblegum`, `tangerine`, `magenta`, `lime`, `silver`, `carbon`,
    `stone` — or `custom` (supply `shades`). Dynamic: the variant within the `style`
    (e.g. `sunrise`).

    An unrecognized value still returns `202`, but no background is applied and no
    `chat.background_updated` webhook fires. Send one of the values above.
    """
