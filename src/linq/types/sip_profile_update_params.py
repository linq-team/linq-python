# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SipProfileUpdateParams"]


class SipProfileUpdateParams(TypedDict, total=False):
    backup_uri: str
    """Set to "" to clear the backup URI."""

    name: str

    primary_uri: str
