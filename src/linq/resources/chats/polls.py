# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.chats import poll_create_params
from ..._base_client import make_request_options
from ...types.chats.poll_envelope import PollEnvelope

__all__ = ["PollsResource", "AsyncPollsResource"]


class PollsResource(SyncAPIResource):
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

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is given a **retention window configured for your account**. After that window, the message's text, formatting, and attachment references are no longer retrievable through the API — see the Attachments row below for how the attachment media itself is handled. Metadata about the message is retained: message identifiers, timestamps, phone numbers, and delivery state. Metadata retention is not bounded by this window. Bounded operational copies, such as backups and delivery queues, expire on their own separate schedules. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    The window can be set anywhere from **60 minutes to 24 hours**, and defaults to **24 hours**. Ask your Linq support contact to configure a shorter window; it cannot be changed through the API.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account has its content removed from the API surface after your configured window. Metadata is retained. |
    | **Per phone number** | Only the specified phone numbers have message content removed from the API surface this way. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: your configured window** (60 minutes – 24 hours, default 24 hours) from when the message is created |
    | After expiry | Message stays retrievable | Message content is no longer retrievable — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are removed from the API surface, not blanked out in place. Metadata (identifiers, timestamps, phone numbers, delivery state) is retained; its retention is not bounded by this window |
    | Attachments | Retained | Media sent on the **ephemeral attachments tier** is removed on its own storage backstop — within roughly 24–48 hours of upload — independently of the message window, so it can outlast a window shorter than a day. Attachments on the persistent tier (including pre-uploads via `POST /v3/attachments`) are kept until you `DELETE` them |
    | Cross-partner isolation | Enforced | Enforced |

    **How the retention window works:**

    - The window runs from **message creation** (`created_at`). It is configured for your account (60 minutes – 24 hours, default 24 hours) and cannot be set per message.
    - Attachment media follows its own storage backstop rather than the message window — see the Attachments row above.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.
    - **Deletion happens shortly *after* the window, not exactly at it.** A background sweep runs every ~5 minutes, so a message typically stops being retrievable within about 5 minutes of its expiry, and longer while a backlog is being worked through. Treat the window as the guaranteed *minimum* retention, never as an exact deletion time or an upper bound.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time, and they do not report your configured window either — so if you are on a window shorter than 24 hours you cannot derive a message's expiry from the API today. Track the window you agreed with your Linq support contact and compute `created_at + window` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **The attachment backstop is separate from the message window.** API retrievability (the `404` behavior above) ends at your configured window. Ephemeral-tier media objects are removed on their own storage backstop — within roughly 24–48 hours of upload — which is independent of the message window and can outlast a window shorter than a day. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message once its window passes, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> PollsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return PollsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PollsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return PollsResourceWithStreamingResponse(self)

    def create(
        self,
        chat_id: str,
        *,
        poll: poll_create_params.Poll,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """Create an iMessage poll in an existing chat and send it.

        Polls are
        iMessage-only.

        The chat must already exist — **a poll cannot be the first message of a new
        chat** (use `POST /v3/chats` for that). Options are **add-only and immutable**:
        you can add options later via `POST /v3/messages/{messageId}/poll/options`, but
        never edit or remove them.

        Args:
          poll: Poll content to create. A poll needs at least two options. Options are add-only
              and immutable — there is no title/question (send that as a normal text message).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v3/chats/{chat_id}/polls", chat_id=chat_id),
            body=maybe_transform({"poll": poll}, poll_create_params.PollCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )


class AsyncPollsResource(AsyncAPIResource):
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

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is given a **retention window configured for your account**. After that window, the message's text, formatting, and attachment references are no longer retrievable through the API — see the Attachments row below for how the attachment media itself is handled. Metadata about the message is retained: message identifiers, timestamps, phone numbers, and delivery state. Metadata retention is not bounded by this window. Bounded operational copies, such as backups and delivery queues, expire on their own separate schedules. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    The window can be set anywhere from **60 minutes to 24 hours**, and defaults to **24 hours**. Ask your Linq support contact to configure a shorter window; it cannot be changed through the API.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account has its content removed from the API surface after your configured window. Metadata is retained. |
    | **Per phone number** | Only the specified phone numbers have message content removed from the API surface this way. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: your configured window** (60 minutes – 24 hours, default 24 hours) from when the message is created |
    | After expiry | Message stays retrievable | Message content is no longer retrievable — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are removed from the API surface, not blanked out in place. Metadata (identifiers, timestamps, phone numbers, delivery state) is retained; its retention is not bounded by this window |
    | Attachments | Retained | Media sent on the **ephemeral attachments tier** is removed on its own storage backstop — within roughly 24–48 hours of upload — independently of the message window, so it can outlast a window shorter than a day. Attachments on the persistent tier (including pre-uploads via `POST /v3/attachments`) are kept until you `DELETE` them |
    | Cross-partner isolation | Enforced | Enforced |

    **How the retention window works:**

    - The window runs from **message creation** (`created_at`). It is configured for your account (60 minutes – 24 hours, default 24 hours) and cannot be set per message.
    - Attachment media follows its own storage backstop rather than the message window — see the Attachments row above.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.
    - **Deletion happens shortly *after* the window, not exactly at it.** A background sweep runs every ~5 minutes, so a message typically stops being retrievable within about 5 minutes of its expiry, and longer while a backlog is being worked through. Treat the window as the guaranteed *minimum* retention, never as an exact deletion time or an upper bound.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time, and they do not report your configured window either — so if you are on a window shorter than 24 hours you cannot derive a message's expiry from the API today. Track the window you agreed with your Linq support contact and compute `created_at + window` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **The attachment backstop is separate from the message window.** API retrievability (the `404` behavior above) ends at your configured window. Ephemeral-tier media objects are removed on their own storage backstop — within roughly 24–48 hours of upload — which is independent of the message window and can outlast a window shorter than a day. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message once its window passes, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPollsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPollsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPollsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncPollsResourceWithStreamingResponse(self)

    async def create(
        self,
        chat_id: str,
        *,
        poll: poll_create_params.Poll,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PollEnvelope:
        """Create an iMessage poll in an existing chat and send it.

        Polls are
        iMessage-only.

        The chat must already exist — **a poll cannot be the first message of a new
        chat** (use `POST /v3/chats` for that). Options are **add-only and immutable**:
        you can add options later via `POST /v3/messages/{messageId}/poll/options`, but
        never edit or remove them.

        Args:
          poll: Poll content to create. A poll needs at least two options. Options are add-only
              and immutable — there is no title/question (send that as a normal text message).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v3/chats/{chat_id}/polls", chat_id=chat_id),
            body=await async_maybe_transform({"poll": poll}, poll_create_params.PollCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PollEnvelope,
        )


class PollsResourceWithRawResponse:
    def __init__(self, polls: PollsResource) -> None:
        self._polls = polls

        self.create = to_raw_response_wrapper(
            polls.create,
        )


class AsyncPollsResourceWithRawResponse:
    def __init__(self, polls: AsyncPollsResource) -> None:
        self._polls = polls

        self.create = async_to_raw_response_wrapper(
            polls.create,
        )


class PollsResourceWithStreamingResponse:
    def __init__(self, polls: PollsResource) -> None:
        self._polls = polls

        self.create = to_streamed_response_wrapper(
            polls.create,
        )


class AsyncPollsResourceWithStreamingResponse:
    def __init__(self, polls: AsyncPollsResource) -> None:
        self._polls = polls

        self.create = async_to_streamed_response_wrapper(
            polls.create,
        )
