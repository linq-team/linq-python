# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.experience_list_response import ExperienceListResponse
from ..types.experience_retrieve_response import ExperienceRetrieveResponse

__all__ = ["ExperiencesResource", "AsyncExperiencesResource"]


class ExperiencesResource(SyncAPIResource):
    """
    Let an agent pay on a customer's behalf with a single-use virtual card.
    Connect a customer once, then create a payment — a virtual card is minted
    scoped to that purchase and the card details are handed back for checkout.
    """

    @cached_property
    def with_raw_response(self) -> ExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return ExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return ExperiencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        experience: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExperienceRetrieveResponse:
        """
        Get one experience

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience:
            raise ValueError(f"Expected a non-empty value for `experience` but received {experience!r}")
        return self._get(
            path_template("/v3/experiences/{experience}", experience=experience),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceRetrieveResponse,
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
    ) -> ExperienceListResponse:
        """
        The experiences enabled for your account, with the actions you may invoke on
        each and the fields each action accepts. This is the authoritative list — an
        action missing here cannot be sent.
        """
        return self._get(
            "/v3/experiences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceListResponse,
        )


class AsyncExperiencesResource(AsyncAPIResource):
    """
    Let an agent pay on a customer's behalf with a single-use virtual card.
    Connect a customer once, then create a payment — a virtual card is minted
    scoped to that purchase and the card details are handed back for checkout.
    """

    @cached_property
    def with_raw_response(self) -> AsyncExperiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExperiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncExperiencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        experience: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExperienceRetrieveResponse:
        """
        Get one experience

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experience:
            raise ValueError(f"Expected a non-empty value for `experience` but received {experience!r}")
        return await self._get(
            path_template("/v3/experiences/{experience}", experience=experience),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceRetrieveResponse,
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
    ) -> ExperienceListResponse:
        """
        The experiences enabled for your account, with the actions you may invoke on
        each and the fields each action accepts. This is the authoritative list — an
        action missing here cannot be sent.
        """
        return await self._get(
            "/v3/experiences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperienceListResponse,
        )


class ExperiencesResourceWithRawResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.retrieve = to_raw_response_wrapper(
            experiences.retrieve,
        )
        self.list = to_raw_response_wrapper(
            experiences.list,
        )


class AsyncExperiencesResourceWithRawResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.retrieve = async_to_raw_response_wrapper(
            experiences.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            experiences.list,
        )


class ExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: ExperiencesResource) -> None:
        self._experiences = experiences

        self.retrieve = to_streamed_response_wrapper(
            experiences.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            experiences.list,
        )


class AsyncExperiencesResourceWithStreamingResponse:
    def __init__(self, experiences: AsyncExperiencesResource) -> None:
        self._experiences = experiences

        self.retrieve = async_to_streamed_response_wrapper(
            experiences.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            experiences.list,
        )
