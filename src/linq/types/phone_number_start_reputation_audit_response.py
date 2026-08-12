# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberStartReputationAuditResponse"]


class PhoneNumberStartReputationAuditResponse(BaseModel):
    audit_id: str
    """Identifier for this audit.

    Poll `GET /v3/phone_numbers/{phoneNumber}/reputation_audit/{auditId}` until
    `status` is `complete` or `error`.
    """

    status: Literal["pending", "complete", "error"]
    """A newly started audit is `pending`."""
