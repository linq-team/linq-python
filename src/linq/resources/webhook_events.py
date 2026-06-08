# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_event_list_response import WebhookEventListResponse

__all__ = ["WebhookEventsResource", "AsyncWebhookEventsResource"]


class WebhookEventsResource(SyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> WebhookEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return WebhookEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return WebhookEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEventListResponse:
        """Returns all available webhook event types that can be subscribed to.

        Use this
        endpoint to discover valid values for the `subscribed_events` field when
        creating or updating webhook subscriptions.
        """
        return self._get(
            "/v3/webhook-events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEventListResponse,
        )


class AsyncWebhookEventsResource(AsyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> AsyncWebhookEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncWebhookEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEventListResponse:
        """Returns all available webhook event types that can be subscribed to.

        Use this
        endpoint to discover valid values for the `subscribed_events` field when
        creating or updating webhook subscriptions.
        """
        return await self._get(
            "/v3/webhook-events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEventListResponse,
        )


class WebhookEventsResourceWithRawResponse:
    def __init__(self, webhook_events: WebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.list = to_raw_response_wrapper(
            webhook_events.list,
        )


class AsyncWebhookEventsResourceWithRawResponse:
    def __init__(self, webhook_events: AsyncWebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.list = async_to_raw_response_wrapper(
            webhook_events.list,
        )


class WebhookEventsResourceWithStreamingResponse:
    def __init__(self, webhook_events: WebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.list = to_streamed_response_wrapper(
            webhook_events.list,
        )


class AsyncWebhookEventsResourceWithStreamingResponse:
    def __init__(self, webhook_events: AsyncWebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.list = async_to_streamed_response_wrapper(
            webhook_events.list,
        )
