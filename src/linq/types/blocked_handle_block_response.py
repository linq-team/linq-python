# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .blocked_handle_entry import BlockedHandleEntry

__all__ = ["BlockedHandleBlockResponse"]


class BlockedHandleBlockResponse(BaseModel):
    blocked_handle: BlockedHandleEntry
