# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChatUpdateParams"]


class ChatUpdateParams(TypedDict, total=False):
    display_name: str
    """New display name for the chat (group chats only)"""

    group_chat_icon: str
    """URL of an image to set as the group chat icon (group chats only)"""
