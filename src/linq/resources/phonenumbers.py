# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

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
from ..types.phonenumber_list_response import PhonenumberListResponse

__all__ = ["PhonenumbersResource", "AsyncPhonenumbersResource"]


class PhonenumbersResource(SyncAPIResource):
    """Phone Numbers represent the phone numbers assigned to your partner account.

    Use the list phone numbers endpoint to discover which phone numbers are available
    for sending messages.

    When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
    in the `from` field.
    """

    @cached_property
    def with_raw_response(self) -> PhonenumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return PhonenumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhonenumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return PhonenumbersResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhonenumberListResponse:
        """**Deprecated.** Use `GET /v3/phone_numbers` instead."""
        return self._get(
            "/v3/phonenumbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhonenumberListResponse,
        )


class AsyncPhonenumbersResource(AsyncAPIResource):
    """Phone Numbers represent the phone numbers assigned to your partner account.

    Use the list phone numbers endpoint to discover which phone numbers are available
    for sending messages.

    When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
    in the `from` field.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPhonenumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhonenumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhonenumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncPhonenumbersResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhonenumberListResponse:
        """**Deprecated.** Use `GET /v3/phone_numbers` instead."""
        return await self._get(
            "/v3/phonenumbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhonenumberListResponse,
        )


class PhonenumbersResourceWithRawResponse:
    def __init__(self, phonenumbers: PhonenumbersResource) -> None:
        self._phonenumbers = phonenumbers

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                phonenumbers.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncPhonenumbersResourceWithRawResponse:
    def __init__(self, phonenumbers: AsyncPhonenumbersResource) -> None:
        self._phonenumbers = phonenumbers

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                phonenumbers.list,  # pyright: ignore[reportDeprecated],
            )
        )


class PhonenumbersResourceWithStreamingResponse:
    def __init__(self, phonenumbers: PhonenumbersResource) -> None:
        self._phonenumbers = phonenumbers

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                phonenumbers.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncPhonenumbersResourceWithStreamingResponse:
    def __init__(self, phonenumbers: AsyncPhonenumbersResource) -> None:
        self._phonenumbers = phonenumbers

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                phonenumbers.list,  # pyright: ignore[reportDeprecated],
            )
        )
