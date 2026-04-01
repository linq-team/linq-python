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

    Each webhook request includes the following headers:

    | Header | Description |
    |--------|-------------|
    | `X-Webhook-Event` | The event type (e.g., `message.sent`, `message.received`) |
    | `X-Webhook-Subscription-ID` | Your webhook subscription ID |
    | `X-Webhook-Timestamp` | Unix timestamp (seconds) when the webhook was sent |
    | `X-Webhook-Signature` | HMAC-SHA256 signature for verification |

    ## Verifying Webhook Signatures

    All webhooks are signed using HMAC-SHA256. You should always verify the signature
    to ensure the webhook originated from Linq and hasn't been tampered with.

    **Signature Construction:**

    The signature is computed over a concatenation of the timestamp and payload:

    ```
    {timestamp}.{payload}
    ```

    Where:
    - `timestamp` is the value from the `X-Webhook-Timestamp` header
    - `payload` is the raw JSON request body (exact bytes, not re-serialized)

    **Verification Steps:**

    1. Extract the `X-Webhook-Timestamp` and `X-Webhook-Signature` headers
    2. Get the raw request body bytes (do not parse and re-serialize)
    3. Concatenate: `"{timestamp}.{payload}"`
    4. Compute HMAC-SHA256 using your signing secret as the key
    5. Hex-encode the result and compare with `X-Webhook-Signature`
    6. Use constant-time comparison to prevent timing attacks

    **Example (Python):**

    ```python
    import hmac
    import hashlib


    def verify_webhook(signing_secret, payload, timestamp, signature):
        message = f"{timestamp}.{payload.decode('utf-8')}"
        expected = hmac.new(signing_secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)
    ```

    **Example (Node.js):**

    ```javascript
    const crypto = require('crypto');

    function verifyWebhook(signingSecret, payload, timestamp, signature) {
      const message = `${timestamp}.${payload}`;
      const expected = crypto
        .createHmac('sha256', signingSecret)
        .update(message)
        .digest('hex');
      return crypto.timingSafeEqual(
        Buffer.from(expected),
        Buffer.from(signature)
      );
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

    Each webhook request includes the following headers:

    | Header | Description |
    |--------|-------------|
    | `X-Webhook-Event` | The event type (e.g., `message.sent`, `message.received`) |
    | `X-Webhook-Subscription-ID` | Your webhook subscription ID |
    | `X-Webhook-Timestamp` | Unix timestamp (seconds) when the webhook was sent |
    | `X-Webhook-Signature` | HMAC-SHA256 signature for verification |

    ## Verifying Webhook Signatures

    All webhooks are signed using HMAC-SHA256. You should always verify the signature
    to ensure the webhook originated from Linq and hasn't been tampered with.

    **Signature Construction:**

    The signature is computed over a concatenation of the timestamp and payload:

    ```
    {timestamp}.{payload}
    ```

    Where:
    - `timestamp` is the value from the `X-Webhook-Timestamp` header
    - `payload` is the raw JSON request body (exact bytes, not re-serialized)

    **Verification Steps:**

    1. Extract the `X-Webhook-Timestamp` and `X-Webhook-Signature` headers
    2. Get the raw request body bytes (do not parse and re-serialize)
    3. Concatenate: `"{timestamp}.{payload}"`
    4. Compute HMAC-SHA256 using your signing secret as the key
    5. Hex-encode the result and compare with `X-Webhook-Signature`
    6. Use constant-time comparison to prevent timing attacks

    **Example (Python):**

    ```python
    import hmac
    import hashlib


    def verify_webhook(signing_secret, payload, timestamp, signature):
        message = f"{timestamp}.{payload.decode('utf-8')}"
        expected = hmac.new(signing_secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)
    ```

    **Example (Node.js):**

    ```javascript
    const crypto = require('crypto');

    function verifyWebhook(signingSecret, payload, timestamp, signature) {
      const message = `${timestamp}.${payload}`;
      const expected = crypto
        .createHmac('sha256', signingSecret)
        .update(message)
        .digest('hex');
      return crypto.timingSafeEqual(
        Buffer.from(expected),
        Buffer.from(signature)
      );
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
