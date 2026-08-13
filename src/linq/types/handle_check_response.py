# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HandleCheckResponse"]


class HandleCheckResponse(BaseModel):
    address: str
    """The recipient address that was checked"""

    available: bool
    """Whether the recipient supports the checked messaging service"""

    reason: Optional[Literal["not_supported"]] = None
    """Why `available` is `false`. Only present on a negative result.

    `not_supported` is the only value returned with a `200`, and it means the check
    completed and the recipient is genuinely not reachable over this service. On
    `check_rcs`, sender-side faults do not return `200` — they return `503` with a
    specific error code. `check_imessage` does not use this mapping.
    """

    selected_service: Optional[str] = None
    """
    The service that would actually carry a message to this address right now, which
    is not always the service you checked — a recipient without RCS resolves to
    `SMS`. Absent when the check could not determine one.
    """
