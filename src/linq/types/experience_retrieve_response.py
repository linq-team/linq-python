# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExperienceRetrieveResponse", "Action", "ActionFields"]


class ActionFields(BaseModel):
    max: Optional[int] = None
    """Maximum length, for strings."""

    required: Optional[bool] = None

    type: Optional[Literal["string", "cents", "int", "url"]] = None


class Action(BaseModel):
    fields: Optional[Dict[str, ActionFields]] = None
    """Fields you may send in `params`, keyed by the exact name to use."""

    name: Optional[str] = None

    summary: Optional[str] = None


class ExperienceRetrieveResponse(BaseModel):
    """What an experience offers you.

    Deliberately a projection: where its
    templates live and how they are built is not yours to depend on, so it
    is not here.
    """

    actions: Optional[List[Action]] = None

    display_name: Optional[str] = None

    experience: Optional[str] = None
