# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReputationActionItem"]


class ReputationActionItem(BaseModel):
    detail: Optional[str] = None

    expected_impact: Optional[Literal["high", "medium", "low"]] = None

    priority: Optional[int] = None
    """1 = do first"""

    title: Optional[str] = None
