# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncListMessagesPagination, AsyncListMessagesPagination
from ...types.chats import message_list_params, message_send_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message import Message
from ...types.message_content_param import MessageContentParam
from ...types.chats.message_send_response import MessageSendResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
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
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def list(
        self,
        chat_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncListMessagesPagination[Message]:
        """
        Retrieve messages from a specific chat with pagination support.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get_api_list(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            page=SyncListMessagesPagination[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    def send(
        self,
        chat_id: str,
        *,
        message: MessageContentParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a message to an existing chat.

        Use this endpoint when you already have a
        chat ID and want to send additional messages to it.

        ## Message Effects

        You can add iMessage effects to make your messages more expressive. Effects are
        optional and can be either screen effects (full-screen animations) or bubble
        effects (message bubble animations).

        **Screen Effects:** `confetti`, `fireworks`, `lasers`, `sparkles`,
        `celebration`, `hearts`, `love`, `balloons`, `happy_birthday`, `echo`,
        `spotlight`

        **Bubble Effects:** `slam`, `loud`, `gentle`, `invisible`

        Only one effect type can be applied per message.

        ## Inline Text Decorations (iMessage only)

        Use the `text_decorations` array on a text part to apply styling and animations
        to character ranges.

        Each decoration specifies a `range: [start, end)` and exactly one of `style` or
        `animation`.

        **Styles:** `bold`, `italic`, `strikethrough`, `underline` **Animations:**
        `big`, `small`, `shake`, `nod`, `explode`, `ripple`, `bloom`, `jitter`

        ```json
        {
          "type": "text",
          "value": "Hello world",
          "text_decorations": [
            { "range": [0, 5], "style": "bold" },
            { "range": [6, 11], "animation": "shake" }
          ]
        }
        ```

        **Note:** Style ranges (bold, italic, etc.) may overlap, but animation ranges
        must not overlap with other animations or styles. Text decorations only render
        for iMessage recipients. For SMS/RCS, text decorations are not applied.

        Args:
          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            body=maybe_transform({"message": message}, message_send_params.MessageSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
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
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    def list(
        self,
        chat_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncListMessagesPagination[Message]]:
        """
        Retrieve messages from a specific chat with pagination support.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get_api_list(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            page=AsyncListMessagesPagination[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    async def send(
        self,
        chat_id: str,
        *,
        message: MessageContentParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a message to an existing chat.

        Use this endpoint when you already have a
        chat ID and want to send additional messages to it.

        ## Message Effects

        You can add iMessage effects to make your messages more expressive. Effects are
        optional and can be either screen effects (full-screen animations) or bubble
        effects (message bubble animations).

        **Screen Effects:** `confetti`, `fireworks`, `lasers`, `sparkles`,
        `celebration`, `hearts`, `love`, `balloons`, `happy_birthday`, `echo`,
        `spotlight`

        **Bubble Effects:** `slam`, `loud`, `gentle`, `invisible`

        Only one effect type can be applied per message.

        ## Inline Text Decorations (iMessage only)

        Use the `text_decorations` array on a text part to apply styling and animations
        to character ranges.

        Each decoration specifies a `range: [start, end)` and exactly one of `style` or
        `animation`.

        **Styles:** `bold`, `italic`, `strikethrough`, `underline` **Animations:**
        `big`, `small`, `shake`, `nod`, `explode`, `ripple`, `bloom`, `jitter`

        ```json
        {
          "type": "text",
          "value": "Hello world",
          "text_decorations": [
            { "range": [0, 5], "style": "bold" },
            { "range": [6, 11], "animation": "shake" }
          ]
        }
        ```

        **Note:** Style ranges (bold, italic, etc.) may overlap, but animation ranges
        must not overlap with other animations or styles. Text decorations only render
        for iMessage recipients. For SMS/RCS, text decorations are not applied.

        Args:
          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            body=await async_maybe_transform({"message": message}, message_send_params.MessageSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
