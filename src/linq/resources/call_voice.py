# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import call_voice_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.call_voice_record import CallVoiceRecord
from ..types.call_voice_list_response import CallVoiceListResponse

__all__ = ["CallVoiceResource", "AsyncCallVoiceResource"]


class CallVoiceResource(SyncAPIResource):
    """Read the carrier (BYOC) voice calls received on your phone numbers.

    Each
    record is the durable form of the `call_voice.*` webhooks for that call and
    shares the same `id`, so you can look a call up by the id a webhook
    delivered. See SIP Profiles for routing inbound calls to your endpoint.
    """

    @cached_property
    def with_raw_response(self) -> CallVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return CallVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return CallVoiceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        call_voice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallVoiceRecord:
        """
        Retrieve a single carrier voice call by its `id` — the same id delivered in the
        `call_voice.*` webhooks and returned by the list endpoint. The call must belong
        to the authenticated partner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_voice_id:
            raise ValueError(f"Expected a non-empty value for `call_voice_id` but received {call_voice_id!r}")
        return self._get(
            path_template("/v3/call-voice/{call_voice_id}", call_voice_id=call_voice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallVoiceRecord,
        )

    def list(
        self,
        phone_number: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallVoiceListResponse:
        """
        List the carrier voice calls received on one of your phone numbers, newest
        first, with cursor pagination. Each record is the durable form of the
        `call_voice.*` webhooks for that call; the `id` is the same id those webhooks
        carry. Results are scoped to the authenticated partner — a number that isn't
        yours (or simply has no calls) returns `200` with an empty `call_voice` array,
        not an error.

        Args:
          cursor: Pagination cursor from a previous next_cursor response

          limit: Maximum number of calls to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template("/v3/phone-numbers/{phone_number}/call-voice", phone_number=phone_number),
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
                    call_voice_list_params.CallVoiceListParams,
                ),
            ),
            cast_to=CallVoiceListResponse,
        )


class AsyncCallVoiceResource(AsyncAPIResource):
    """Read the carrier (BYOC) voice calls received on your phone numbers.

    Each
    record is the durable form of the `call_voice.*` webhooks for that call and
    shares the same `id`, so you can look a call up by the id a webhook
    delivered. See SIP Profiles for routing inbound calls to your endpoint.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCallVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncCallVoiceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        call_voice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallVoiceRecord:
        """
        Retrieve a single carrier voice call by its `id` — the same id delivered in the
        `call_voice.*` webhooks and returned by the list endpoint. The call must belong
        to the authenticated partner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_voice_id:
            raise ValueError(f"Expected a non-empty value for `call_voice_id` but received {call_voice_id!r}")
        return await self._get(
            path_template("/v3/call-voice/{call_voice_id}", call_voice_id=call_voice_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallVoiceRecord,
        )

    async def list(
        self,
        phone_number: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallVoiceListResponse:
        """
        List the carrier voice calls received on one of your phone numbers, newest
        first, with cursor pagination. Each record is the durable form of the
        `call_voice.*` webhooks for that call; the `id` is the same id those webhooks
        carry. Results are scoped to the authenticated partner — a number that isn't
        yours (or simply has no calls) returns `200` with an empty `call_voice` array,
        not an error.

        Args:
          cursor: Pagination cursor from a previous next_cursor response

          limit: Maximum number of calls to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template("/v3/phone-numbers/{phone_number}/call-voice", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    call_voice_list_params.CallVoiceListParams,
                ),
            ),
            cast_to=CallVoiceListResponse,
        )


class CallVoiceResourceWithRawResponse:
    def __init__(self, call_voice: CallVoiceResource) -> None:
        self._call_voice = call_voice

        self.retrieve = to_raw_response_wrapper(
            call_voice.retrieve,
        )
        self.list = to_raw_response_wrapper(
            call_voice.list,
        )


class AsyncCallVoiceResourceWithRawResponse:
    def __init__(self, call_voice: AsyncCallVoiceResource) -> None:
        self._call_voice = call_voice

        self.retrieve = async_to_raw_response_wrapper(
            call_voice.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            call_voice.list,
        )


class CallVoiceResourceWithStreamingResponse:
    def __init__(self, call_voice: CallVoiceResource) -> None:
        self._call_voice = call_voice

        self.retrieve = to_streamed_response_wrapper(
            call_voice.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            call_voice.list,
        )


class AsyncCallVoiceResourceWithStreamingResponse:
    def __init__(self, call_voice: AsyncCallVoiceResource) -> None:
        self._call_voice = call_voice

        self.retrieve = async_to_streamed_response_wrapper(
            call_voice.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            call_voice.list,
        )
