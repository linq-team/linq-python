# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .chats.sent_message import SentMessage
from .shared.chat_handle import ChatHandle
from .shared.service_type import ServiceType

__all__ = ["MessageCreateResponse", "FromSelection"]


class FromSelection(BaseModel):
    """Why this line/chat was chosen."""

    reason: Literal["reused_active_chat", "new_best_number", "failover_flagged"]
    """
    - `reused_active_chat` — reused an existing chat on its healthy line
    - `new_best_number` — created a new chat on the best available line
    - `failover_flagged` — no existing chat for these recipients was on a line that
      could send; created a new chat on a fresh line
    """

    reused_existing_chat: bool
    """True only when an existing chat was reused."""


class MessageCreateResponse(BaseModel):
    """Result of an auto-from send.

    Self-describing: which line was used, which
    chat the message landed in, whether a new chat was created, and the
    resulting message id(s).
    """

    chat_id: str
    """The resolved chat (reused or newly created) the message landed in."""

    created_new_chat: bool
    """True when a new chat was created (new or failover), false on reuse."""

    from_: str = FieldInfo(alias="from")
    """The line (E.164) the message was actually sent from."""

    from_selection: FromSelection
    """Why this line/chat was chosen."""

    handles: List[ChatHandle]
    """Participants of the resolved chat."""

    is_group: bool
    """Whether the resolved chat is a group chat."""

    message: SentMessage
    """A message that was sent (used in CreateChat and SendMessage responses)"""

    service: ServiceType
    """Messaging service type"""

    previous_chat_id: Optional[str] = None
    """
    Set ONLY on `failover_flagged`: the abandoned flagged chat that was NOT sent
    into. Null otherwise.
    """
