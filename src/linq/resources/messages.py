# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import message_update_params, message_add_reaction_params, message_list_messages_thread_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncListMessagesPagination, AsyncListMessagesPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.message import Message
from ..types.shared.reaction_type import ReactionType
from ..types.message_add_reaction_response import MessageAddReactionResponse

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
    ) -> Message:
        """Retrieve a specific message by its ID.

        This endpoint returns the full message
        details including text, attachments, reactions, and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def update(
        self,
        message_id: str,
        *,
        text: str,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Edit the text content of a specific part of a previously sent message.

        **Note:** A message can be edited up to 5 times, and only within 15 minutes of
        when it was originally sent.

        Args:
          text: New text content for the message part

          part_index: Index of the message part to edit. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._patch(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            body=maybe_transform(
                {
                    "text": text,
                    "part_index": part_index,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a message from the Linq API only.

        This does NOT unsend or remove the
        message from the actual chat — recipients will still see the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_reaction(
        self,
        message_id: str,
        *,
        operation: Literal["add", "remove"],
        type: ReactionType,
        custom_emoji: str | Omit = omit,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageAddReactionResponse:
        """Add or remove emoji reactions to messages.

        Reactions let users express their
        response to a message without sending a new message.

        **Supported Reactions:**

        - love ❤️
        - like 👍
        - dislike 👎
        - laugh 😂
        - emphasize ‼️
        - question ❓
        - custom - any emoji (use `custom_emoji` field to specify)

        Args:
          operation: Whether to add or remove the reaction

          type: Type of reaction. Standard iMessage tapbacks are love, like, dislike, laugh,
              emphasize, question. Custom emoji reactions have type "custom" with the actual
              emoji in the custom_emoji field. Sticker reactions have type "sticker" with
              sticker attachment details in the sticker field.

          custom_emoji: Custom emoji string. Required when type is "custom".

          part_index: Optional index of the message part to react to. If not provided, reacts to the
              entire message (part 0).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/v3/messages/{message_id}/reactions", message_id=message_id),
            body=maybe_transform(
                {
                    "operation": operation,
                    "type": type,
                    "custom_emoji": custom_emoji,
                    "part_index": part_index,
                },
                message_add_reaction_params.MessageAddReactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAddReactionResponse,
        )

    def list_messages_thread(
        self,
        message_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncListMessagesPagination[Message]:
        """Retrieve all messages in a conversation thread.

        Given any message ID in the
        thread, returns the originator message and all replies in chronological order.

        If the message is not part of a thread, returns just that single message.

        Supports pagination and configurable ordering.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          order: Sort order for messages (asc = oldest first, desc = newest first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            path_template("/v3/messages/{message_id}/thread", message_id=message_id),
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
                        "order": order,
                    },
                    message_list_messages_thread_params.MessageListMessagesThreadParams,
                ),
            ),
            model=Message,
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
    ) -> Message:
        """Retrieve a specific message by its ID.

        This endpoint returns the full message
        details including text, attachments, reactions, and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def update(
        self,
        message_id: str,
        *,
        text: str,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Edit the text content of a specific part of a previously sent message.

        **Note:** A message can be edited up to 5 times, and only within 15 minutes of
        when it was originally sent.

        Args:
          text: New text content for the message part

          part_index: Index of the message part to edit. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._patch(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "part_index": part_index,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a message from the Linq API only.

        This does NOT unsend or remove the
        message from the actual chat — recipients will still see the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_reaction(
        self,
        message_id: str,
        *,
        operation: Literal["add", "remove"],
        type: ReactionType,
        custom_emoji: str | Omit = omit,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageAddReactionResponse:
        """Add or remove emoji reactions to messages.

        Reactions let users express their
        response to a message without sending a new message.

        **Supported Reactions:**

        - love ❤️
        - like 👍
        - dislike 👎
        - laugh 😂
        - emphasize ‼️
        - question ❓
        - custom - any emoji (use `custom_emoji` field to specify)

        Args:
          operation: Whether to add or remove the reaction

          type: Type of reaction. Standard iMessage tapbacks are love, like, dislike, laugh,
              emphasize, question. Custom emoji reactions have type "custom" with the actual
              emoji in the custom_emoji field. Sticker reactions have type "sticker" with
              sticker attachment details in the sticker field.

          custom_emoji: Custom emoji string. Required when type is "custom".

          part_index: Optional index of the message part to react to. If not provided, reacts to the
              entire message (part 0).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/v3/messages/{message_id}/reactions", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "operation": operation,
                    "type": type,
                    "custom_emoji": custom_emoji,
                    "part_index": part_index,
                },
                message_add_reaction_params.MessageAddReactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAddReactionResponse,
        )

    def list_messages_thread(
        self,
        message_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncListMessagesPagination[Message]]:
        """Retrieve all messages in a conversation thread.

        Given any message ID in the
        thread, returns the originator message and all replies in chronological order.

        If the message is not part of a thread, returns just that single message.

        Supports pagination and configurable ordering.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          order: Sort order for messages (asc = oldest first, desc = newest first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            path_template("/v3/messages/{message_id}/thread", message_id=message_id),
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
                        "order": order,
                    },
                    message_list_messages_thread_params.MessageListMessagesThreadParams,
                ),
            ),
            model=Message,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )
        self.add_reaction = to_raw_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = to_raw_response_wrapper(
            messages.list_messages_thread,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )
        self.add_reaction = async_to_raw_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = async_to_raw_response_wrapper(
            messages.list_messages_thread,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )
        self.add_reaction = to_streamed_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = to_streamed_response_wrapper(
            messages.list_messages_thread,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )
        self.add_reaction = async_to_streamed_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = async_to_streamed_response_wrapper(
            messages.list_messages_thread,
        )
