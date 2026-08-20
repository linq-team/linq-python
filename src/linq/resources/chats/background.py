# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chats import background_set_params
from ..._base_client import make_request_options

__all__ = ["BackgroundResource", "AsyncBackgroundResource"]


class BackgroundResource(SyncAPIResource):
    """A Chat is a conversation thread with one or more participants.

    To begin a chat, you must create a Chat with at least one recipient handle.
    Including multiple handles creates a group chat.

    When creating a chat, the `from` field specifies which of your
    authorized phone numbers the message originates from. Your authentication token grants
    access to one or more phone numbers, but the `from` field determines the actual sender.

    **Handle Format:**
    - Handles can be phone numbers or email addresses
    - Phone numbers MUST be in E.164 format (starting with +)
    - Phone format: `+[country code][subscriber number]`
    - Example phone: `+12223334444` (US), `+442071234567` (UK), `+81312345678` (Japan)
    - Example email: `user@example.com`
    - No spaces, dashes, or parentheses in phone numbers
    """

    @cached_property
    def with_raw_response(self) -> BackgroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return BackgroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BackgroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return BackgroundResourceWithStreamingResponse(self)

    def remove(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove the transcript background from a chat, resetting it to the default.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/chats/{chat_id}/background", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set(
        self,
        chat_id: str,
        *,
        type: Literal["color", "dynamic", "photo"],
        image_url: str | Omit = omit,
        shades: SequenceNotStr[str] | Omit = omit,
        style: Literal["sky", "water", "aurora"] | Omit = omit,
        variant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set the transcript background for a chat.

        Provide one of: a **color** (a named preset or a custom 2-stop gradient), a
        **dynamic** animated style, or a **photo** (by URL). The request is accepted
        asynchronously; the terminal result arrives via the `chat.background_updated`
        webhook on success, or `chat.background_update_failed` on failure.

        **Group chats are supported.** Requests for RCS or SMS chats are accepted
        (`202`) but no background is applied and no `chat.background_updated` webhook
        fires.

        Args:
          type: The background family.

          image_url: Photo: the image URL to embed in the background. Must be an absolute `https` URL
              pointing at an image (`.jpg`, `.png`, `.heic`, `.webp`), and the image is
              fetched and re-hosted on our CDN before the request is accepted — the same way
              `group_chat_icon` works. A URL we cannot fetch, or one that isn't an image, is
              rejected with a `400` (`5007`/`5006`) rather than failing later on the device.

              Example: `https://cdn.linqapp.com/u/bg.jpg`.

          shades: Color with `variant: custom`: the two gradient stops as hex, top then bottom —
              e.g. `["#F2C4E1", "#F5A623"]`. Ignored for named color variants (they carry
              their own two colors).

          style: Dynamic: the animated style — `sky`, `water`, or `aurora`.

          variant: Color: a named swatch — `mango`, `ice`, `plum`, `deep_sea`, `green_apple`,
              `cherry`, `bubblegum`, `tangerine`, `magenta`, `lime`, `silver`, `carbon`,
              `stone` — or `custom` (supply `shades`). Omitting `variant` is equivalent to
              `custom`, so it still requires `shades`.

              Dynamic: required — the variant within the `style`. `sky`: `dusk`, `haze`,
              `sunset`, `clear`, `sunrise`, `dawn`. `water`: `light`, `dark`. `aurora`:
              `green`, `purple`, `pink`.

              An unrecognized value is rejected with `400`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v3/chats/{chat_id}/background", chat_id=chat_id),
            body=maybe_transform(
                {
                    "type": type,
                    "image_url": image_url,
                    "shades": shades,
                    "style": style,
                    "variant": variant,
                },
                background_set_params.BackgroundSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBackgroundResource(AsyncAPIResource):
    """A Chat is a conversation thread with one or more participants.

    To begin a chat, you must create a Chat with at least one recipient handle.
    Including multiple handles creates a group chat.

    When creating a chat, the `from` field specifies which of your
    authorized phone numbers the message originates from. Your authentication token grants
    access to one or more phone numbers, but the `from` field determines the actual sender.

    **Handle Format:**
    - Handles can be phone numbers or email addresses
    - Phone numbers MUST be in E.164 format (starting with +)
    - Phone format: `+[country code][subscriber number]`
    - Example phone: `+12223334444` (US), `+442071234567` (UK), `+81312345678` (Japan)
    - Example email: `user@example.com`
    - No spaces, dashes, or parentheses in phone numbers
    """

    @cached_property
    def with_raw_response(self) -> AsyncBackgroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBackgroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBackgroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncBackgroundResourceWithStreamingResponse(self)

    async def remove(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove the transcript background from a chat, resetting it to the default.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/chats/{chat_id}/background", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set(
        self,
        chat_id: str,
        *,
        type: Literal["color", "dynamic", "photo"],
        image_url: str | Omit = omit,
        shades: SequenceNotStr[str] | Omit = omit,
        style: Literal["sky", "water", "aurora"] | Omit = omit,
        variant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set the transcript background for a chat.

        Provide one of: a **color** (a named preset or a custom 2-stop gradient), a
        **dynamic** animated style, or a **photo** (by URL). The request is accepted
        asynchronously; the terminal result arrives via the `chat.background_updated`
        webhook on success, or `chat.background_update_failed` on failure.

        **Group chats are supported.** Requests for RCS or SMS chats are accepted
        (`202`) but no background is applied and no `chat.background_updated` webhook
        fires.

        Args:
          type: The background family.

          image_url: Photo: the image URL to embed in the background. Must be an absolute `https` URL
              pointing at an image (`.jpg`, `.png`, `.heic`, `.webp`), and the image is
              fetched and re-hosted on our CDN before the request is accepted — the same way
              `group_chat_icon` works. A URL we cannot fetch, or one that isn't an image, is
              rejected with a `400` (`5007`/`5006`) rather than failing later on the device.

              Example: `https://cdn.linqapp.com/u/bg.jpg`.

          shades: Color with `variant: custom`: the two gradient stops as hex, top then bottom —
              e.g. `["#F2C4E1", "#F5A623"]`. Ignored for named color variants (they carry
              their own two colors).

          style: Dynamic: the animated style — `sky`, `water`, or `aurora`.

          variant: Color: a named swatch — `mango`, `ice`, `plum`, `deep_sea`, `green_apple`,
              `cherry`, `bubblegum`, `tangerine`, `magenta`, `lime`, `silver`, `carbon`,
              `stone` — or `custom` (supply `shades`). Omitting `variant` is equivalent to
              `custom`, so it still requires `shades`.

              Dynamic: required — the variant within the `style`. `sky`: `dusk`, `haze`,
              `sunset`, `clear`, `sunrise`, `dawn`. `water`: `light`, `dark`. `aurora`:
              `green`, `purple`, `pink`.

              An unrecognized value is rejected with `400`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v3/chats/{chat_id}/background", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "image_url": image_url,
                    "shades": shades,
                    "style": style,
                    "variant": variant,
                },
                background_set_params.BackgroundSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BackgroundResourceWithRawResponse:
    def __init__(self, background: BackgroundResource) -> None:
        self._background = background

        self.remove = to_raw_response_wrapper(
            background.remove,
        )
        self.set = to_raw_response_wrapper(
            background.set,
        )


class AsyncBackgroundResourceWithRawResponse:
    def __init__(self, background: AsyncBackgroundResource) -> None:
        self._background = background

        self.remove = async_to_raw_response_wrapper(
            background.remove,
        )
        self.set = async_to_raw_response_wrapper(
            background.set,
        )


class BackgroundResourceWithStreamingResponse:
    def __init__(self, background: BackgroundResource) -> None:
        self._background = background

        self.remove = to_streamed_response_wrapper(
            background.remove,
        )
        self.set = to_streamed_response_wrapper(
            background.set,
        )


class AsyncBackgroundResourceWithStreamingResponse:
    def __init__(self, background: AsyncBackgroundResource) -> None:
        self._background = background

        self.remove = async_to_streamed_response_wrapper(
            background.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            background.set,
        )
