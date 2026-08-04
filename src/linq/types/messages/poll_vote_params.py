# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PollVoteParams"]


class PollVoteParams(TypedDict, total=False):
    operation: Required[Literal["add", "remove"]]
    """Add or remove your line's vote on the option."""

    option_id: Required[str]
    """The option to toggle a vote on."""
