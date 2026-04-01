# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ParticipantRemoveParams"]


class ParticipantRemoveParams(TypedDict, total=False):
    handle: Required[str]
    """Phone number (E.164 format) or email address of the participant to remove"""
