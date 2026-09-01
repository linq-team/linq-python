# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AttachmentCreateResponse"]


class AttachmentCreateResponse(BaseModel):
    attachment_id: str
    """Unique identifier for the attachment"""

    download_url: str
    """Stable CDN URL for the file.

    Use the `attachment_id` to reference this file in media parts when sending
    messages. Files on the ephemeral attachments tier — and this URL — are removed
    within roughly 24–48 hours of upload, independently of any message retention
    window.
    """

    expires_at: datetime
    """When the upload URL expires (15 minutes from now)"""

    http_method: Literal["PUT"]
    """HTTP method to use for upload (always PUT)"""

    required_headers: Dict[str, str]
    """HTTP headers that must be set on the upload request.

    The presigned URL is signed with these exact values — S3 will reject the upload
    if they don't match.
    """

    upload_url: str
    """Presigned URL for uploading the file.

    PUT the raw binary file content to this URL with the `required_headers`. Do not
    JSON-encode or multipart-wrap the body. Expires after 15 minutes. Treat the URL
    as opaque — the hostname depends on partner configuration and is the same across
    sandbox and production.
    """
