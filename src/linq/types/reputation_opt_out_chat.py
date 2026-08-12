# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReputationOptOutChat"]


class ReputationOptOutChat(BaseModel):
    chat_id: Optional[str] = None

    messages_after_stop: Optional[int] = None
    """Outbound messages sent after the recipient asked to stop."""
