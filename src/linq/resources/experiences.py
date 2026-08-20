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
    An **experience** renders inside Linq's iMessage app as a native card,
    instead of as text or a link. You invoke one by name; Linq resolves the
    recipient, mints any session it needs, composes the card and sends it.

    Send it to `POST /v3/chats/{chatId}/messages`:

    ```json
    {
      "message": {
        "experience": {
          "name": "agentpay",
          "action": "request_payment",
          "params": { "checkout_url": "https://zero.linqapp.com/pay/acme?session=tok_..." }
        }
      }
    }
    ```

    The key is `experience` — what you're invoking. Nested under it is its
    `name`, the action you're invoking on it, and that action's params. A card
    **is** the whole message on Apple's side, so a message carries either
    `experience` or `parts`, never both, and an action goes to exactly one
    recipient.

    ## What you can invoke

    | Experience | Action | What the customer sees |
    |---|---|---|
    | `agentpay` | `request_payment` | A payment request they can pay in the app. Turns itself into "Paid" in place once it settles. |
    | `agentcard` | `attach_card` | A prompt to add a card to their wallet. |
    | `agentcard` | `approve_card` | A passkey approval for a virtual card. |
    | `link` | `open` | A card that opens a URL you supply. |

    `GET /v3/experiences` is the list to build against, with every action and
    the fields each accepts — anything not described there is unsupported.
    Fields are display copy unless documented otherwise.

    ## Params are checked before the card is sent

    Unknown fields are **rejected rather than ignored**, so copy that would
    never have rendered fails for you now instead of arriving wrong on
    somebody's phone. Some fields are read rather than sent: `agentpay`'s
    `request_payment` takes only a `checkout_url` and resolves the amount and
    reason from that payment request, so a card can never claim a figure the
    checkout will not charge.

    Cards are **iMessage-only**. Recipients without the app see a static
    version built from the same copy; SMS and RCS recipients cannot receive
    one at all (error codes 2018 and 4005).
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
        each and the fields each action accepts. Treat it as the list to build against:
        anything not described here is unsupported and may change or stop working
        without notice.
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
    An **experience** renders inside Linq's iMessage app as a native card,
    instead of as text or a link. You invoke one by name; Linq resolves the
    recipient, mints any session it needs, composes the card and sends it.

    Send it to `POST /v3/chats/{chatId}/messages`:

    ```json
    {
      "message": {
        "experience": {
          "name": "agentpay",
          "action": "request_payment",
          "params": { "checkout_url": "https://zero.linqapp.com/pay/acme?session=tok_..." }
        }
      }
    }
    ```

    The key is `experience` — what you're invoking. Nested under it is its
    `name`, the action you're invoking on it, and that action's params. A card
    **is** the whole message on Apple's side, so a message carries either
    `experience` or `parts`, never both, and an action goes to exactly one
    recipient.

    ## What you can invoke

    | Experience | Action | What the customer sees |
    |---|---|---|
    | `agentpay` | `request_payment` | A payment request they can pay in the app. Turns itself into "Paid" in place once it settles. |
    | `agentcard` | `attach_card` | A prompt to add a card to their wallet. |
    | `agentcard` | `approve_card` | A passkey approval for a virtual card. |
    | `link` | `open` | A card that opens a URL you supply. |

    `GET /v3/experiences` is the list to build against, with every action and
    the fields each accepts — anything not described there is unsupported.
    Fields are display copy unless documented otherwise.

    ## Params are checked before the card is sent

    Unknown fields are **rejected rather than ignored**, so copy that would
    never have rendered fails for you now instead of arriving wrong on
    somebody's phone. Some fields are read rather than sent: `agentpay`'s
    `request_payment` takes only a `checkout_url` and resolves the amount and
    reason from that payment request, so a card can never claim a figure the
    checkout will not charge.

    Cards are **iMessage-only**. Recipients without the app see a static
    version built from the same copy; SMS and RCS recipients cannot receive
    one at all (error codes 2018 and 4005).
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
        each and the fields each action accepts. Treat it as the list to build against:
        anything not described here is unsupported and may change or stop working
        without notice.
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
