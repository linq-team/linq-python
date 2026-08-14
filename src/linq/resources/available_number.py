# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import available_number_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.available_number_retrieve_response import AvailableNumberRetrieveResponse

__all__ = ["AvailableNumberResource", "AsyncAvailableNumberResource"]


class AvailableNumberResource(SyncAPIResource):
    """Phone Numbers represent the phone numbers assigned to your partner account.

    Use the list phone numbers endpoint to discover which phone numbers are available
    for sending messages.

    When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
    in the `from` field.

    **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
    While it is in that state, requests that would produce new activity on it — sending a
    message, creating a chat, reacting, typing, group actions — are rejected with `403`
    (error code `2027`) before anything is created. Reads keep working, so your existing
    chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
    pick an eligible number for you, skipping ineligible ones; if none of your assigned
    numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
    specific number to blame with a `403`).
    """

    @cached_property
    def with_raw_response(self) -> AvailableNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AvailableNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AvailableNumberResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        exclude_from: SequenceNotStr[str] | Omit = omit,
        to: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvailableNumberRetrieveResponse:
        """
        Returns the best available line (E.164) to send from, applying smart number
        assignment. Optionally pass `to` recipients to make the choice "sticky" —
        reusing the line an existing chat with those recipients is already on. Without
        `to`, the best available line is chosen, always preferring lines with a
        healthier reputation.

        This does not reserve the line. Without `to`, the least-recently-used available
        line is returned — suggestions and your own sends (including an explicit `from`
        on chat creation) both count as use, so successive calls cycle through your
        available lines and traffic spreads evenly. Pass the returned `phone_number` as
        `from` when you create the chat to guarantee the same line.

        Also returns `vcf_url`: a time-limited link to a vCard (`.vcf`) for the chosen
        line, carrying its contact card (name/photo) with the chosen number as the
        primary `TEL` and the partner's other available lines as backups. Share it with
        recipients so they can save the line as a contact. Lines you pass in
        `exclude_from` are left out of the vCard too.

        Args:
          exclude_from: Lines (E.164) to leave out of this selection. Applies to the returned
              `phone_number`, to the sticky choice when `to` is given, and to the vCard's
              backup numbers. Repeat the parameter for multiple lines; use `%2B` for the
              leading `+`.

              Numbers that are not your lines are ignored. Every entry must be E.164 — a value
              like `4155551234` is rejected rather than silently skipped. Excluding every one
              of your available lines returns 400.

          to: Recipient handles (E.164 or email) the message is destined for. When provided,
              an existing chat with these recipients makes the choice sticky. Repeat the
              parameter for multiple recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/available_number",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_from": exclude_from,
                        "to": to,
                    },
                    available_number_retrieve_params.AvailableNumberRetrieveParams,
                ),
            ),
            cast_to=AvailableNumberRetrieveResponse,
        )


class AsyncAvailableNumberResource(AsyncAPIResource):
    """Phone Numbers represent the phone numbers assigned to your partner account.

    Use the list phone numbers endpoint to discover which phone numbers are available
    for sending messages.

    When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
    in the `from` field.

    **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
    While it is in that state, requests that would produce new activity on it — sending a
    message, creating a chat, reacting, typing, group actions — are rejected with `403`
    (error code `2027`) before anything is created. Reads keep working, so your existing
    chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
    pick an eligible number for you, skipping ineligible ones; if none of your assigned
    numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
    specific number to blame with a `403`).
    """

    @cached_property
    def with_raw_response(self) -> AsyncAvailableNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailableNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncAvailableNumberResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        exclude_from: SequenceNotStr[str] | Omit = omit,
        to: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvailableNumberRetrieveResponse:
        """
        Returns the best available line (E.164) to send from, applying smart number
        assignment. Optionally pass `to` recipients to make the choice "sticky" —
        reusing the line an existing chat with those recipients is already on. Without
        `to`, the best available line is chosen, always preferring lines with a
        healthier reputation.

        This does not reserve the line. Without `to`, the least-recently-used available
        line is returned — suggestions and your own sends (including an explicit `from`
        on chat creation) both count as use, so successive calls cycle through your
        available lines and traffic spreads evenly. Pass the returned `phone_number` as
        `from` when you create the chat to guarantee the same line.

        Also returns `vcf_url`: a time-limited link to a vCard (`.vcf`) for the chosen
        line, carrying its contact card (name/photo) with the chosen number as the
        primary `TEL` and the partner's other available lines as backups. Share it with
        recipients so they can save the line as a contact. Lines you pass in
        `exclude_from` are left out of the vCard too.

        Args:
          exclude_from: Lines (E.164) to leave out of this selection. Applies to the returned
              `phone_number`, to the sticky choice when `to` is given, and to the vCard's
              backup numbers. Repeat the parameter for multiple lines; use `%2B` for the
              leading `+`.

              Numbers that are not your lines are ignored. Every entry must be E.164 — a value
              like `4155551234` is rejected rather than silently skipped. Excluding every one
              of your available lines returns 400.

          to: Recipient handles (E.164 or email) the message is destined for. When provided,
              an existing chat with these recipients makes the choice sticky. Repeat the
              parameter for multiple recipients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/available_number",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude_from": exclude_from,
                        "to": to,
                    },
                    available_number_retrieve_params.AvailableNumberRetrieveParams,
                ),
            ),
            cast_to=AvailableNumberRetrieveResponse,
        )


class AvailableNumberResourceWithRawResponse:
    def __init__(self, available_number: AvailableNumberResource) -> None:
        self._available_number = available_number

        self.retrieve = to_raw_response_wrapper(
            available_number.retrieve,
        )


class AsyncAvailableNumberResourceWithRawResponse:
    def __init__(self, available_number: AsyncAvailableNumberResource) -> None:
        self._available_number = available_number

        self.retrieve = async_to_raw_response_wrapper(
            available_number.retrieve,
        )


class AvailableNumberResourceWithStreamingResponse:
    def __init__(self, available_number: AvailableNumberResource) -> None:
        self._available_number = available_number

        self.retrieve = to_streamed_response_wrapper(
            available_number.retrieve,
        )


class AsyncAvailableNumberResourceWithStreamingResponse:
    def __init__(self, available_number: AsyncAvailableNumberResource) -> None:
        self._available_number = available_number

        self.retrieve = async_to_streamed_response_wrapper(
            available_number.retrieve,
        )
