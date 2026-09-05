# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MediaPartParam"]


class MediaPartParam(TypedDict, total=False):
    type: Required[Literal["media"]]
    """Indicates this is a media attachment part"""

    attachment_id: str
    """
    Reference to a file pre-uploaded via `POST /v3/attachments` (optional). The file
    is already stored, so sends using this ID skip the download step — useful when
    sending the same file to many recipients.

    Either `url` or `attachment_id` must be provided, but not both.
    """

    sticker: bool
    """Send this image as a **sticker** rather than a photo.

    The recipient can peel it off and place it on any message in the conversation,
    and it renders without a bubble.

    An opaque photo is cut out automatically — the subject is lifted from its
    background, the same way "Add Sticker" does on iOS. An image that already has
    transparency is sent as-is. If no subject can be found, the image sends as an
    ordinary photo.

    **iMessage only.** On SMS/RCS the flag is ignored and the image sends as a
    photo.

    Stickers can be combined with a `text` part in the same message; the text
    arrives as its own bubble. To place a sticker _onto_ an existing message
    instead, use `POST /v3/messages/{messageId}/reactions` with `type: "sticker"`.
    """

    url: str
    """Any publicly accessible HTTPS URL to the media file.

    The server downloads and sends the file automatically — no pre-upload step
    required.

    **Size limit:** 10MB maximum for URL-based downloads. For larger files (up to
    100MB), use the pre-upload flow: `POST /v3/attachments` to get a presigned URL,
    upload directly, then reference by `attachment_id`.

    **Requirements:**

    - URL must use HTTPS
    - File content must be a supported format (the server validates the actual file
      content)

    **Supported formats:**

    - Images: .jpg, .jpeg, .png, .gif, .heic, .heif, .tif, .tiff, .bmp
    - Videos: .mp4, .mov, .m4v, .mpeg, .mpg, .3gp
    - Audio: .m4a, .mp3, .aac, .caf, .wav, .aiff, .amr
    - Documents: .pdf, .txt, .rtf, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx,
      .pages, .numbers, .key, .epub, .zip, .html, .htm
    - Contact & Calendar: .vcf, .ics

    **Tip:** Audio sent here appears as a regular file attachment. To send audio as
    an iMessage voice memo bubble (with inline playback), use
    `/v3/chats/{chatId}/voicememo`. For repeated sends of the same file, use
    `attachment_id` to avoid redundant downloads.

    Either `url` or `attachment_id` must be provided, but not both.
    """
