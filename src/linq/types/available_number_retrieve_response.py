# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AvailableNumberRetrieveResponse"]


class AvailableNumberRetrieveResponse(BaseModel):
    """The line smart number assignment selected, plus a shareable vCard."""

    phone_number: str
    """The selected sending line in E.164 format."""

    vcf_url: str
    """Time-limited link to a vCard (`.vcf`) for the selected line.

    The card carries the line's contact details with the selected number as the
    primary `TEL` and the partner's other healthy lines as backups. The link
    expires; re-call this endpoint to mint a fresh one.
    """
