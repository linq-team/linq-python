# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .reputation_report import ReputationReport

__all__ = ["ReputationAudit"]


class ReputationAudit(BaseModel):
    audit_id: str

    status: Literal["pending", "complete", "error"]
    """`pending` until the report is ready — poll until `complete` or `error`."""

    error: Optional[str] = None
    """Present only when `status` is `error`. Short, generic reason safe to display."""

    generated_at: Optional[datetime] = None
    """When the report was generated; signals reflect the line at this moment."""

    phone: Optional[str] = None
    """The line audited, E.164."""

    report: Optional[ReputationReport] = None
    """Present only when `status` is `complete`."""
