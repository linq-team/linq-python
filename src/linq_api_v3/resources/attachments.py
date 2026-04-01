# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import SupportedContentType, attachment_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.supported_content_type import SupportedContentType
from ..types.attachment_create_response import AttachmentCreateResponse
from ..types.attachment_retrieve_response import AttachmentRetrieveResponse

__all__ = ["AttachmentsResource", "AsyncAttachmentsResource"]


class AttachmentsResource(SyncAPIResource):
    """
    Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
    Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

    ## Sending Media via URL (up to 10MB)

    Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

    ```json
    {
      "parts": [
        { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
      ]
    }
    ```

    This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

    ## Pre-Upload (required for files over 10MB)

    Use `POST /v3/attachments` when you want to:
    - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
    - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
    - **Reduce message send latency** — the file is already stored, so sending is faster

    **How it works:**
    1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
    2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
    3. Reference the `attachment_id` in your media part when sending messages (no expiration)

    **Key difference:** When you provide an external `url`, we download and process the file on every send.
    When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

    ## Domain Allowlisting

    Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
    - `url` fields in media and voice memo message parts
    - `download_url` fields in attachment and upload response objects

    If your application enforces domain allowlists (e.g., for SSRF protection), add:

    ```
    cdn.linqapp.com
    ```

    ## Supported File Types

    - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
    - **Videos:** MP4, MOV, M4V
    - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
    - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
    - **Contact & Calendar:** VCF, ICS

    ## Audio: Attachment vs Voice Memo

    Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
    To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
    use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

    ## File Size Limits

    - **URL-based (`url` field):** 10MB maximum
    - **Pre-upload (`attachment_id`):** 100MB maximum
    """

    @cached_property
    def with_raw_response(self) -> AttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/linq-api-v3-python#accessing-raw-response-data-eg-headers
        """
        return AttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/linq-api-v3-python#with_streaming_response
        """
        return AttachmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content_type: SupportedContentType,
        filename: str,
        size_bytes: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentCreateResponse:
        """
        **This endpoint is optional.** You can send media by simply providing a URL in
        your message's media part — no pre-upload required. Use this endpoint only when
        you want to upload a file ahead of time for reuse or latency optimization.

        Returns a presigned upload URL and a permanent `attachment_id` you can reference
        in future messages.

        ## Step 1: Request an upload URL

        Call this endpoint with file metadata:

        ```json
        POST /v3/attachments
        {
          "filename": "photo.jpg",
          "content_type": "image/jpeg",
          "size_bytes": 1024000
        }
        ```

        The response includes an `upload_url` (valid for 15 minutes) and a permanent
        `attachment_id`.

        ## Step 2: Upload the file

        Make a PUT request to the `upload_url` with the raw file bytes as the request
        body. You **must** include all headers from `required_headers` exactly as
        returned — the presigned URL is signed with these values and S3 will reject the
        upload if they don't match.

        The request body is the binary file content — **not** JSON, **not** multipart
        form data. The file must equal `size_bytes` bytes (the value you declared in
        step 1).

        ```bash
        curl -X PUT "<upload_url from step 1>" \\
          -H "Content-Type: image/jpeg" \\
          -H "Content-Length: 1024000" \\
          --data-binary @photo.jpg
        ```

        ## Step 3: Send a message with the attachment

        Reference the `attachment_id` in a media part. The ID never expires — use it in
        as many messages as you want.

        ```json
        POST /v3/chats
        {
          "from": "+15559876543",
          "to": ["+15551234567"],
          "message": {
            "parts": [
              { "type": "media", "attachment_id": "<attachment_id from step 1>" }
            ]
          }
        }
        ```

        ## When to use this instead of a URL in the media part

        - Sending the same file to multiple recipients (avoids re-downloading each time)
        - Large files where you want to separate upload from message send
        - Latency-sensitive sends where the file should already be stored

        If you just need to send a file once, skip all of this and pass a `url` directly
        in the media part instead.

        **File Size Limit:** 100MB

        **Unsupported Types:** WebP, SVG, FLAC, OGG, and executable files are explicitly
        rejected.

        Args:
          content_type: Supported MIME types for file attachments and media URLs.

              **Images:** image/jpeg, image/png, image/gif, image/heic, image/heif,
              image/tiff, image/bmp

              **Videos:** video/mp4, video/quicktime, video/mpeg, video/3gpp

              **Audio:** audio/mpeg, audio/mp4, audio/x-m4a, audio/x-caf, audio/wav,
              audio/aiff, audio/aac, audio/amr

              **Documents:** application/pdf, text/plain, text/markdown, text/vcard, text/rtf,
              text/csv, text/html, text/calendar, application/msword,
              application/vnd.openxmlformats-officedocument.wordprocessingml.document,
              application/vnd.ms-excel,
              application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,
              application/vnd.ms-powerpoint,
              application/vnd.openxmlformats-officedocument.presentationml.presentation,
              application/vnd.apple.pages, application/vnd.apple.numbers,
              application/vnd.apple.keynote, application/epub+zip, application/zip

              **Unsupported:** WebP, SVG, FLAC, OGG, and executable files are explicitly
              rejected.

          filename: Name of the file to upload

          size_bytes: Size of the file in bytes (max 100MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/attachments",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "size_bytes": size_bytes,
                },
                attachment_create_params.AttachmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentCreateResponse,
        )

    def retrieve(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentRetrieveResponse:
        """
        Retrieve metadata for a specific attachment including its status, file
        information, and URLs for downloading.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return self._get(
            path_template("/v3/attachments/{attachment_id}", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentRetrieveResponse,
        )


class AsyncAttachmentsResource(AsyncAPIResource):
    """
    Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
    Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

    ## Sending Media via URL (up to 10MB)

    Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

    ```json
    {
      "parts": [
        { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
      ]
    }
    ```

    This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

    ## Pre-Upload (required for files over 10MB)

    Use `POST /v3/attachments` when you want to:
    - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
    - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
    - **Reduce message send latency** — the file is already stored, so sending is faster

    **How it works:**
    1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
    2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
    3. Reference the `attachment_id` in your media part when sending messages (no expiration)

    **Key difference:** When you provide an external `url`, we download and process the file on every send.
    When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

    ## Domain Allowlisting

    Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
    - `url` fields in media and voice memo message parts
    - `download_url` fields in attachment and upload response objects

    If your application enforces domain allowlists (e.g., for SSRF protection), add:

    ```
    cdn.linqapp.com
    ```

    ## Supported File Types

    - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
    - **Videos:** MP4, MOV, M4V
    - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
    - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
    - **Contact & Calendar:** VCF, ICS

    ## Audio: Attachment vs Voice Memo

    Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
    To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
    use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

    ## File Size Limits

    - **URL-based (`url` field):** 10MB maximum
    - **Pre-upload (`attachment_id`):** 100MB maximum
    """

    @cached_property
    def with_raw_response(self) -> AsyncAttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/linq-api-v3-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/linq-api-v3-python#with_streaming_response
        """
        return AsyncAttachmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content_type: SupportedContentType,
        filename: str,
        size_bytes: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentCreateResponse:
        """
        **This endpoint is optional.** You can send media by simply providing a URL in
        your message's media part — no pre-upload required. Use this endpoint only when
        you want to upload a file ahead of time for reuse or latency optimization.

        Returns a presigned upload URL and a permanent `attachment_id` you can reference
        in future messages.

        ## Step 1: Request an upload URL

        Call this endpoint with file metadata:

        ```json
        POST /v3/attachments
        {
          "filename": "photo.jpg",
          "content_type": "image/jpeg",
          "size_bytes": 1024000
        }
        ```

        The response includes an `upload_url` (valid for 15 minutes) and a permanent
        `attachment_id`.

        ## Step 2: Upload the file

        Make a PUT request to the `upload_url` with the raw file bytes as the request
        body. You **must** include all headers from `required_headers` exactly as
        returned — the presigned URL is signed with these values and S3 will reject the
        upload if they don't match.

        The request body is the binary file content — **not** JSON, **not** multipart
        form data. The file must equal `size_bytes` bytes (the value you declared in
        step 1).

        ```bash
        curl -X PUT "<upload_url from step 1>" \\
          -H "Content-Type: image/jpeg" \\
          -H "Content-Length: 1024000" \\
          --data-binary @photo.jpg
        ```

        ## Step 3: Send a message with the attachment

        Reference the `attachment_id` in a media part. The ID never expires — use it in
        as many messages as you want.

        ```json
        POST /v3/chats
        {
          "from": "+15559876543",
          "to": ["+15551234567"],
          "message": {
            "parts": [
              { "type": "media", "attachment_id": "<attachment_id from step 1>" }
            ]
          }
        }
        ```

        ## When to use this instead of a URL in the media part

        - Sending the same file to multiple recipients (avoids re-downloading each time)
        - Large files where you want to separate upload from message send
        - Latency-sensitive sends where the file should already be stored

        If you just need to send a file once, skip all of this and pass a `url` directly
        in the media part instead.

        **File Size Limit:** 100MB

        **Unsupported Types:** WebP, SVG, FLAC, OGG, and executable files are explicitly
        rejected.

        Args:
          content_type: Supported MIME types for file attachments and media URLs.

              **Images:** image/jpeg, image/png, image/gif, image/heic, image/heif,
              image/tiff, image/bmp

              **Videos:** video/mp4, video/quicktime, video/mpeg, video/3gpp

              **Audio:** audio/mpeg, audio/mp4, audio/x-m4a, audio/x-caf, audio/wav,
              audio/aiff, audio/aac, audio/amr

              **Documents:** application/pdf, text/plain, text/markdown, text/vcard, text/rtf,
              text/csv, text/html, text/calendar, application/msword,
              application/vnd.openxmlformats-officedocument.wordprocessingml.document,
              application/vnd.ms-excel,
              application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,
              application/vnd.ms-powerpoint,
              application/vnd.openxmlformats-officedocument.presentationml.presentation,
              application/vnd.apple.pages, application/vnd.apple.numbers,
              application/vnd.apple.keynote, application/epub+zip, application/zip

              **Unsupported:** WebP, SVG, FLAC, OGG, and executable files are explicitly
              rejected.

          filename: Name of the file to upload

          size_bytes: Size of the file in bytes (max 100MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/attachments",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "filename": filename,
                    "size_bytes": size_bytes,
                },
                attachment_create_params.AttachmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentCreateResponse,
        )

    async def retrieve(
        self,
        attachment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentRetrieveResponse:
        """
        Retrieve metadata for a specific attachment including its status, file
        information, and URLs for downloading.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return await self._get(
            path_template("/v3/attachments/{attachment_id}", attachment_id=attachment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentRetrieveResponse,
        )


class AttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.create = to_raw_response_wrapper(
            attachments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            attachments.retrieve,
        )


class AsyncAttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.create = async_to_raw_response_wrapper(
            attachments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            attachments.retrieve,
        )


class AttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.create = to_streamed_response_wrapper(
            attachments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            attachments.retrieve,
        )


class AsyncAttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.create = async_to_streamed_response_wrapper(
            attachments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            attachments.retrieve,
        )
