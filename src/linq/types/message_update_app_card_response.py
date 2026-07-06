# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .chats.sent_message import SentMessage

__all__ = ["MessageUpdateAppCardResponse"]


class MessageUpdateAppCardResponse(BaseModel):
    """Response for sending a message to a chat"""

    chat_id: str
    """Unique identifier of the chat this message was sent to"""

    message: SentMessage
    """A message that was sent (used in CreateChat and SendMessage responses)"""
