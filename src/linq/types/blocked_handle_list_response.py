# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .blocked_handle_entry import BlockedHandleEntry

__all__ = ["BlockedHandleListResponse"]


class BlockedHandleListResponse(BaseModel):
    blocked_handles: List[BlockedHandleEntry]
    """All handles blocked by the partner, newest first"""
