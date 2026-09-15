# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["InlineStickerParam"]


class InlineStickerParam(TypedDict, total=False):
    """
    A sticker image placed inside the text of a part, replacing the characters in `range`.
    Provide exactly one of `url` or `attachment_id`.
    """

    range: Required[Iterable[int]]
    """
    Character range `[start, end)` in the `value` string that the sticker replaces.
    `start` is inclusive, `end` is exclusive. Those characters are hidden on
    iMessage and sent as written on SMS and RCS. _Characters are measured as UTF-16
    code units. Most characters count as 1; some emoji count as 2._
    """

    attachment_id: str
    """Reference to a sticker image pre-uploaded via `POST /v3/attachments`.

    Exactly one of `url` or `attachment_id` is required.
    """

    url: str
    """
    Linq attachment URL of the sticker image — the `download_url` returned by
    `POST /v3/attachments`.

    The image must already be stored with us. To use an image from elsewhere, upload
    it with `POST /v3/attachments` first and pass `attachment_id`.

    Exactly one of `url` or `attachment_id` is required.
    """
