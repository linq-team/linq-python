# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["TypingResource", "AsyncTypingResource"]


class TypingResource(SyncAPIResource):
    """A Chat is a conversation thread with one or more participants.

    To begin a chat, you must create a Chat with at least one recipient handle.
    Including multiple handles creates a group chat.

    When creating a chat, the `from` field specifies which of your
    authorized phone numbers the message originates from. Your authentication token grants
    access to one or more phone numbers, but the `from` field determines the actual sender.

    **Handle Format:**
    - Handles can be phone numbers or email addresses
    - Phone numbers MUST be in E.164 format (starting with +)
    - Phone format: `+[country code][subscriber number]`
    - Example phone: `+12223334444` (US), `+442071234567` (UK), `+81312345678` (Japan)
    - Example email: `user@example.com`
    - No spaces, dashes, or parentheses in phone numbers
    """

    @cached_property
    def with_raw_response(self) -> TypingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return TypingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return TypingResourceWithStreamingResponse(self)

    def start(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a typing indicator to show that someone is typing in the chat.

        ## Behavior & Limitations

        Typing indicators are best-effort signals with the following limitations:

        - **Active conversations only:** The recipient must have sent or received a
          message in this chat within the **last 5 minutes**. If the chat is inactive,
          the request is still accepted (`204`) but the indicator will not reach the
          recipient's device.

        - **No delivery guarantee:** Even for active chats, a `204` response only
          indicates the request was accepted for processing.

        - **Group chats not supported:** Attempting to start a typing indicator in a
          group chat will return a `403` error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v3/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stop(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop the typing indicator for the chat.

        Typing indicators are automatically stopped when a message is sent, so calling
        this endpoint after sending a message is unnecessary.

        See the `POST` endpoint above for behavior details and limitations.

        **Note:** Group chats are not supported and will return a `403` error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTypingResource(AsyncAPIResource):
    """A Chat is a conversation thread with one or more participants.

    To begin a chat, you must create a Chat with at least one recipient handle.
    Including multiple handles creates a group chat.

    When creating a chat, the `from` field specifies which of your
    authorized phone numbers the message originates from. Your authentication token grants
    access to one or more phone numbers, but the `from` field determines the actual sender.

    **Handle Format:**
    - Handles can be phone numbers or email addresses
    - Phone numbers MUST be in E.164 format (starting with +)
    - Phone format: `+[country code][subscriber number]`
    - Example phone: `+12223334444` (US), `+442071234567` (UK), `+81312345678` (Japan)
    - Example email: `user@example.com`
    - No spaces, dashes, or parentheses in phone numbers
    """

    @cached_property
    def with_raw_response(self) -> AsyncTypingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncTypingResourceWithStreamingResponse(self)

    async def start(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a typing indicator to show that someone is typing in the chat.

        ## Behavior & Limitations

        Typing indicators are best-effort signals with the following limitations:

        - **Active conversations only:** The recipient must have sent or received a
          message in this chat within the **last 5 minutes**. If the chat is inactive,
          the request is still accepted (`204`) but the indicator will not reach the
          recipient's device.

        - **No delivery guarantee:** Even for active chats, a `204` response only
          indicates the request was accepted for processing.

        - **Group chats not supported:** Attempting to start a typing indicator in a
          group chat will return a `403` error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v3/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stop(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop the typing indicator for the chat.

        Typing indicators are automatically stopped when a message is sent, so calling
        this endpoint after sending a message is unnecessary.

        See the `POST` endpoint above for behavior details and limitations.

        **Note:** Group chats are not supported and will return a `403` error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/chats/{chat_id}/typing", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TypingResourceWithRawResponse:
    def __init__(self, typing: TypingResource) -> None:
        self._typing = typing

        self.start = to_raw_response_wrapper(
            typing.start,
        )
        self.stop = to_raw_response_wrapper(
            typing.stop,
        )


class AsyncTypingResourceWithRawResponse:
    def __init__(self, typing: AsyncTypingResource) -> None:
        self._typing = typing

        self.start = async_to_raw_response_wrapper(
            typing.start,
        )
        self.stop = async_to_raw_response_wrapper(
            typing.stop,
        )


class TypingResourceWithStreamingResponse:
    def __init__(self, typing: TypingResource) -> None:
        self._typing = typing

        self.start = to_streamed_response_wrapper(
            typing.start,
        )
        self.stop = to_streamed_response_wrapper(
            typing.stop,
        )


class AsyncTypingResourceWithStreamingResponse:
    def __init__(self, typing: AsyncTypingResource) -> None:
        self._typing = typing

        self.start = async_to_streamed_response_wrapper(
            typing.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            typing.stop,
        )
