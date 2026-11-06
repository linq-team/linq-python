# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import sip_profile_assign_params, sip_profile_create_params, sip_profile_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.sip_profile import SipProfile
from ..types.sip_profile_list_response import SipProfileListResponse
from ..types.sip_profile_assign_response import SipProfileAssignResponse

__all__ = ["SipProfilesResource", "AsyncSipProfilesResource"]


class SipProfilesResource(SyncAPIResource):
    """## SIP configuration

    Your Linq representative provides the signaling and media IP ranges and
    ports to allow through your firewall during onboarding.

    Set `primary_uri` to your endpoint as scheme + host — `sips:` for TLS or
    `sip:` for UDP, with no user part (we add it). Each call arrives at your
    endpoint as:

    ```
    sip:<called-number>@<your-host>
    ```

    so you can route on the dialed number. The caller's number is in the
    `From` header in E.164.
    """

    @cached_property
    def with_raw_response(self) -> SipProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return SipProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SipProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return SipProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        primary_uri: str,
        backup_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfile:
        """
        ## SIP configuration

        Your Linq representative provides the signaling and media IP ranges and ports to
        allow through your firewall during onboarding.

        Set `primary_uri` to your endpoint as scheme + host — `sips:` for TLS or `sip:`
        for UDP, with no user part (we add it). Each call arrives at your endpoint as:

        ```
        sip:<called-number>@<your-host>
        ```

        so you can route on the dialed number. The caller's number is in the `From`
        header in E.164.

        ---

        Create a SIP routing profile for your inbound calls, then assign it to a phone
        number to start routing calls to its SIP URI.

        Args:
          primary_uri: Your SIP endpoint as scheme + host, e.g. `sips:sip.partner.example`. Must start
              with `sip:` (UDP) or `sips:` (TLS) — the scheme sets the transport. Do not
              include a user part: we set it to the called number on each call
              (`sip:<called-number>@<your-host>`). A bare host with no scheme is rejected.

          backup_uri: Optional failover SIP URI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/sip-profiles",
            body=maybe_transform(
                {
                    "name": name,
                    "primary_uri": primary_uri,
                    "backup_uri": backup_uri,
                },
                sip_profile_create_params.SipProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfile,
        )

    def retrieve(
        self,
        sip_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfile:
        """
        Retrieve details for a specific SIP profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sip_profile_id:
            raise ValueError(f"Expected a non-empty value for `sip_profile_id` but received {sip_profile_id!r}")
        return self._get(
            path_template("/v3/sip-profiles/{sip_profile_id}", sip_profile_id=sip_profile_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfile,
        )

    def update(
        self,
        sip_profile_id: str,
        *,
        backup_uri: str | Omit = omit,
        name: str | Omit = omit,
        primary_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfile:
        """Update a SIP profile.

        Only the fields you send are changed; omitted fields keep
        their current value. Set `backup_uri` to an empty string to clear it.

        Args:
          backup_uri: Set to "" to clear the backup URI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sip_profile_id:
            raise ValueError(f"Expected a non-empty value for `sip_profile_id` but received {sip_profile_id!r}")
        return self._put(
            path_template("/v3/sip-profiles/{sip_profile_id}", sip_profile_id=sip_profile_id),
            body=maybe_transform(
                {
                    "backup_uri": backup_uri,
                    "name": name,
                    "primary_uri": primary_uri,
                },
                sip_profile_update_params.SipProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfile,
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
    ) -> SipProfileListResponse:
        """Retrieve all SIP profiles for the authenticated partner."""
        return self._get(
            "/v3/sip-profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfileListResponse,
        )

    def delete(
        self,
        sip_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a SIP profile.

        The profile must not be assigned to any phone number;
        unassign it first or the request is rejected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sip_profile_id:
            raise ValueError(f"Expected a non-empty value for `sip_profile_id` but received {sip_profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/sip-profiles/{sip_profile_id}", sip_profile_id=sip_profile_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def assign(
        self,
        phone_number: str,
        *,
        sip_profile_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfileAssignResponse:
        """
        ## SIP configuration

        Your Linq representative provides the signaling and media IP ranges and ports to
        allow through your firewall during onboarding.

        Set `primary_uri` to your endpoint as scheme + host — `sips:` for TLS or `sip:`
        for UDP, with no user part (we add it). Each call arrives at your endpoint as:

        ```
        sip:<called-number>@<your-host>
        ```

        so you can route on the dialed number. The caller's number is in the `From`
        header in E.164.

        ---

        Assign a SIP profile to route inbound calls to its SIP URI. This takes
        precedence over an existing `forwarding_number` without clearing it. Send
        `sip_profile_id: null` to remove the SIP assignment and resume existing
        forwarding, if configured. Allow about 5 minutes for routing changes to
        propagate. The phone number must belong to the authenticated partner.

        Args:
          sip_profile_id: The SIP profile to assign, or null to clear the number's current assignment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._put(
            path_template("/v3/phone-numbers/{phone_number}/sip-profile", phone_number=phone_number),
            body=maybe_transform({"sip_profile_id": sip_profile_id}, sip_profile_assign_params.SipProfileAssignParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfileAssignResponse,
        )


class AsyncSipProfilesResource(AsyncAPIResource):
    """## SIP configuration

    Your Linq representative provides the signaling and media IP ranges and
    ports to allow through your firewall during onboarding.

    Set `primary_uri` to your endpoint as scheme + host — `sips:` for TLS or
    `sip:` for UDP, with no user part (we add it). Each call arrives at your
    endpoint as:

    ```
    sip:<called-number>@<your-host>
    ```

    so you can route on the dialed number. The caller's number is in the
    `From` header in E.164.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSipProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSipProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSipProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncSipProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        primary_uri: str,
        backup_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfile:
        """
        ## SIP configuration

        Your Linq representative provides the signaling and media IP ranges and ports to
        allow through your firewall during onboarding.

        Set `primary_uri` to your endpoint as scheme + host — `sips:` for TLS or `sip:`
        for UDP, with no user part (we add it). Each call arrives at your endpoint as:

        ```
        sip:<called-number>@<your-host>
        ```

        so you can route on the dialed number. The caller's number is in the `From`
        header in E.164.

        ---

        Create a SIP routing profile for your inbound calls, then assign it to a phone
        number to start routing calls to its SIP URI.

        Args:
          primary_uri: Your SIP endpoint as scheme + host, e.g. `sips:sip.partner.example`. Must start
              with `sip:` (UDP) or `sips:` (TLS) — the scheme sets the transport. Do not
              include a user part: we set it to the called number on each call
              (`sip:<called-number>@<your-host>`). A bare host with no scheme is rejected.

          backup_uri: Optional failover SIP URI

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/sip-profiles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "primary_uri": primary_uri,
                    "backup_uri": backup_uri,
                },
                sip_profile_create_params.SipProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfile,
        )

    async def retrieve(
        self,
        sip_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfile:
        """
        Retrieve details for a specific SIP profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sip_profile_id:
            raise ValueError(f"Expected a non-empty value for `sip_profile_id` but received {sip_profile_id!r}")
        return await self._get(
            path_template("/v3/sip-profiles/{sip_profile_id}", sip_profile_id=sip_profile_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfile,
        )

    async def update(
        self,
        sip_profile_id: str,
        *,
        backup_uri: str | Omit = omit,
        name: str | Omit = omit,
        primary_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfile:
        """Update a SIP profile.

        Only the fields you send are changed; omitted fields keep
        their current value. Set `backup_uri` to an empty string to clear it.

        Args:
          backup_uri: Set to "" to clear the backup URI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sip_profile_id:
            raise ValueError(f"Expected a non-empty value for `sip_profile_id` but received {sip_profile_id!r}")
        return await self._put(
            path_template("/v3/sip-profiles/{sip_profile_id}", sip_profile_id=sip_profile_id),
            body=await async_maybe_transform(
                {
                    "backup_uri": backup_uri,
                    "name": name,
                    "primary_uri": primary_uri,
                },
                sip_profile_update_params.SipProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfile,
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
    ) -> SipProfileListResponse:
        """Retrieve all SIP profiles for the authenticated partner."""
        return await self._get(
            "/v3/sip-profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfileListResponse,
        )

    async def delete(
        self,
        sip_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a SIP profile.

        The profile must not be assigned to any phone number;
        unassign it first or the request is rejected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sip_profile_id:
            raise ValueError(f"Expected a non-empty value for `sip_profile_id` but received {sip_profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/sip-profiles/{sip_profile_id}", sip_profile_id=sip_profile_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def assign(
        self,
        phone_number: str,
        *,
        sip_profile_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipProfileAssignResponse:
        """
        ## SIP configuration

        Your Linq representative provides the signaling and media IP ranges and ports to
        allow through your firewall during onboarding.

        Set `primary_uri` to your endpoint as scheme + host — `sips:` for TLS or `sip:`
        for UDP, with no user part (we add it). Each call arrives at your endpoint as:

        ```
        sip:<called-number>@<your-host>
        ```

        so you can route on the dialed number. The caller's number is in the `From`
        header in E.164.

        ---

        Assign a SIP profile to route inbound calls to its SIP URI. This takes
        precedence over an existing `forwarding_number` without clearing it. Send
        `sip_profile_id: null` to remove the SIP assignment and resume existing
        forwarding, if configured. Allow about 5 minutes for routing changes to
        propagate. The phone number must belong to the authenticated partner.

        Args:
          sip_profile_id: The SIP profile to assign, or null to clear the number's current assignment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._put(
            path_template("/v3/phone-numbers/{phone_number}/sip-profile", phone_number=phone_number),
            body=await async_maybe_transform(
                {"sip_profile_id": sip_profile_id}, sip_profile_assign_params.SipProfileAssignParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipProfileAssignResponse,
        )


class SipProfilesResourceWithRawResponse:
    def __init__(self, sip_profiles: SipProfilesResource) -> None:
        self._sip_profiles = sip_profiles

        self.create = to_raw_response_wrapper(
            sip_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sip_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sip_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            sip_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            sip_profiles.delete,
        )
        self.assign = to_raw_response_wrapper(
            sip_profiles.assign,
        )


class AsyncSipProfilesResourceWithRawResponse:
    def __init__(self, sip_profiles: AsyncSipProfilesResource) -> None:
        self._sip_profiles = sip_profiles

        self.create = async_to_raw_response_wrapper(
            sip_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sip_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sip_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            sip_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sip_profiles.delete,
        )
        self.assign = async_to_raw_response_wrapper(
            sip_profiles.assign,
        )


class SipProfilesResourceWithStreamingResponse:
    def __init__(self, sip_profiles: SipProfilesResource) -> None:
        self._sip_profiles = sip_profiles

        self.create = to_streamed_response_wrapper(
            sip_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sip_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sip_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            sip_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            sip_profiles.delete,
        )
        self.assign = to_streamed_response_wrapper(
            sip_profiles.assign,
        )


class AsyncSipProfilesResourceWithStreamingResponse:
    def __init__(self, sip_profiles: AsyncSipProfilesResource) -> None:
        self._sip_profiles = sip_profiles

        self.create = async_to_streamed_response_wrapper(
            sip_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sip_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sip_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sip_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sip_profiles.delete,
        )
        self.assign = async_to_streamed_response_wrapper(
            sip_profiles.assign,
        )
