# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.chats.location_request_response import LocationRequestResponse
from ...types.chats.get_chat_location_response import GetChatLocationResponse

__all__ = ["LocationResource", "AsyncLocationResource"]


class LocationResource(SyncAPIResource):
    """
    Request a contact's location, retrieve location for contacts sharing with you,
    and subscribe to webhooks when someone starts or stops sharing.

    **Coordinates** are returned in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format:
    `[longitude, latitude]` or `[longitude, latitude, altitude]` if altitude is available.

    ### Reading location is poll-based

    Poll `GET /v3/chats/{chatId}/location` whenever you need the latest position.
    **There is no webhook that pushes updated coordinates** — the
    `location.sharing.started` / `location.sharing.stopped` webhooks fire only when a
    contact begins or ends sharing, not on each position update. To track a moving
    contact, poll the `GET` endpoint.

    ### Freshness

    Each feature's `properties.updated_at` tells you when that participant's
    location was last updated — use it to judge freshness.

    ### Polling guidance

    Locations refresh on Apple's cadence, not per request — polling faster than a
    participant's location actually updates just returns the same position. Poll at a
    modest interval (for example, once every few minutes per chat) rather than
    continuously.

    ### Why is location empty after `location.sharing.started` fired?

    If the contact started sharing from the **standalone Find My app** instead of the
    Messages conversation, the share may be tied to their **Apple ID email** rather
    than their phone number — the webhook's `shared_by` field shows the email in that
    case. Location is readable only through a chat with the handle that shared, so
    `GET /v3/chats/{chatId}/location` on the phone-number chat stays empty.

    The fix: have the contact stop sharing and re-share from **Find My inside the
    Messages conversation** with your number.
    """

    @cached_property
    def with_raw_response(self) -> LocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return LocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return LocationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetChatLocationResponse:
        """
        Retrieve the current location for contacts sharing with you in a chat.

        The response is wrapped in the standard `{ "success": true, "data": ... }`
        envelope — the body is **not** a bare GeoJSON document. `data` is a
        [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) `FeatureCollection`
        with a `Feature` for each participant actively sharing their location.

        Works for both 1:1 and group chats. In group chats, `data.features` contains a
        separate feature for each participant who is sharing. Each feature's
        `properties.handle` identifies the user.

        Returns an empty `data.features` array if no one is sharing or no location data
        is available yet. If sharing started but this stays empty, see the **Location
        Sharing** overview.

        Poll this endpoint to track a moving contact. `properties.updated_at` reflects
        when each participant's location was last updated. There is no coordinate-update
        webhook. See the **Location Sharing** overview for polling guidance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return self._get(
            path_template("/v3/chats/{chat_id}/location", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetChatLocationResponse,
        )

    def request(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationRequestResponse:
        """Request a contact in a chat to share their location.

        They receive an iMessage
        prompt and must accept before any location is available; once they do, read
        their location coordinates with `GET /v3/chats/{chatId}/location`.

        The request is delivered asynchronously. The endpoint returns immediately with
        `{ "success": true, "message": "Location request sent" }` and does not return
        coordinates.

        Location requests only work in **1:1 iMessage chats** (Apple limitation):

        - Group chats (any service) return `409` with code `2016`
          (`GroupChatNotSupported`).
        - 1:1 SMS and RCS chats return `409` with code `2017`
          (`ChatServiceNotSupported`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v3/chats/{chat_id}/location/request", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationRequestResponse,
        )


class AsyncLocationResource(AsyncAPIResource):
    """
    Request a contact's location, retrieve location for contacts sharing with you,
    and subscribe to webhooks when someone starts or stops sharing.

    **Coordinates** are returned in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format:
    `[longitude, latitude]` or `[longitude, latitude, altitude]` if altitude is available.

    ### Reading location is poll-based

    Poll `GET /v3/chats/{chatId}/location` whenever you need the latest position.
    **There is no webhook that pushes updated coordinates** — the
    `location.sharing.started` / `location.sharing.stopped` webhooks fire only when a
    contact begins or ends sharing, not on each position update. To track a moving
    contact, poll the `GET` endpoint.

    ### Freshness

    Each feature's `properties.updated_at` tells you when that participant's
    location was last updated — use it to judge freshness.

    ### Polling guidance

    Locations refresh on Apple's cadence, not per request — polling faster than a
    participant's location actually updates just returns the same position. Poll at a
    modest interval (for example, once every few minutes per chat) rather than
    continuously.

    ### Why is location empty after `location.sharing.started` fired?

    If the contact started sharing from the **standalone Find My app** instead of the
    Messages conversation, the share may be tied to their **Apple ID email** rather
    than their phone number — the webhook's `shared_by` field shows the email in that
    case. Location is readable only through a chat with the handle that shared, so
    `GET /v3/chats/{chatId}/location` on the phone-number chat stays empty.

    The fix: have the contact stop sharing and re-share from **Find My inside the
    Messages conversation** with your number.
    """

    @cached_property
    def with_raw_response(self) -> AsyncLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncLocationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetChatLocationResponse:
        """
        Retrieve the current location for contacts sharing with you in a chat.

        The response is wrapped in the standard `{ "success": true, "data": ... }`
        envelope — the body is **not** a bare GeoJSON document. `data` is a
        [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) `FeatureCollection`
        with a `Feature` for each participant actively sharing their location.

        Works for both 1:1 and group chats. In group chats, `data.features` contains a
        separate feature for each participant who is sharing. Each feature's
        `properties.handle` identifies the user.

        Returns an empty `data.features` array if no one is sharing or no location data
        is available yet. If sharing started but this stays empty, see the **Location
        Sharing** overview.

        Poll this endpoint to track a moving contact. `properties.updated_at` reflects
        when each participant's location was last updated. There is no coordinate-update
        webhook. See the **Location Sharing** overview for polling guidance.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "application/geo+json", **(extra_headers or {})}
        return await self._get(
            path_template("/v3/chats/{chat_id}/location", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetChatLocationResponse,
        )

    async def request(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationRequestResponse:
        """Request a contact in a chat to share their location.

        They receive an iMessage
        prompt and must accept before any location is available; once they do, read
        their location coordinates with `GET /v3/chats/{chatId}/location`.

        The request is delivered asynchronously. The endpoint returns immediately with
        `{ "success": true, "message": "Location request sent" }` and does not return
        coordinates.

        Location requests only work in **1:1 iMessage chats** (Apple limitation):

        - Group chats (any service) return `409` with code `2016`
          (`GroupChatNotSupported`).
        - 1:1 SMS and RCS chats return `409` with code `2017`
          (`ChatServiceNotSupported`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v3/chats/{chat_id}/location/request", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationRequestResponse,
        )


class LocationResourceWithRawResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

        self.retrieve = to_raw_response_wrapper(
            location.retrieve,
        )
        self.request = to_raw_response_wrapper(
            location.request,
        )


class AsyncLocationResourceWithRawResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

        self.retrieve = async_to_raw_response_wrapper(
            location.retrieve,
        )
        self.request = async_to_raw_response_wrapper(
            location.request,
        )


class LocationResourceWithStreamingResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

        self.retrieve = to_streamed_response_wrapper(
            location.retrieve,
        )
        self.request = to_streamed_response_wrapper(
            location.request,
        )


class AsyncLocationResourceWithStreamingResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

        self.retrieve = async_to_streamed_response_wrapper(
            location.retrieve,
        )
        self.request = async_to_streamed_response_wrapper(
            location.request,
        )
