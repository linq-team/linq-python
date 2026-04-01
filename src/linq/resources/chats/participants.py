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
from ...types.chats import participant_add_params, participant_remove_params
from ..._base_client import make_request_options
from ...types.chats.participant_add_response import ParticipantAddResponse
from ...types.chats.participant_remove_response import ParticipantRemoveResponse

__all__ = ["ParticipantsResource", "AsyncParticipantsResource"]


class ParticipantsResource(SyncAPIResource):
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
    def with_raw_response(self) -> ParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return ParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return ParticipantsResourceWithStreamingResponse(self)

    def add(
        self,
        chat_id: str,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantAddResponse:
        """
        Add a new participant to an existing group chat.

        **Requirements:**

        - Group chats only (3+ existing participants)
        - New participant must support the same messaging service as the group
        - Cross-service additions not allowed (e.g., can't add RCS-only user to iMessage
          group)
        - For cross-service scenarios, create a new chat instead

        Args:
          handle: Phone number (E.164 format) or email address of the participant to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v3/chats/{chat_id}/participants", chat_id=chat_id),
            body=maybe_transform({"handle": handle}, participant_add_params.ParticipantAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantAddResponse,
        )

    def remove(
        self,
        chat_id: str,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantRemoveResponse:
        """
        Remove a participant from an existing group chat.

        **Requirements:**

        - Group chats only
        - Must have 3+ participants after removal

        Args:
          handle: Phone number (E.164 format) or email address of the participant to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._delete(
            path_template("/v3/chats/{chat_id}/participants", chat_id=chat_id),
            body=maybe_transform({"handle": handle}, participant_remove_params.ParticipantRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRemoveResponse,
        )


class AsyncParticipantsResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncParticipantsResourceWithStreamingResponse(self)

    async def add(
        self,
        chat_id: str,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantAddResponse:
        """
        Add a new participant to an existing group chat.

        **Requirements:**

        - Group chats only (3+ existing participants)
        - New participant must support the same messaging service as the group
        - Cross-service additions not allowed (e.g., can't add RCS-only user to iMessage
          group)
        - For cross-service scenarios, create a new chat instead

        Args:
          handle: Phone number (E.164 format) or email address of the participant to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v3/chats/{chat_id}/participants", chat_id=chat_id),
            body=await async_maybe_transform({"handle": handle}, participant_add_params.ParticipantAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantAddResponse,
        )

    async def remove(
        self,
        chat_id: str,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParticipantRemoveResponse:
        """
        Remove a participant from an existing group chat.

        **Requirements:**

        - Group chats only
        - Must have 3+ participants after removal

        Args:
          handle: Phone number (E.164 format) or email address of the participant to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._delete(
            path_template("/v3/chats/{chat_id}/participants", chat_id=chat_id),
            body=await async_maybe_transform({"handle": handle}, participant_remove_params.ParticipantRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRemoveResponse,
        )


class ParticipantsResourceWithRawResponse:
    def __init__(self, participants: ParticipantsResource) -> None:
        self._participants = participants

        self.add = to_raw_response_wrapper(
            participants.add,
        )
        self.remove = to_raw_response_wrapper(
            participants.remove,
        )


class AsyncParticipantsResourceWithRawResponse:
    def __init__(self, participants: AsyncParticipantsResource) -> None:
        self._participants = participants

        self.add = async_to_raw_response_wrapper(
            participants.add,
        )
        self.remove = async_to_raw_response_wrapper(
            participants.remove,
        )


class ParticipantsResourceWithStreamingResponse:
    def __init__(self, participants: ParticipantsResource) -> None:
        self._participants = participants

        self.add = to_streamed_response_wrapper(
            participants.add,
        )
        self.remove = to_streamed_response_wrapper(
            participants.remove,
        )


class AsyncParticipantsResourceWithStreamingResponse:
    def __init__(self, participants: AsyncParticipantsResource) -> None:
        self._participants = participants

        self.add = async_to_streamed_response_wrapper(
            participants.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            participants.remove,
        )
