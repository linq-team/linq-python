# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.messages import poll_vote_params, poll_add_options_params
from ...types.chats.poll_envelope import PollEnvelope

__all__ = ["PollResource", "AsyncPollResource"]


class PollResource(SyncAPIResource):
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

    ## Ephemeral Messages (Privacy Tier)

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is automatically given a fixed **24-hour retention window** — after that window the platform permanently deletes the message from Linq storage. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account is retained for 24 hours, then deleted. |
    | **Per phone number** | Only the specified phone numbers have their messages auto-deleted. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: 24 hours** from when the message is created |
    | After expiry | Message stays retrievable | Message is permanently deleted — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are scrubbed; the message is gone, not blanked out |
    | Cross-partner isolation | Enforced | Enforced |

    **How the 24-hour window works:**

    - The window is fixed at **24 hours from message creation** (`created_at`) and cannot be configured per message.
    - It mirrors the ephemeral *attachments* 1-day backstop, so a message and any media it carries expire together.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time. If you need it, compute `created_at + 24h` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> PollResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return PollResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PollResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return PollResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """
        Return a poll's current results — its options, each option's voters, and the
        distinct total number of voters — by the poll-definition message's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/v3/messages/{message_id}/poll", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )

    def add_options(
        self,
        message_id: str,
        *,
        options: Iterable[poll_add_options_params.Option],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """Add one or more options to an existing poll.

        Options are **add-only and
        immutable** — you can append options but never edit or remove them (Apple
        constraint). Returns the full poll.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/v3/messages/{message_id}/poll/options", message_id=message_id),
            body=maybe_transform({"options": options}, poll_add_options_params.PollAddOptionsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )

    def vote(
        self,
        message_id: str,
        *,
        operation: Literal["add", "remove"],
        option_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """
        Add or remove your line's vote on **one** poll option (per-option toggle —
        iMessage polls are toggled one option at a time). Returns the poll reflecting
        the toggle.

        Args:
          operation: Add or remove your line's vote on the option.

          option_id: The option to toggle a vote on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/v3/messages/{message_id}/poll/votes", message_id=message_id),
            body=maybe_transform(
                {
                    "operation": operation,
                    "option_id": option_id,
                },
                poll_vote_params.PollVoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )


class AsyncPollResource(AsyncAPIResource):
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

    ## Ephemeral Messages (Privacy Tier)

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is automatically given a fixed **24-hour retention window** — after that window the platform permanently deletes the message from Linq storage. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account is retained for 24 hours, then deleted. |
    | **Per phone number** | Only the specified phone numbers have their messages auto-deleted. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: 24 hours** from when the message is created |
    | After expiry | Message stays retrievable | Message is permanently deleted — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are scrubbed; the message is gone, not blanked out |
    | Cross-partner isolation | Enforced | Enforced |

    **How the 24-hour window works:**

    - The window is fixed at **24 hours from message creation** (`created_at`) and cannot be configured per message.
    - It mirrors the ephemeral *attachments* 1-day backstop, so a message and any media it carries expire together.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time. If you need it, compute `created_at + 24h` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPollResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPollResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPollResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncPollResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """
        Return a poll's current results — its options, each option's voters, and the
        distinct total number of voters — by the poll-definition message's ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/v3/messages/{message_id}/poll", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )

    async def add_options(
        self,
        message_id: str,
        *,
        options: Iterable[poll_add_options_params.Option],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """Add one or more options to an existing poll.

        Options are **add-only and
        immutable** — you can append options but never edit or remove them (Apple
        constraint). Returns the full poll.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/v3/messages/{message_id}/poll/options", message_id=message_id),
            body=await async_maybe_transform({"options": options}, poll_add_options_params.PollAddOptionsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )

    async def vote(
        self,
        message_id: str,
        *,
        operation: Literal["add", "remove"],
        option_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """
        Add or remove your line's vote on **one** poll option (per-option toggle —
        iMessage polls are toggled one option at a time). Returns the poll reflecting
        the toggle.

        Args:
          operation: Add or remove your line's vote on the option.

          option_id: The option to toggle a vote on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/v3/messages/{message_id}/poll/votes", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "operation": operation,
                    "option_id": option_id,
                },
                poll_vote_params.PollVoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )


class PollResourceWithRawResponse:
    def __init__(self, poll: PollResource) -> None:
        self._poll = poll

        self.retrieve = to_raw_response_wrapper(
            poll.retrieve,
        )
        self.add_options = to_raw_response_wrapper(
            poll.add_options,
        )
        self.vote = to_raw_response_wrapper(
            poll.vote,
        )


class AsyncPollResourceWithRawResponse:
    def __init__(self, poll: AsyncPollResource) -> None:
        self._poll = poll

        self.retrieve = async_to_raw_response_wrapper(
            poll.retrieve,
        )
        self.add_options = async_to_raw_response_wrapper(
            poll.add_options,
        )
        self.vote = async_to_raw_response_wrapper(
            poll.vote,
        )


class PollResourceWithStreamingResponse:
    def __init__(self, poll: PollResource) -> None:
        self._poll = poll

        self.retrieve = to_streamed_response_wrapper(
            poll.retrieve,
        )
        self.add_options = to_streamed_response_wrapper(
            poll.add_options,
        )
        self.vote = to_streamed_response_wrapper(
            poll.vote,
        )


class AsyncPollResourceWithStreamingResponse:
    def __init__(self, poll: AsyncPollResource) -> None:
        self._poll = poll

        self.retrieve = async_to_streamed_response_wrapper(
            poll.retrieve,
        )
        self.add_options = async_to_streamed_response_wrapper(
            poll.add_options,
        )
        self.vote = async_to_streamed_response_wrapper(
            poll.vote,
        )
