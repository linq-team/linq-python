# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkPartParam"]


class LinkPartParam(TypedDict, total=False):
    type: Required[Literal["link"]]
    """Indicates this is a rich link preview part"""

    value: Required[str]
    """URL to send with a rich link preview.

    The recipient will see an inline card with the page's title, description, and
    preview image (when available).

    A `link` part must be the **only** part in the message. To send a URL as plain
    text (no preview card), use a `text` part instead.
    """
