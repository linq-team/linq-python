# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PollCreateParams", "Poll", "PollOption"]


class PollCreateParams(TypedDict, total=False):
    poll: Required[Poll]
    """Poll content to create.

    A poll needs at least two options. Options are add-only and immutable — there is
    no title/question (send that as a normal text message).
    """


class PollOption(TypedDict, total=False):
    text: Required[str]


class Poll(TypedDict, total=False):
    """Poll content to create.

    A poll needs at least two options. Options are add-only and
    immutable — there is no title/question (send that as a normal text message).
    """

    options: Required[Iterable[PollOption]]

    idempotency_key: str
    """Optional key to deduplicate the poll creation."""
