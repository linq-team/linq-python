# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import webhook_subscription_create_params, webhook_subscription_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.webhook_event_type import WebhookEventType
from ..types.webhook_subscription import WebhookSubscription
from ..types.webhook_subscription_list_response import WebhookSubscriptionListResponse
from ..types.webhook_subscription_create_response import WebhookSubscriptionCreateResponse

__all__ = ["WebhookSubscriptionsResource", "AsyncWebhookSubscriptionsResource"]


class WebhookSubscriptionsResource(SyncAPIResource):
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
    def with_raw_response(self) -> WebhookSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return WebhookSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return WebhookSubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        subscribed_events: List[WebhookEventType],
        target_url: str,
        phone_numbers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscriptionCreateResponse:
        """Create a new webhook subscription to receive events at a target URL.

        Upon
        creation, a signing secret is generated for verifying webhook authenticity.
        **Store this secret securely — it cannot be retrieved later.**

        **Phone Number Filtering:**

        - Optionally specify `phone_numbers` to only receive events for specific lines
        - If omitted, events from all phone numbers are delivered (default behavior)
        - Use multiple subscriptions with different `phone_numbers` to route different
          lines to different endpoints
        - Each `target_url` can only be used once per account. To route different lines
          to different destinations, use a unique URL per subscription (e.g., append a
          query parameter: `https://example.com/webhook?line=1`)

        **Webhook Delivery:**

        - Events are sent via HTTP POST to the target URL
        - Each request includes `X-Webhook-Signature` and `X-Webhook-Timestamp` headers
        - Signature is HMAC-SHA256 over `{timestamp}.{payload}` — see
          [Webhook Events](/docs/webhook-events) for verification details
        - Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
          ~25 minutes with exponential backoff
        - Client errors (4xx except 429) are not retried

        Args:
          subscribed_events: List of event types to subscribe to

          target_url: URL where webhook events will be sent. Must be HTTPS.

          phone_numbers: Optional list of phone numbers to filter events for. Only events originating
              from these phone numbers will be delivered to this subscription. If omitted or
              empty, events from all phone numbers are delivered. Phone numbers must be in
              E.164 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/webhook-subscriptions",
            body=maybe_transform(
                {
                    "subscribed_events": subscribed_events,
                    "target_url": target_url,
                    "phone_numbers": phone_numbers,
                },
                webhook_subscription_create_params.WebhookSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscriptionCreateResponse,
        )

    def retrieve(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscription:
        """
        Retrieve details for a specific webhook subscription including its target URL,
        subscribed events, and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._get(
            path_template("/v3/webhook-subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscription,
        )

    def update(
        self,
        subscription_id: str,
        *,
        is_active: bool | Omit = omit,
        phone_numbers: Optional[SequenceNotStr[str]] | Omit = omit,
        subscribed_events: List[WebhookEventType] | Omit = omit,
        target_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscription:
        """Update an existing webhook subscription.

        You can modify the target URL,
        subscribed events, or activate/deactivate the subscription.

        **Note:** The signing secret cannot be changed via this endpoint.

        Args:
          is_active: Activate or deactivate the subscription

          phone_numbers: Updated list of phone numbers to filter events for. Set to a non-empty array to
              filter events to specific phone numbers. Set to an empty array or null to remove
              the filter and receive events from all phone numbers. Phone numbers must be in
              E.164 format.

          subscribed_events: Updated list of event types to subscribe to

          target_url: New target URL for webhook events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._put(
            path_template("/v3/webhook-subscriptions/{subscription_id}", subscription_id=subscription_id),
            body=maybe_transform(
                {
                    "is_active": is_active,
                    "phone_numbers": phone_numbers,
                    "subscribed_events": subscribed_events,
                    "target_url": target_url,
                },
                webhook_subscription_update_params.WebhookSubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscription,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscriptionListResponse:
        """Retrieve all webhook subscriptions for the authenticated partner.

        Returns a list
        of active and inactive subscriptions with their configuration and status.
        """
        return self._get(
            "/v3/webhook-subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscriptionListResponse,
        )

    def delete(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a webhook subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/webhook-subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWebhookSubscriptionsResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncWebhookSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncWebhookSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        subscribed_events: List[WebhookEventType],
        target_url: str,
        phone_numbers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscriptionCreateResponse:
        """Create a new webhook subscription to receive events at a target URL.

        Upon
        creation, a signing secret is generated for verifying webhook authenticity.
        **Store this secret securely — it cannot be retrieved later.**

        **Phone Number Filtering:**

        - Optionally specify `phone_numbers` to only receive events for specific lines
        - If omitted, events from all phone numbers are delivered (default behavior)
        - Use multiple subscriptions with different `phone_numbers` to route different
          lines to different endpoints
        - Each `target_url` can only be used once per account. To route different lines
          to different destinations, use a unique URL per subscription (e.g., append a
          query parameter: `https://example.com/webhook?line=1`)

        **Webhook Delivery:**

        - Events are sent via HTTP POST to the target URL
        - Each request includes `X-Webhook-Signature` and `X-Webhook-Timestamp` headers
        - Signature is HMAC-SHA256 over `{timestamp}.{payload}` — see
          [Webhook Events](/docs/webhook-events) for verification details
        - Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
          ~25 minutes with exponential backoff
        - Client errors (4xx except 429) are not retried

        Args:
          subscribed_events: List of event types to subscribe to

          target_url: URL where webhook events will be sent. Must be HTTPS.

          phone_numbers: Optional list of phone numbers to filter events for. Only events originating
              from these phone numbers will be delivered to this subscription. If omitted or
              empty, events from all phone numbers are delivered. Phone numbers must be in
              E.164 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/webhook-subscriptions",
            body=await async_maybe_transform(
                {
                    "subscribed_events": subscribed_events,
                    "target_url": target_url,
                    "phone_numbers": phone_numbers,
                },
                webhook_subscription_create_params.WebhookSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscriptionCreateResponse,
        )

    async def retrieve(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscription:
        """
        Retrieve details for a specific webhook subscription including its target URL,
        subscribed events, and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._get(
            path_template("/v3/webhook-subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscription,
        )

    async def update(
        self,
        subscription_id: str,
        *,
        is_active: bool | Omit = omit,
        phone_numbers: Optional[SequenceNotStr[str]] | Omit = omit,
        subscribed_events: List[WebhookEventType] | Omit = omit,
        target_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscription:
        """Update an existing webhook subscription.

        You can modify the target URL,
        subscribed events, or activate/deactivate the subscription.

        **Note:** The signing secret cannot be changed via this endpoint.

        Args:
          is_active: Activate or deactivate the subscription

          phone_numbers: Updated list of phone numbers to filter events for. Set to a non-empty array to
              filter events to specific phone numbers. Set to an empty array or null to remove
              the filter and receive events from all phone numbers. Phone numbers must be in
              E.164 format.

          subscribed_events: Updated list of event types to subscribe to

          target_url: New target URL for webhook events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._put(
            path_template("/v3/webhook-subscriptions/{subscription_id}", subscription_id=subscription_id),
            body=await async_maybe_transform(
                {
                    "is_active": is_active,
                    "phone_numbers": phone_numbers,
                    "subscribed_events": subscribed_events,
                    "target_url": target_url,
                },
                webhook_subscription_update_params.WebhookSubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscription,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSubscriptionListResponse:
        """Retrieve all webhook subscriptions for the authenticated partner.

        Returns a list
        of active and inactive subscriptions with their configuration and status.
        """
        return await self._get(
            "/v3/webhook-subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSubscriptionListResponse,
        )

    async def delete(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a webhook subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/webhook-subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WebhookSubscriptionsResourceWithRawResponse:
    def __init__(self, webhook_subscriptions: WebhookSubscriptionsResource) -> None:
        self._webhook_subscriptions = webhook_subscriptions

        self.create = to_raw_response_wrapper(
            webhook_subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhook_subscriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhook_subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            webhook_subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            webhook_subscriptions.delete,
        )


class AsyncWebhookSubscriptionsResourceWithRawResponse:
    def __init__(self, webhook_subscriptions: AsyncWebhookSubscriptionsResource) -> None:
        self._webhook_subscriptions = webhook_subscriptions

        self.create = async_to_raw_response_wrapper(
            webhook_subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhook_subscriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhook_subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhook_subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhook_subscriptions.delete,
        )


class WebhookSubscriptionsResourceWithStreamingResponse:
    def __init__(self, webhook_subscriptions: WebhookSubscriptionsResource) -> None:
        self._webhook_subscriptions = webhook_subscriptions

        self.create = to_streamed_response_wrapper(
            webhook_subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhook_subscriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhook_subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            webhook_subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhook_subscriptions.delete,
        )


class AsyncWebhookSubscriptionsResourceWithStreamingResponse:
    def __init__(self, webhook_subscriptions: AsyncWebhookSubscriptionsResource) -> None:
        self._webhook_subscriptions = webhook_subscriptions

        self.create = async_to_streamed_response_wrapper(
            webhook_subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhook_subscriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhook_subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhook_subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhook_subscriptions.delete,
        )
