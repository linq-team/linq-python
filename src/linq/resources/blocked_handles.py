# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import blocked_handle_block_params, blocked_handle_unblock_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.blocked_handle_list_response import BlockedHandleListResponse
from ..types.blocked_handle_block_response import BlockedHandleBlockResponse

__all__ = ["BlockedHandlesResource", "AsyncBlockedHandlesResource"]


class BlockedHandlesResource(SyncAPIResource):
    """Block handles — phone numbers, email addresses, SMS short codes, or
    sender IDs.

    Inbound messages from a blocked handle are dropped before
    they reach your webhooks, and direct sends to a blocked handle are
    rejected with `403` (error code `2026`). Group sends that include
    unblocked members are not restricted.
    """

    @cached_property
    def with_raw_response(self) -> BlockedHandlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return BlockedHandlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockedHandlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return BlockedHandlesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedHandleListResponse:
        """Returns all handles you have blocked.

        Inbound messages from a blocked handle are
        dropped and produce no webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include unblocked
        members are not restricted.
        """
        return self._get(
            "/v3/blocked_handles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedHandleListResponse,
        )

    def block(
        self,
        *,
        handle: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedHandleBlockResponse:
        """
        Blocks a handle — an E.164 phone number, an email address (iMessage sender), an
        SMS short code (e.g. `262966`), or an alphanumeric sender ID. Inbound messages
        from it are dropped and produce no webhooks, and direct sends to it are rejected
        with `403` (error code `2026`); group sends that include unblocked members are
        not restricted. Blocking is idempotent — re-blocking an already blocked handle
        returns the existing entry.

        Args:
          handle: The handle to block: an E.164 phone number, an email address, an SMS short code
              (3-8 digits), or an alphanumeric sender ID.

          reason: Optional free-text note on why the handle was blocked

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/blocked_handles",
            body=maybe_transform(
                {
                    "handle": handle,
                    "reason": reason,
                },
                blocked_handle_block_params.BlockedHandleBlockParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedHandleBlockResponse,
        )

    def unblock(
        self,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a handle from your blocklist.

        Inbound messages from it will be delivered
        again and sends to it are allowed again. The handle goes in the request body,
        mirroring block — no URL encoding needed.

        Args:
          handle: The handle to unblock

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v3/blocked_handles",
            body=maybe_transform({"handle": handle}, blocked_handle_unblock_params.BlockedHandleUnblockParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBlockedHandlesResource(AsyncAPIResource):
    """Block handles — phone numbers, email addresses, SMS short codes, or
    sender IDs.

    Inbound messages from a blocked handle are dropped before
    they reach your webhooks, and direct sends to a blocked handle are
    rejected with `403` (error code `2026`). Group sends that include
    unblocked members are not restricted.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBlockedHandlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockedHandlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockedHandlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncBlockedHandlesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedHandleListResponse:
        """Returns all handles you have blocked.

        Inbound messages from a blocked handle are
        dropped and produce no webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include unblocked
        members are not restricted.
        """
        return await self._get(
            "/v3/blocked_handles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedHandleListResponse,
        )

    async def block(
        self,
        *,
        handle: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedHandleBlockResponse:
        """
        Blocks a handle — an E.164 phone number, an email address (iMessage sender), an
        SMS short code (e.g. `262966`), or an alphanumeric sender ID. Inbound messages
        from it are dropped and produce no webhooks, and direct sends to it are rejected
        with `403` (error code `2026`); group sends that include unblocked members are
        not restricted. Blocking is idempotent — re-blocking an already blocked handle
        returns the existing entry.

        Args:
          handle: The handle to block: an E.164 phone number, an email address, an SMS short code
              (3-8 digits), or an alphanumeric sender ID.

          reason: Optional free-text note on why the handle was blocked

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/blocked_handles",
            body=await async_maybe_transform(
                {
                    "handle": handle,
                    "reason": reason,
                },
                blocked_handle_block_params.BlockedHandleBlockParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedHandleBlockResponse,
        )

    async def unblock(
        self,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a handle from your blocklist.

        Inbound messages from it will be delivered
        again and sends to it are allowed again. The handle goes in the request body,
        mirroring block — no URL encoding needed.

        Args:
          handle: The handle to unblock

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v3/blocked_handles",
            body=await async_maybe_transform(
                {"handle": handle}, blocked_handle_unblock_params.BlockedHandleUnblockParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BlockedHandlesResourceWithRawResponse:
    def __init__(self, blocked_handles: BlockedHandlesResource) -> None:
        self._blocked_handles = blocked_handles

        self.list = to_raw_response_wrapper(
            blocked_handles.list,
        )
        self.block = to_raw_response_wrapper(
            blocked_handles.block,
        )
        self.unblock = to_raw_response_wrapper(
            blocked_handles.unblock,
        )


class AsyncBlockedHandlesResourceWithRawResponse:
    def __init__(self, blocked_handles: AsyncBlockedHandlesResource) -> None:
        self._blocked_handles = blocked_handles

        self.list = async_to_raw_response_wrapper(
            blocked_handles.list,
        )
        self.block = async_to_raw_response_wrapper(
            blocked_handles.block,
        )
        self.unblock = async_to_raw_response_wrapper(
            blocked_handles.unblock,
        )


class BlockedHandlesResourceWithStreamingResponse:
    def __init__(self, blocked_handles: BlockedHandlesResource) -> None:
        self._blocked_handles = blocked_handles

        self.list = to_streamed_response_wrapper(
            blocked_handles.list,
        )
        self.block = to_streamed_response_wrapper(
            blocked_handles.block,
        )
        self.unblock = to_streamed_response_wrapper(
            blocked_handles.unblock,
        )


class AsyncBlockedHandlesResourceWithStreamingResponse:
    def __init__(self, blocked_handles: AsyncBlockedHandlesResource) -> None:
        self._blocked_handles = blocked_handles

        self.list = async_to_streamed_response_wrapper(
            blocked_handles.list,
        )
        self.block = async_to_streamed_response_wrapper(
            blocked_handles.block,
        )
        self.unblock = async_to_streamed_response_wrapper(
            blocked_handles.unblock,
        )
