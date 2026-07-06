# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AvailableNumberRetrieveParams"]


class AvailableNumberRetrieveParams(TypedDict, total=False):
    to: SequenceNotStr[str]
    """Recipient handles (E.164 or email) the message is destined for.

    When provided, an existing chat with these recipients makes the choice sticky.
    Repeat the parameter for multiple recipients.
    """
