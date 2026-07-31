# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExperienceListResponse", "Experience", "ExperienceAction", "ExperienceActionFields"]


class ExperienceActionFields(BaseModel):
    max: Optional[int] = None
    """Maximum length, for strings."""

    required: Optional[bool] = None

    type: Optional[Literal["string", "cents", "int", "url"]] = None


class ExperienceAction(BaseModel):
    fields: Optional[Dict[str, ExperienceActionFields]] = None
    """Fields you may send in `params`, keyed by the exact name to use."""

    name: Optional[str] = None

    summary: Optional[str] = None


class Experience(BaseModel):
    """What an experience offers you.

    Deliberately a projection: where its
    templates live and how they are built is not yours to depend on, so it
    is not here.
    """

    actions: Optional[List[ExperienceAction]] = None

    display_name: Optional[str] = None

    experience: Optional[str] = None


class ExperienceListResponse(BaseModel):
    experiences: Optional[List[Experience]] = None
