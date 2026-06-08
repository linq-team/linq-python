# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LinqApiv3Error
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        chats,
        messages,
        capability,
        attachments,
        contact_card,
        phonenumbers,
        phone_numbers,
        webhook_events,
        webhook_subscriptions,
    )
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.capability import CapabilityResource, AsyncCapabilityResource
    from .resources.attachments import AttachmentsResource, AsyncAttachmentsResource
    from .resources.chats.chats import ChatsResource, AsyncChatsResource
    from .resources.contact_card import ContactCardResource, AsyncContactCardResource
    from .resources.phonenumbers import PhonenumbersResource, AsyncPhonenumbersResource
    from .resources.phone_numbers import PhoneNumbersResource, AsyncPhoneNumbersResource
    from .resources.webhook_events import WebhookEventsResource, AsyncWebhookEventsResource
    from .resources.webhook_subscriptions import WebhookSubscriptionsResource, AsyncWebhookSubscriptionsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LinqAPIV3",
    "AsyncLinqAPIV3",
    "Client",
    "AsyncClient",
]


class LinqAPIV3(SyncAPIClient):
    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LinqAPIV3 client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `LINQ_API_V3_API_KEY`
        - `webhook_secret` from `LINQ_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("LINQ_API_V3_API_KEY")
        if api_key is None:
            raise LinqApiv3Error(
                "The api_key client option must be set either by passing api_key to the client or by setting the LINQ_API_V3_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("LINQ_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("LINQ_API_V3_BASE_URL")
        if base_url is None:
            base_url = f"https://api.linqapp.com/api/partner"

        custom_headers_env = os.environ.get("LINQ_API_V3_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def chats(self) -> ChatsResource:
        from .resources.chats import ChatsResource

        return ChatsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        """Messages are individual communications within a chat thread.

        Messages can include text, media attachments, rich link previews, special effects
        (like confetti or fireworks), and reactions. All messages are associated with a
        specific chat and sent from a phone number you own.

        Messages support delivery status tracking, read receipts, and editing capabilities.

        ## Rich Link Previews

        Send a URL as a `link` part to deliver it with a rich preview card showing the
        page's title, description, and image (when available). A `link` part must be the
        **only** part in the message — it cannot be combined with text or media parts.
        To send a URL without a preview card, include it in a `text` part instead.

        **Limitations:**
        - A `link` part cannot be combined with other parts in the same message.
        - Maximum URL length: 2,048 characters.
        """
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def attachments(self) -> AttachmentsResource:
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

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AttachmentsResource

        return AttachmentsResource(self)

    @cached_property
    def phonenumbers(self) -> PhonenumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phonenumbers import PhonenumbersResource

        return PhonenumbersResource(self)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phone_numbers import PhoneNumbersResource

        return PhoneNumbersResource(self)

    @cached_property
    def webhook_events(self) -> WebhookEventsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import WebhookEventsResource

        return WebhookEventsResource(self)

    @cached_property
    def webhook_subscriptions(self) -> WebhookSubscriptionsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import WebhookSubscriptionsResource

        return WebhookSubscriptionsResource(self)

    @cached_property
    def capability(self) -> CapabilityResource:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import CapabilityResource

        return CapabilityResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def contact_card(self) -> ContactCardResource:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import ContactCardResource

        return ContactCardResource(self)

    @cached_property
    def with_raw_response(self) -> LinqAPIV3WithRawResponse:
        return LinqAPIV3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinqAPIV3WithStreamedResponse:
        return LinqAPIV3WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLinqAPIV3(AsyncAPIClient):
    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLinqAPIV3 client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `LINQ_API_V3_API_KEY`
        - `webhook_secret` from `LINQ_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("LINQ_API_V3_API_KEY")
        if api_key is None:
            raise LinqApiv3Error(
                "The api_key client option must be set either by passing api_key to the client or by setting the LINQ_API_V3_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("LINQ_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("LINQ_API_V3_BASE_URL")
        if base_url is None:
            base_url = f"https://api.linqapp.com/api/partner"

        custom_headers_env = os.environ.get("LINQ_API_V3_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def chats(self) -> AsyncChatsResource:
        from .resources.chats import AsyncChatsResource

        return AsyncChatsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Messages are individual communications within a chat thread.

        Messages can include text, media attachments, rich link previews, special effects
        (like confetti or fireworks), and reactions. All messages are associated with a
        specific chat and sent from a phone number you own.

        Messages support delivery status tracking, read receipts, and editing capabilities.

        ## Rich Link Previews

        Send a URL as a `link` part to deliver it with a rich preview card showing the
        page's title, description, and image (when available). A `link` part must be the
        **only** part in the message — it cannot be combined with text or media parts.
        To send a URL without a preview card, include it in a `text` part instead.

        **Limitations:**
        - A `link` part cannot be combined with other parts in the same message.
        - Maximum URL length: 2,048 characters.
        """
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def attachments(self) -> AsyncAttachmentsResource:
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

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AsyncAttachmentsResource

        return AsyncAttachmentsResource(self)

    @cached_property
    def phonenumbers(self) -> AsyncPhonenumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phonenumbers import AsyncPhonenumbersResource

        return AsyncPhonenumbersResource(self)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResource

        return AsyncPhoneNumbersResource(self)

    @cached_property
    def webhook_events(self) -> AsyncWebhookEventsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import AsyncWebhookEventsResource

        return AsyncWebhookEventsResource(self)

    @cached_property
    def webhook_subscriptions(self) -> AsyncWebhookSubscriptionsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import AsyncWebhookSubscriptionsResource

        return AsyncWebhookSubscriptionsResource(self)

    @cached_property
    def capability(self) -> AsyncCapabilityResource:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import AsyncCapabilityResource

        return AsyncCapabilityResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def contact_card(self) -> AsyncContactCardResource:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import AsyncContactCardResource

        return AsyncContactCardResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLinqAPIV3WithRawResponse:
        return AsyncLinqAPIV3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinqAPIV3WithStreamedResponse:
        return AsyncLinqAPIV3WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LinqAPIV3WithRawResponse:
    _client: LinqAPIV3

    def __init__(self, client: LinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.ChatsResourceWithRawResponse:
        from .resources.chats import ChatsResourceWithRawResponse

        return ChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """Messages are individual communications within a chat thread.

        Messages can include text, media attachments, rich link previews, special effects
        (like confetti or fireworks), and reactions. All messages are associated with a
        specific chat and sent from a phone number you own.

        Messages support delivery status tracking, read receipts, and editing capabilities.

        ## Rich Link Previews

        Send a URL as a `link` part to deliver it with a rich preview card showing the
        page's title, description, and image (when available). A `link` part must be the
        **only** part in the message — it cannot be combined with text or media parts.
        To send a URL without a preview card, include it in a `text` part instead.

        **Limitations:**
        - A `link` part cannot be combined with other parts in the same message.
        - Maximum URL length: 2,048 characters.
        """
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithRawResponse:
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

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AttachmentsResourceWithRawResponse

        return AttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.PhonenumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phonenumbers import PhonenumbersResourceWithRawResponse

        return PhonenumbersResourceWithRawResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phone_numbers import PhoneNumbersResourceWithRawResponse

        return PhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def webhook_events(self) -> webhook_events.WebhookEventsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import WebhookEventsResourceWithRawResponse

        return WebhookEventsResourceWithRawResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.WebhookSubscriptionsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import WebhookSubscriptionsResourceWithRawResponse

        return WebhookSubscriptionsResourceWithRawResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.CapabilityResourceWithRawResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import CapabilityResourceWithRawResponse

        return CapabilityResourceWithRawResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.ContactCardResourceWithRawResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import ContactCardResourceWithRawResponse

        return ContactCardResourceWithRawResponse(self._client.contact_card)


class AsyncLinqAPIV3WithRawResponse:
    _client: AsyncLinqAPIV3

    def __init__(self, client: AsyncLinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithRawResponse:
        from .resources.chats import AsyncChatsResourceWithRawResponse

        return AsyncChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """Messages are individual communications within a chat thread.

        Messages can include text, media attachments, rich link previews, special effects
        (like confetti or fireworks), and reactions. All messages are associated with a
        specific chat and sent from a phone number you own.

        Messages support delivery status tracking, read receipts, and editing capabilities.

        ## Rich Link Previews

        Send a URL as a `link` part to deliver it with a rich preview card showing the
        page's title, description, and image (when available). A `link` part must be the
        **only** part in the message — it cannot be combined with text or media parts.
        To send a URL without a preview card, include it in a `text` part instead.

        **Limitations:**
        - A `link` part cannot be combined with other parts in the same message.
        - Maximum URL length: 2,048 characters.
        """
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithRawResponse:
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

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithRawResponse

        return AsyncAttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.AsyncPhonenumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phonenumbers import AsyncPhonenumbersResourceWithRawResponse

        return AsyncPhonenumbersResourceWithRawResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithRawResponse

        return AsyncPhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def webhook_events(self) -> webhook_events.AsyncWebhookEventsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import AsyncWebhookEventsResourceWithRawResponse

        return AsyncWebhookEventsResourceWithRawResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.AsyncWebhookSubscriptionsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import AsyncWebhookSubscriptionsResourceWithRawResponse

        return AsyncWebhookSubscriptionsResourceWithRawResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.AsyncCapabilityResourceWithRawResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import AsyncCapabilityResourceWithRawResponse

        return AsyncCapabilityResourceWithRawResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.AsyncContactCardResourceWithRawResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import AsyncContactCardResourceWithRawResponse

        return AsyncContactCardResourceWithRawResponse(self._client.contact_card)


class LinqAPIV3WithStreamedResponse:
    _client: LinqAPIV3

    def __init__(self, client: LinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.ChatsResourceWithStreamingResponse:
        from .resources.chats import ChatsResourceWithStreamingResponse

        return ChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """Messages are individual communications within a chat thread.

        Messages can include text, media attachments, rich link previews, special effects
        (like confetti or fireworks), and reactions. All messages are associated with a
        specific chat and sent from a phone number you own.

        Messages support delivery status tracking, read receipts, and editing capabilities.

        ## Rich Link Previews

        Send a URL as a `link` part to deliver it with a rich preview card showing the
        page's title, description, and image (when available). A `link` part must be the
        **only** part in the message — it cannot be combined with text or media parts.
        To send a URL without a preview card, include it in a `text` part instead.

        **Limitations:**
        - A `link` part cannot be combined with other parts in the same message.
        - Maximum URL length: 2,048 characters.
        """
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithStreamingResponse:
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

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AttachmentsResourceWithStreamingResponse

        return AttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.PhonenumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phonenumbers import PhonenumbersResourceWithStreamingResponse

        return PhonenumbersResourceWithStreamingResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phone_numbers import PhoneNumbersResourceWithStreamingResponse

        return PhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def webhook_events(self) -> webhook_events.WebhookEventsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import WebhookEventsResourceWithStreamingResponse

        return WebhookEventsResourceWithStreamingResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.WebhookSubscriptionsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import WebhookSubscriptionsResourceWithStreamingResponse

        return WebhookSubscriptionsResourceWithStreamingResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.CapabilityResourceWithStreamingResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import CapabilityResourceWithStreamingResponse

        return CapabilityResourceWithStreamingResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.ContactCardResourceWithStreamingResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import ContactCardResourceWithStreamingResponse

        return ContactCardResourceWithStreamingResponse(self._client.contact_card)


class AsyncLinqAPIV3WithStreamedResponse:
    _client: AsyncLinqAPIV3

    def __init__(self, client: AsyncLinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithStreamingResponse:
        from .resources.chats import AsyncChatsResourceWithStreamingResponse

        return AsyncChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """Messages are individual communications within a chat thread.

        Messages can include text, media attachments, rich link previews, special effects
        (like confetti or fireworks), and reactions. All messages are associated with a
        specific chat and sent from a phone number you own.

        Messages support delivery status tracking, read receipts, and editing capabilities.

        ## Rich Link Previews

        Send a URL as a `link` part to deliver it with a rich preview card showing the
        page's title, description, and image (when available). A `link` part must be the
        **only** part in the message — it cannot be combined with text or media parts.
        To send a URL without a preview card, include it in a `text` part instead.

        **Limitations:**
        - A `link` part cannot be combined with other parts in the same message.
        - Maximum URL length: 2,048 characters.
        """
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithStreamingResponse:
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

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithStreamingResponse

        return AsyncAttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.AsyncPhonenumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phonenumbers import AsyncPhonenumbersResourceWithStreamingResponse

        return AsyncPhonenumbersResourceWithStreamingResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithStreamingResponse

        return AsyncPhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def webhook_events(self) -> webhook_events.AsyncWebhookEventsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import AsyncWebhookEventsResourceWithStreamingResponse

        return AsyncWebhookEventsResourceWithStreamingResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.AsyncWebhookSubscriptionsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import AsyncWebhookSubscriptionsResourceWithStreamingResponse

        return AsyncWebhookSubscriptionsResourceWithStreamingResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.AsyncCapabilityResourceWithStreamingResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import AsyncCapabilityResourceWithStreamingResponse

        return AsyncCapabilityResourceWithStreamingResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.AsyncContactCardResourceWithStreamingResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import AsyncContactCardResourceWithStreamingResponse

        return AsyncContactCardResourceWithStreamingResponse(self._client.contact_card)


Client = LinqAPIV3

AsyncClient = AsyncLinqAPIV3
