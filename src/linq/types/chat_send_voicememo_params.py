# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChatSendVoicememoParams"]


class ChatSendVoicememoParams(TypedDict, total=False):
    attachment_id: str
    """
    Reference to a voice memo file pre-uploaded via `POST /v3/attachments`. The file
    is already stored, so sends using this ID skip the download step.

    Either `voice_memo_url` or `attachment_id` must be provided, but not both.
    """

    voice_memo_url: str
    """URL of the voice memo audio file. Must be a publicly accessible HTTPS URL.

    Either `voice_memo_url` or `attachment_id` must be provided, but not both.
    """
