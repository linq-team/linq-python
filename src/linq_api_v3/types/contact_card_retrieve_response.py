# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ContactCardRetrieveResponse", "ContactCard"]


class ContactCard(BaseModel):
    first_name: str

    is_active: bool

    phone_number: str

    image_url: Optional[str] = None

    last_name: Optional[str] = None


class ContactCardRetrieveResponse(BaseModel):
    contact_cards: List[ContactCard]
