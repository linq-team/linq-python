# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    text: Required[str]
    """New text content for the message part"""

    part_index: int
    """Index of the message part to edit. Defaults to 0."""
