# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import capability_check_RCS_params, capability_check_i_message_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.handle_check_response import HandleCheckResponse

__all__ = ["CapabilityResource", "AsyncCapabilityResource"]


class CapabilityResource(SyncAPIResource):
    """
    Check whether a recipient address supports iMessage or RCS before sending a message.
    """

    @cached_property
    def with_raw_response(self) -> CapabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return CapabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return CapabilityResourceWithStreamingResponse(self)

    def check_i_message(
        self,
        *,
        address: str,
        from_: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HandleCheckResponse:
        """
        Check whether a recipient address (phone number or email) is reachable via
        iMessage.

        Args:
          address: The recipient address to check. `check_imessage` accepts an E.164 phone number
              or an email address; `check_rcs` accepts an E.164 phone number only and rejects
              an email with a `400`, since RCS has no email addressing.

          from_: Optional sender phone number. If omitted, an available phone from your pool is
              used automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/capability/check_imessage",
            body=maybe_transform(
                {
                    "address": address,
                    "from_": from_,
                },
                capability_check_i_message_params.CapabilityCheckIMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HandleCheckResponse,
        )

    def check_RCS(
        self,
        *,
        address: str,
        from_: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HandleCheckResponse:
        """
        Check whether a recipient address (phone number) supports RCS messaging.

        `address` must be an E.164 phone number. RCS has no email addressing, so an
        email is rejected with a `400` rather than attempted.

        A `200` means the check ran and the answer is about the **recipient**. A `503`
        means the check could not produce an answer because of a fault on the **sender**
        line — `4004` (RCS not turned on for the line), `4009` (line has no RCS
        account), or `4010` (the check could not run). Treat all three as "unknown",
        never as "the recipient does not support RCS", and do not cache them as a
        negative result.

        Args:
          address: The recipient address to check. `check_imessage` accepts an E.164 phone number
              or an email address; `check_rcs` accepts an E.164 phone number only and rejects
              an email with a `400`, since RCS has no email addressing.

          from_: Optional sender phone number. If omitted, an available phone from your pool is
              used automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/capability/check_rcs",
            body=maybe_transform(
                {
                    "address": address,
                    "from_": from_,
                },
                capability_check_RCS_params.CapabilityCheckRCSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HandleCheckResponse,
        )


class AsyncCapabilityResource(AsyncAPIResource):
    """
    Check whether a recipient address supports iMessage or RCS before sending a message.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCapabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCapabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncCapabilityResourceWithStreamingResponse(self)

    async def check_i_message(
        self,
        *,
        address: str,
        from_: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HandleCheckResponse:
        """
        Check whether a recipient address (phone number or email) is reachable via
        iMessage.

        Args:
          address: The recipient address to check. `check_imessage` accepts an E.164 phone number
              or an email address; `check_rcs` accepts an E.164 phone number only and rejects
              an email with a `400`, since RCS has no email addressing.

          from_: Optional sender phone number. If omitted, an available phone from your pool is
              used automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/capability/check_imessage",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "from_": from_,
                },
                capability_check_i_message_params.CapabilityCheckIMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HandleCheckResponse,
        )

    async def check_RCS(
        self,
        *,
        address: str,
        from_: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HandleCheckResponse:
        """
        Check whether a recipient address (phone number) supports RCS messaging.

        `address` must be an E.164 phone number. RCS has no email addressing, so an
        email is rejected with a `400` rather than attempted.

        A `200` means the check ran and the answer is about the **recipient**. A `503`
        means the check could not produce an answer because of a fault on the **sender**
        line — `4004` (RCS not turned on for the line), `4009` (line has no RCS
        account), or `4010` (the check could not run). Treat all three as "unknown",
        never as "the recipient does not support RCS", and do not cache them as a
        negative result.

        Args:
          address: The recipient address to check. `check_imessage` accepts an E.164 phone number
              or an email address; `check_rcs` accepts an E.164 phone number only and rejects
              an email with a `400`, since RCS has no email addressing.

          from_: Optional sender phone number. If omitted, an available phone from your pool is
              used automatically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/capability/check_rcs",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "from_": from_,
                },
                capability_check_RCS_params.CapabilityCheckRCSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HandleCheckResponse,
        )


class CapabilityResourceWithRawResponse:
    def __init__(self, capability: CapabilityResource) -> None:
        self._capability = capability

        self.check_i_message = to_raw_response_wrapper(
            capability.check_i_message,
        )
        self.check_RCS = to_raw_response_wrapper(
            capability.check_RCS,
        )


class AsyncCapabilityResourceWithRawResponse:
    def __init__(self, capability: AsyncCapabilityResource) -> None:
        self._capability = capability

        self.check_i_message = async_to_raw_response_wrapper(
            capability.check_i_message,
        )
        self.check_RCS = async_to_raw_response_wrapper(
            capability.check_RCS,
        )


class CapabilityResourceWithStreamingResponse:
    def __init__(self, capability: CapabilityResource) -> None:
        self._capability = capability

        self.check_i_message = to_streamed_response_wrapper(
            capability.check_i_message,
        )
        self.check_RCS = to_streamed_response_wrapper(
            capability.check_RCS,
        )


class AsyncCapabilityResourceWithStreamingResponse:
    def __init__(self, capability: AsyncCapabilityResource) -> None:
        self._capability = capability

        self.check_i_message = async_to_streamed_response_wrapper(
            capability.check_i_message,
        )
        self.check_RCS = async_to_streamed_response_wrapper(
            capability.check_RCS,
        )
