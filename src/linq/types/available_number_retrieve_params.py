# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AvailableNumberRetrieveParams"]


class AvailableNumberRetrieveParams(TypedDict, total=False):
    exclude_from: SequenceNotStr[str]
    """Lines (E.164) to leave out of this selection.

    Applies to the returned `phone_number`, to the sticky choice when `to` is given,
    and to the vCard's backup numbers. Repeat the parameter for multiple lines; use
    `%2B` for the leading `+`.

    Numbers that are not your lines are ignored. Every entry must be E.164 — a value
    like `4155551234` is rejected rather than silently skipped. Excluding every one
    of your available lines returns 400.
    """

    to: SequenceNotStr[str]
    """Recipient handles (E.164 or email) the message is destined for.

    When provided, an existing chat with these recipients makes the choice sticky.
    Repeat the parameter for multiple recipients.
    """
