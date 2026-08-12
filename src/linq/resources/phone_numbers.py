# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import phone_number_update_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.reputation_audit import ReputationAudit
from ..types.reputation_audit_started import ReputationAuditStarted
from ..types.phone_number_list_response import PhoneNumberListResponse
from ..types.phone_number_update_response import PhoneNumberUpdateResponse

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    """Phone Numbers represent the phone numbers assigned to your partner account.

    Use the list phone numbers endpoint to discover which phone numbers are available
    for sending messages.

    When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
    in the `from` field.
    """

    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

    def update(
        self,
        phone_number_id: str,
        *,
        forwarding_number: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberUpdateResponse:
        """Updates the forwarding number for a phone number.

        The forwarding number is where
        inbound calls will be forwarded to.

        Pass an empty string to clear the forwarding number.

        Args:
          forwarding_number: The forwarding number in E.164 format. Set to null or empty string to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._put(
            path_template("/v3/phone_numbers/{phone_number_id}", phone_number_id=phone_number_id),
            body=maybe_transform(
                {"forwarding_number": forwarding_number}, phone_number_update_params.PhoneNumberUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
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
    ) -> PhoneNumberListResponse:
        """Returns all phone numbers assigned to the authenticated partner.

        Use this
        endpoint to discover which phone numbers are available for use as the `from`
        field when creating a chat, listing chats, or sending a voice memo.
        """
        return self._get(
            "/v3/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberListResponse,
        )

    def get_reputation_audit(
        self,
        audit_id: str,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationAudit:
        """Returns the audit's status and, once complete, the report.

        Audits are scoped to
        the line in the URL — an `auditId` started on a different line returns `404`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        return self._get(
            path_template(
                "/v3/phone_numbers/{phone_number}/reputation_audit/{audit_id}",
                phone_number=phone_number,
                audit_id=audit_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationAudit,
        )

    def start_reputation_audit(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationAuditStarted:
        """
        Starts an asynchronous reputation audit for a line and returns an `audit_id`.
        Poll the GET endpoint for the result.

        Rate limited per line: only one audit may run at a time (a second request
        returns `409` while the first is still in progress), and a new audit can't be
        started for the same line until a cooldown elapses (`429`, with `Retry-After`
        carrying the wait).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._post(
            path_template("/v3/phone_numbers/{phone_number}/reputation_audit", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationAuditStarted,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    """Phone Numbers represent the phone numbers assigned to your partner account.

    Use the list phone numbers endpoint to discover which phone numbers are available
    for sending messages.

    When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
    in the `from` field.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

    async def update(
        self,
        phone_number_id: str,
        *,
        forwarding_number: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberUpdateResponse:
        """Updates the forwarding number for a phone number.

        The forwarding number is where
        inbound calls will be forwarded to.

        Pass an empty string to clear the forwarding number.

        Args:
          forwarding_number: The forwarding number in E.164 format. Set to null or empty string to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._put(
            path_template("/v3/phone_numbers/{phone_number_id}", phone_number_id=phone_number_id),
            body=await async_maybe_transform(
                {"forwarding_number": forwarding_number}, phone_number_update_params.PhoneNumberUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
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
    ) -> PhoneNumberListResponse:
        """Returns all phone numbers assigned to the authenticated partner.

        Use this
        endpoint to discover which phone numbers are available for use as the `from`
        field when creating a chat, listing chats, or sending a voice memo.
        """
        return await self._get(
            "/v3/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberListResponse,
        )

    async def get_reputation_audit(
        self,
        audit_id: str,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationAudit:
        """Returns the audit's status and, once complete, the report.

        Audits are scoped to
        the line in the URL — an `auditId` started on a different line returns `404`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        return await self._get(
            path_template(
                "/v3/phone_numbers/{phone_number}/reputation_audit/{audit_id}",
                phone_number=phone_number,
                audit_id=audit_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationAudit,
        )

    async def start_reputation_audit(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationAuditStarted:
        """
        Starts an asynchronous reputation audit for a line and returns an `audit_id`.
        Poll the GET endpoint for the result.

        Rate limited per line: only one audit may run at a time (a second request
        returns `409` while the first is still in progress), and a new audit can't be
        started for the same line until a cooldown elapses (`429`, with `Retry-After`
        carrying the wait).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._post(
            path_template("/v3/phone_numbers/{phone_number}/reputation_audit", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationAuditStarted,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.update = to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.get_reputation_audit = to_raw_response_wrapper(
            phone_numbers.get_reputation_audit,
        )
        self.start_reputation_audit = to_raw_response_wrapper(
            phone_numbers.start_reputation_audit,
        )


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.update = async_to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.get_reputation_audit = async_to_raw_response_wrapper(
            phone_numbers.get_reputation_audit,
        )
        self.start_reputation_audit = async_to_raw_response_wrapper(
            phone_numbers.start_reputation_audit,
        )


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.update = to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.get_reputation_audit = to_streamed_response_wrapper(
            phone_numbers.get_reputation_audit,
        )
        self.start_reputation_audit = to_streamed_response_wrapper(
            phone_numbers.start_reputation_audit,
        )


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.update = async_to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.get_reputation_audit = async_to_streamed_response_wrapper(
            phone_numbers.get_reputation_audit,
        )
        self.start_reputation_audit = async_to_streamed_response_wrapper(
            phone_numbers.start_reputation_audit,
        )
