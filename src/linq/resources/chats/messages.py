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
