# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import contact_card_create_params, contact_card_update_params, contact_card_retrieve_params
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
from ..types.set_contact_card import SetContactCard
from ..types.contact_card_retrieve_response import ContactCardRetrieveResponse

__all__ = ["ContactCardResource", "AsyncContactCardResource"]


class ContactCardResource(SyncAPIResource):
    """
    Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

    Use `POST /v3/contact_card` to create or update a card for a phone number.
    Use `PATCH /v3/contact_card` to update an existing active card.
    Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

    **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
    """

    @cached_property
    def with_raw_response(self) -> ContactCardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return ContactCardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactCardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return ContactCardResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        first_name: str,
        phone_number: str,
        image_url: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetContactCard:
        """Creates a contact card for a phone number.

        This endpoint is intended for
        initial, one-time setup only.

        The contact card is stored in an inactive state first. Once it's applied
        successfully, it is activated and `is_active` is returned as `true`. On failure,
        `is_active` is `false`.

        **Note:** To update an existing contact card after setup, use
        `PATCH /v3/contact_card` instead.

        Args:
          first_name: First name for the contact card. Required.

          phone_number: E.164 phone number to associate the contact card with

          image_url: URL of the profile image to rehost on the CDN. Only re-uploaded when a new value
              is provided.

          last_name: Last name for the contact card. Optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/contact_card",
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "phone_number": phone_number,
                    "image_url": image_url,
                    "last_name": last_name,
                },
                contact_card_create_params.ContactCardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetContactCard,
        )

    def retrieve(
        self,
        *,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCardRetrieveResponse:
        """
        Returns the contact card for a specific phone number, or all contact cards for
        the authenticated partner if no `phone_number` is provided.

        Args:
          phone_number: E.164 phone number to filter by. If omitted, all my cards for the partner are
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/contact_card",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"phone_number": phone_number}, contact_card_retrieve_params.ContactCardRetrieveParams
                ),
            ),
            cast_to=ContactCardRetrieveResponse,
        )

    def update(
        self,
        *,
        phone_number: str,
        first_name: str | Omit = omit,
        image_url: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetContactCard:
        """
        Partially updates an existing active contact card for a phone number.

        Fetches the current active contact card and merges the provided fields. Only
        fields present in the request body are updated; omitted fields retain their
        existing values.

        Requires an active contact card to exist for the phone number.

        Args:
          phone_number: E.164 phone number of the contact card to update

          first_name: Updated first name. If omitted, the existing value is kept.

          image_url: Updated profile image URL. If omitted, the existing image is kept.

          last_name: Updated last name. If omitted, the existing value is kept.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v3/contact_card",
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "image_url": image_url,
                    "last_name": last_name,
                },
                contact_card_update_params.ContactCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"phone_number": phone_number}, contact_card_update_params.ContactCardUpdateParams
                ),
            ),
            cast_to=SetContactCard,
        )


class AsyncContactCardResource(AsyncAPIResource):
    """
    Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

    Use `POST /v3/contact_card` to create or update a card for a phone number.
    Use `PATCH /v3/contact_card` to update an existing active card.
    Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

    **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
    """

    @cached_property
    def with_raw_response(self) -> AsyncContactCardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactCardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactCardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncContactCardResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        first_name: str,
        phone_number: str,
        image_url: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetContactCard:
        """Creates a contact card for a phone number.

        This endpoint is intended for
        initial, one-time setup only.

        The contact card is stored in an inactive state first. Once it's applied
        successfully, it is activated and `is_active` is returned as `true`. On failure,
        `is_active` is `false`.

        **Note:** To update an existing contact card after setup, use
        `PATCH /v3/contact_card` instead.

        Args:
          first_name: First name for the contact card. Required.

          phone_number: E.164 phone number to associate the contact card with

          image_url: URL of the profile image to rehost on the CDN. Only re-uploaded when a new value
              is provided.

          last_name: Last name for the contact card. Optional.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/contact_card",
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "phone_number": phone_number,
                    "image_url": image_url,
                    "last_name": last_name,
                },
                contact_card_create_params.ContactCardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetContactCard,
        )

    async def retrieve(
        self,
        *,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCardRetrieveResponse:
        """
        Returns the contact card for a specific phone number, or all contact cards for
        the authenticated partner if no `phone_number` is provided.

        Args:
          phone_number: E.164 phone number to filter by. If omitted, all my cards for the partner are
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/contact_card",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"phone_number": phone_number}, contact_card_retrieve_params.ContactCardRetrieveParams
                ),
            ),
            cast_to=ContactCardRetrieveResponse,
        )

    async def update(
        self,
        *,
        phone_number: str,
        first_name: str | Omit = omit,
        image_url: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetContactCard:
        """
        Partially updates an existing active contact card for a phone number.

        Fetches the current active contact card and merges the provided fields. Only
        fields present in the request body are updated; omitted fields retain their
        existing values.

        Requires an active contact card to exist for the phone number.

        Args:
          phone_number: E.164 phone number of the contact card to update

          first_name: Updated first name. If omitted, the existing value is kept.

          image_url: Updated profile image URL. If omitted, the existing image is kept.

          last_name: Updated last name. If omitted, the existing value is kept.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v3/contact_card",
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "image_url": image_url,
                    "last_name": last_name,
                },
                contact_card_update_params.ContactCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"phone_number": phone_number}, contact_card_update_params.ContactCardUpdateParams
                ),
            ),
            cast_to=SetContactCard,
        )


class ContactCardResourceWithRawResponse:
    def __init__(self, contact_card: ContactCardResource) -> None:
        self._contact_card = contact_card

        self.create = to_raw_response_wrapper(
            contact_card.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contact_card.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contact_card.update,
        )


class AsyncContactCardResourceWithRawResponse:
    def __init__(self, contact_card: AsyncContactCardResource) -> None:
        self._contact_card = contact_card

        self.create = async_to_raw_response_wrapper(
            contact_card.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contact_card.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contact_card.update,
        )


class ContactCardResourceWithStreamingResponse:
    def __init__(self, contact_card: ContactCardResource) -> None:
        self._contact_card = contact_card

        self.create = to_streamed_response_wrapper(
            contact_card.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contact_card.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contact_card.update,
        )


class AsyncContactCardResourceWithStreamingResponse:
    def __init__(self, contact_card: AsyncContactCardResource) -> None:
        self._contact_card = contact_card

        self.create = async_to_streamed_response_wrapper(
            contact_card.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contact_card.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contact_card.update,
        )
