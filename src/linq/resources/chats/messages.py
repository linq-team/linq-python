# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncListMessagesPagination, AsyncListMessagesPagination
from ...types.chats import message_list_params, message_send_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message import Message
from ...types.message_content_param import MessageContentParam
from ...types.chats.message_send_response import MessageSendResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    """Messages are individual communications within a chat thread.

    Messages can include text, media attachments, rich link previews, special effects
    (like confetti or fireworks), and reactions. All messages are associated with a
    specific chat and sent from a phone number you own.

    Messages support delivery status tracking, read receipts, and editing capabilities.

    ## Rich Link Previews

    Send a URL as a `link` part to deliver it with a rich preview card showing the
    page's title, description, and image (when available). A `link` part must be the
    **only** part in the message — it cannot be combined with text or media parts.
    To send a URL without a preview card, include it in a `text` part instead.

    **Limitations:**
    - A `link` part cannot be combined with other parts in the same message.
    - Maximum URL length: 2,048 characters.

    ## App Clips

    An `app_clip` part sends a **registered App Clip** — not only Linq's Apple Pay
    checkout, but any partner's own App Clip. Like a `link` part it must be the
    **only** part in the message, and it is **iMessage only** — it never downgrades
    to SMS or RCS. The payment-checkout use of this part is covered in the
    **Payments** section.

    ## Ephemeral Messages (Privacy Tier)

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is given a **retention window configured for your account**. After that window, the message's text, formatting, and attachment references are no longer retrievable through the API — see the Attachments row below for how the attachment media itself is handled. Metadata about the message is retained: message identifiers, timestamps, phone numbers, and delivery state. Metadata retention is not bounded by this window. Bounded operational copies, such as backups and delivery queues, expire on their own separate schedules. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    The window can be set anywhere from **60 minutes to 24 hours**, and defaults to **24 hours**. Ask your Linq support contact to configure a shorter window; it cannot be changed through the API.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account has its content removed from the API surface after your configured window. Metadata is retained. |
    | **Per phone number** | Only the specified phone numbers have message content removed from the API surface this way. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: your configured window** (60 minutes – 24 hours, default 24 hours) from when the message is created |
    | After expiry | Message stays retrievable | Message content is no longer retrievable — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are removed from the API surface, not blanked out in place. Metadata (identifiers, timestamps, phone numbers, delivery state) is retained; its retention is not bounded by this window |
    | Attachments | Retained | Media sent on the **ephemeral attachments tier** is removed on its own storage backstop — within roughly 24–48 hours of upload — independently of the message window, so it can outlast a window shorter than a day. Attachments on the persistent tier (including pre-uploads via `POST /v3/attachments`) are kept until you `DELETE` them |
    | Cross-partner isolation | Enforced | Enforced |

    **How the retention window works:**

    - The window runs from **message creation** (`created_at`). It is configured for your account (60 minutes – 24 hours, default 24 hours) and cannot be set per message.
    - Attachment media follows its own storage backstop rather than the message window — see the Attachments row above.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.
    - **Deletion happens shortly *after* the window, not exactly at it.** A background sweep runs every ~5 minutes, so a message typically stops being retrievable within about 5 minutes of its expiry, and longer while a backlog is being worked through. Treat the window as the guaranteed *minimum* retention, never as an exact deletion time or an upper bound.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time, and they do not report your configured window either — so if you are on a window shorter than 24 hours you cannot derive a message's expiry from the API today. Track the window you agreed with your Linq support contact and compute `created_at + window` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **The attachment backstop is separate from the message window.** API retrievability (the `404` behavior above) ends at your configured window. Ephemeral-tier media objects are removed on their own storage backstop — within roughly 24–48 hours of upload — which is independent of the message window and can outlast a window shorter than a day. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message once its window passes, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def list(
        self,
        chat_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncListMessagesPagination[Message]:
        """
        Retrieve messages from a specific chat with pagination support.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get_api_list(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            page=SyncListMessagesPagination[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    def send(
        self,
        chat_id: str,
        *,
        message: MessageContentParam,
        override_optout: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a message to an existing chat.

        Use this endpoint when you already have a
        chat ID and want to send additional messages to it.

        ## Message Effects

        You can add iMessage effects to make your messages more expressive. Effects are
        optional and can be either screen effects (full-screen animations) or bubble
        effects (message bubble animations).

        **Screen Effects:** `confetti`, `fireworks`, `lasers`, `sparkles`,
        `celebration`, `hearts`, `love`, `balloons`, `happy_birthday`, `echo`,
        `spotlight`

        **Bubble Effects:** `slam`, `loud`, `gentle`, `invisible`

        Only one effect type can be applied per message.

        ## Inline Text Decorations (iMessage only)

        Use the `text_decorations` array on a text part to apply styling and animations
        to character ranges.

        Each decoration specifies a `range: [start, end)` and exactly one of `style` or
        `animation`.

        **Styles:** `bold`, `italic`, `strikethrough`, `underline` **Animations:**
        `big`, `small`, `shake`, `nod`, `explode`, `ripple`, `bloom`, `jitter`

        ```json
        {
          "type": "text",
          "value": "Hello world",
          "text_decorations": [
            { "range": [0, 5], "style": "bold" },
            { "range": [6, 11], "animation": "shake" }
          ]
        }
        ```

        **Note:** Style ranges (bold, italic, etc.) may overlap, but animation ranges
        must not overlap with other animations or styles. Decorations render per
        recipient, not per message: in a group with both iMessage and SMS/RCS
        participants, iMessage recipients see the decorations and SMS/RCS recipients
        receive the same message as plain text.

        Args:
          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

              A message carries EITHER `parts` — text and attachments, which compose into one
              bubble — or a single `experience` invocation, which renders an experience inside
              Linq's iMessage app. Never both: an app card is the whole message (Apple's
              `MSMessage` cannot coexist with text), so copy and a card are two sends, not
              one.

          override_optout: Send even though the recipient asked you to stop (`403`, error code `2024`).
              Applies to this request only: the opt-out stays in place, so the next send
              without this flag is rejected again. Every override is recorded against your API
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            body=maybe_transform(
                {
                    "message": message,
                    "override_optout": override_optout,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    """Messages are individual communications within a chat thread.

    Messages can include text, media attachments, rich link previews, special effects
    (like confetti or fireworks), and reactions. All messages are associated with a
    specific chat and sent from a phone number you own.

    Messages support delivery status tracking, read receipts, and editing capabilities.

    ## Rich Link Previews

    Send a URL as a `link` part to deliver it with a rich preview card showing the
    page's title, description, and image (when available). A `link` part must be the
    **only** part in the message — it cannot be combined with text or media parts.
    To send a URL without a preview card, include it in a `text` part instead.

    **Limitations:**
    - A `link` part cannot be combined with other parts in the same message.
    - Maximum URL length: 2,048 characters.

    ## App Clips

    An `app_clip` part sends a **registered App Clip** — not only Linq's Apple Pay
    checkout, but any partner's own App Clip. Like a `link` part it must be the
    **only** part in the message, and it is **iMessage only** — it never downgrades
    to SMS or RCS. The payment-checkout use of this part is covered in the
    **Payments** section.

    ## Ephemeral Messages (Privacy Tier)

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is given a **retention window configured for your account**. After that window, the message's text, formatting, and attachment references are no longer retrievable through the API — see the Attachments row below for how the attachment media itself is handled. Metadata about the message is retained: message identifiers, timestamps, phone numbers, and delivery state. Metadata retention is not bounded by this window. Bounded operational copies, such as backups and delivery queues, expire on their own separate schedules. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    The window can be set anywhere from **60 minutes to 24 hours**, and defaults to **24 hours**. Ask your Linq support contact to configure a shorter window; it cannot be changed through the API.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account has its content removed from the API surface after your configured window. Metadata is retained. |
    | **Per phone number** | Only the specified phone numbers have message content removed from the API surface this way. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: your configured window** (60 minutes – 24 hours, default 24 hours) from when the message is created |
    | After expiry | Message stays retrievable | Message content is no longer retrievable — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are removed from the API surface, not blanked out in place. Metadata (identifiers, timestamps, phone numbers, delivery state) is retained; its retention is not bounded by this window |
    | Attachments | Retained | Media sent on the **ephemeral attachments tier** is removed on its own storage backstop — within roughly 24–48 hours of upload — independently of the message window, so it can outlast a window shorter than a day. Attachments on the persistent tier (including pre-uploads via `POST /v3/attachments`) are kept until you `DELETE` them |
    | Cross-partner isolation | Enforced | Enforced |

    **How the retention window works:**

    - The window runs from **message creation** (`created_at`). It is configured for your account (60 minutes – 24 hours, default 24 hours) and cannot be set per message.
    - Attachment media follows its own storage backstop rather than the message window — see the Attachments row above.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.
    - **Deletion happens shortly *after* the window, not exactly at it.** A background sweep runs every ~5 minutes, so a message typically stops being retrievable within about 5 minutes of its expiry, and longer while a backlog is being worked through. Treat the window as the guaranteed *minimum* retention, never as an exact deletion time or an upper bound.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time, and they do not report your configured window either — so if you are on a window shorter than 24 hours you cannot derive a message's expiry from the API today. Track the window you agreed with your Linq support contact and compute `created_at + window` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **The attachment backstop is separate from the message window.** API retrievability (the `404` behavior above) ends at your configured window. Ephemeral-tier media objects are removed on their own storage backstop — within roughly 24–48 hours of upload — which is independent of the message window and can outlast a window shorter than a day. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message once its window passes, persist anything you need to keep from the webhook payload at the time it is delivered.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    def list(
        self,
        chat_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncListMessagesPagination[Message]]:
        """
        Retrieve messages from a specific chat with pagination support.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get_api_list(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            page=AsyncListMessagesPagination[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    async def send(
        self,
        chat_id: str,
        *,
        message: MessageContentParam,
        override_optout: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a message to an existing chat.

        Use this endpoint when you already have a
        chat ID and want to send additional messages to it.

        ## Message Effects

        You can add iMessage effects to make your messages more expressive. Effects are
        optional and can be either screen effects (full-screen animations) or bubble
        effects (message bubble animations).

        **Screen Effects:** `confetti`, `fireworks`, `lasers`, `sparkles`,
        `celebration`, `hearts`, `love`, `balloons`, `happy_birthday`, `echo`,
        `spotlight`

        **Bubble Effects:** `slam`, `loud`, `gentle`, `invisible`

        Only one effect type can be applied per message.

        ## Inline Text Decorations (iMessage only)

        Use the `text_decorations` array on a text part to apply styling and animations
        to character ranges.

        Each decoration specifies a `range: [start, end)` and exactly one of `style` or
        `animation`.

        **Styles:** `bold`, `italic`, `strikethrough`, `underline` **Animations:**
        `big`, `small`, `shake`, `nod`, `explode`, `ripple`, `bloom`, `jitter`

        ```json
        {
          "type": "text",
          "value": "Hello world",
          "text_decorations": [
            { "range": [0, 5], "style": "bold" },
            { "range": [6, 11], "animation": "shake" }
          ]
        }
        ```

        **Note:** Style ranges (bold, italic, etc.) may overlap, but animation ranges
        must not overlap with other animations or styles. Decorations render per
        recipient, not per message: in a group with both iMessage and SMS/RCS
        participants, iMessage recipients see the decorations and SMS/RCS recipients
        receive the same message as plain text.

        Args:
          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

              A message carries EITHER `parts` — text and attachments, which compose into one
              bubble — or a single `experience` invocation, which renders an experience inside
              Linq's iMessage app. Never both: an app card is the whole message (Apple's
              `MSMessage` cannot coexist with text), so copy and a card are two sends, not
              one.

          override_optout: Send even though the recipient asked you to stop (`403`, error code `2024`).
              Applies to this request only: the opt-out stays in place, so the next send
              without this flag is rejected again. Every override is recorded against your API
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v3/chats/{chat_id}/messages", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "message": message,
                    "override_optout": override_optout,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
