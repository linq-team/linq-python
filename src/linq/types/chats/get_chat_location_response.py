# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GetChatLocationResponse", "Data", "DataFeature", "DataFeatureGeometry", "DataFeatureProperties"]


class DataFeatureGeometry(BaseModel):
    coordinates: List[float]
    """[longitude, latitude] or [longitude, latitude, altitude]"""

    type: Literal["Point"]


class DataFeatureProperties(BaseModel):
    handle: str
    """Phone number or email of the person sharing their location"""

    address: Optional[str] = None
    """Full street address"""

    locality: Optional[str] = None
    """City or locality name"""

    updated_at: Optional[datetime] = None
    """When the location was last updated"""


class DataFeature(BaseModel):
    geometry: DataFeatureGeometry

    properties: DataFeatureProperties

    type: Literal["Feature"]


class Data(BaseModel):
    features: List[DataFeature]

    type: Literal["FeatureCollection"]


class GetChatLocationResponse(BaseModel):
    data: Data

    success: bool
