# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    message_create_params,
    message_update_params,
    message_add_reaction_params,
    message_update_app_card_params,
    message_list_messages_thread_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncListMessagesPagination, AsyncListMessagesPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.message import Message
from ..types.shared.reaction_type import ReactionType
from ..types.message_content_param import MessageContentParam
from ..types.message_create_response import MessageCreateResponse
from ..types.message_add_reaction_response import MessageAddReactionResponse
from ..types.message_update_app_card_response import MessageUpdateAppCardResponse

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

    ## Ephemeral Messages (Privacy Tier)

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is automatically given a fixed **24-hour retention window** — after that window the platform permanently deletes the message from Linq storage. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account is retained for 24 hours, then deleted. |
    | **Per phone number** | Only the specified phone numbers have their messages auto-deleted. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: 24 hours** from when the message is created |
    | After expiry | Message stays retrievable | Message is permanently deleted — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are scrubbed; the message is gone, not blanked out |
    | Cross-partner isolation | Enforced | Enforced |

    **How the 24-hour window works:**

    - The window is fixed at **24 hours from message creation** (`created_at`) and cannot be configured per message.
    - It mirrors the ephemeral *attachments* 1-day backstop, so a message and any media it carries expire together.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time. If you need it, compute `created_at + 24h` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
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

    def create(
        self,
        *,
        message: MessageContentParam,
        to: SequenceNotStr[str],
        continuation_message: message_create_params.ContinuationMessage | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse:
        """
        Send a message to one or more recipients **without supplying a `from` number**.
        Linq resolves both the sending line and the target chat for you, then returns
        exactly which line was used, which chat the message landed in, whether a new
        chat was created, and every resulting message id.

        This fuses "create chat" and "send message" behind a single message-centric
        resource. Provide only the recipients (`to`) and the `message`; the platform
        decides the rest.

        ## How the from-number and chat are chosen

        - **Reuse** — if a chat with exactly these recipients already exists and the
          line it lives on is healthy, the message is sent into that chat on its
          existing line (`from_selection.reason = reused_active_chat`).
        - **New** — if no such chat exists, a new chat is created on the best available
          line (`from_selection.reason = new_best_number`).
        - **Failover** — if a matching chat exists but its line has been flagged, a
          **new** chat is created on a fresh best line and the flagged chat is abandoned
          (`from_selection.reason = failover_flagged`, `previous_chat_id` set). If you
          supply `continuation_message`, that text is sent as the single message INSTEAD
          of `message` (useful as a fresh-number-appropriate opener). Exactly one
          message is sent either way.

        Recipients (`to`) are an order-independent set: a single handle is a direct
        chat, multiple handles a group chat.

        ## Differences from POST /v3/chats

        - The first message **may contain a link** (including for a newly created chat).
          Note: sending a link as the very first message on a freshly selected line can
          elevate that line's flagging risk — it is allowed, not recommended.
        - Voice memos are **not** supported here. To send an iMessage voice-memo bubble,
          use `POST /v3/chats/{chatId}/voicememo` with a known chat id.

        ## Service preference, effects, decorations

        Set `message.preferred_service` (`iMessage` | `RCS` | `SMS`), `message.effect`,
        and per-part `text_decorations` exactly as on the other send endpoints.

        Always responds `202 Accepted` — chat creation is incidental to the send.

        Args:
          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

          to: Recipient handles (E.164 phone numbers or email addresses). One handle is a
              direct chat; multiple handles a group chat. Order-independent — the set
              identifies the chat.

          continuation_message: Text-only fallback that **replaces** `message` ONLY on the failover branch —
              when a chat with these recipients already existed but its line was flagged, so a
              new chat is created on a fresh line. On that branch this text is sent as the
              single message instead of `message` (the recipient is on a new number, so you
              typically want a fresh-number-appropriate opener rather than the original
              content). Ignored otherwise (a healthy reuse, or genuine first contact). Carries
              no parts, media, or effects — exactly one message is ever sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v3/messages",
            body=maybe_transform(
                {
                    "message": message,
                    "to": to,
                    "continuation_message": continuation_message,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """Retrieve a specific message by its ID.

        This endpoint returns the full message
        details including text, attachments, reactions, and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def update(
        self,
        message_id: str,
        *,
        text: str,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Edit the text content of a specific part of a previously sent message.

        **Note:** A message can be edited up to 5 times, and only within 15 minutes of
        when it was originally sent.

        Args:
          text: New text content for the message part

          part_index: Index of the message part to edit. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._patch(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            body=maybe_transform(
                {
                    "text": text,
                    "part_index": part_index,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a message from the Linq API only.

        This does NOT unsend or remove the
        message from the actual chat — recipients will still see the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_reaction(
        self,
        message_id: str,
        *,
        operation: Literal["add", "remove"],
        type: ReactionType,
        custom_emoji: str | Omit = omit,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageAddReactionResponse:
        """Add or remove emoji reactions to messages.

        Reactions let users express their
        response to a message without sending a new message.

        **Supported Reactions:**

        - love ❤️
        - like 👍
        - dislike 👎
        - laugh 😂
        - emphasize ‼️
        - question ❓
        - custom - any emoji (use `custom_emoji` field to specify)

        Args:
          operation: Whether to add or remove the reaction

          type: Type of reaction. Standard iMessage tapbacks are love, like, dislike, laugh,
              emphasize, question. Custom emoji reactions have type "custom" with the actual
              emoji in the custom_emoji field. Sticker reactions have type "sticker" with
              sticker attachment details in the sticker field.

          custom_emoji: Custom emoji string. Required when type is "custom".

          part_index: Optional index of the message part to react to. If not provided, reacts to the
              entire message (part 0).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/v3/messages/{message_id}/reactions", message_id=message_id),
            body=maybe_transform(
                {
                    "operation": operation,
                    "type": type,
                    "custom_emoji": custom_emoji,
                    "part_index": part_index,
                },
                message_add_reaction_params.MessageAddReactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAddReactionResponse,
        )

    def list_messages_thread(
        self,
        message_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncListMessagesPagination[Message]:
        """Retrieve all messages in a conversation thread.

        Given any message ID in the
        thread, returns the originator message and all replies in chronological order.

        If the message is not part of a thread, returns just that single message.

        Supports pagination and configurable ordering.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          order: Sort order for messages (asc = oldest first, desc = newest first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            path_template("/v3/messages/{message_id}/thread", message_id=message_id),
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
                        "order": order,
                    },
                    message_list_messages_thread_params.MessageListMessagesThreadParams,
                ),
            ),
            model=Message,
        )

    def update_app_card(
        self,
        message_id: str,
        *,
        layout: message_update_app_card_params.Layout,
        fallback_text: str | Omit = omit,
        interactive: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateAppCardResponse:
        """
        Replaces a previously delivered `imessage_app` card on the recipient's screen
        with new content, instead of posting a new bubble (like a game move redrawing
        the board).

        The update is delivered as a **new message** with its own id and delivery
        lifecycle (`message.sent` / `message.delivered` / `message.failed` webhooks fire
        for the new id). To update the card again, reference the message id returned by
        this call.

        Constraints:

        - The referenced message must be an `imessage_app` card sent by you (`400`
          otherwise — inbound cards cannot be updated).
        - The referenced card must already be delivered (`409` otherwise — retry after
          the `message.delivered` webhook for it).
        - The app identity (`team_id`, `bundle_id`, name) is inherited from the original
          card and cannot change; only `url`, `fallback_text`, and `layout` are
          replaced.
        - iMessage-only, like all app cards.
        - Concurrent updates against the same card are not serialized server-side; the
          last one delivered wins on the recipient's screen. Serialize updates by always
          referencing the message id returned by the previous call.

        Args:
          layout: Visible layout of the card. At least one of `caption`, `subcaption`,
              `trailing_caption`, `trailing_subcaption`, or `image_url` must be set, otherwise
              the card renders as an empty bubble.

              `image_url` displays a preview image at the top of the card. The image renders
              on the recipient's card whether or not they have your app installed. The small
              icon beside the caption is the app's own icon and is not settable here.

              `* Note - requires a trusted chat w/ inbound activity`

              `image_title` and `image_subtitle` render as text overlaid on the image (title
              bold, subtitle beneath it). They only appear when `image_url` is set — without
              an image there is nothing to overlay — so setting either without `image_url` is
              rejected.

          fallback_text: Text shown on surfaces that cannot render the card (notifications, lock screen).
              Defaults to the caption when omitted.

          interactive: Whether the updated card renders as your app's interactive balloon for
              recipients who have your iMessage app installed. `true` (default) lets your
              installed extension draw its live view; `false` always shows the static `layout`
              card. Recipients without your app always see the static card regardless of this
              flag.

              Defaults to `true` when omitted — it is **not** inherited from the original
              card. To keep a card static across updates, re-send `interactive: false` on each
              update.

          url: URL the recipient's app opens when they tap the updated card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/v3/messages/{message_id}/update", message_id=message_id),
            body=maybe_transform(
                {
                    "layout": layout,
                    "fallback_text": fallback_text,
                    "interactive": interactive,
                    "url": url,
                },
                message_update_app_card_params.MessageUpdateAppCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateAppCardResponse,
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

    ## Ephemeral Messages (Privacy Tier)

    For regulated or sensitive conversations, opt in to the **ephemeral messages** tier by contacting your Linq support contact. When enabled, every message on the covered phone numbers is automatically given a fixed **24-hour retention window** — after that window the platform permanently deletes the message from Linq storage. There is no per-message flag; ephemerality is applied automatically based on your configuration.

    You can request it at two scopes:

    | Scope | Effect |
    |---|---|
    | **Partner-wide** | Every outbound and inbound message on every phone number under your account is retained for 24 hours, then deleted. |
    | **Per phone number** | Only the specified phone numbers have their messages auto-deleted. The rest follow the standard message-retention policy. |

    **Behavioral differences vs the standard default:**

    | Aspect | Standard | Ephemeral |
    |---|---|---|
    | Retention | Retained per the standard message-retention policy | **Hard backstop: 24 hours** from when the message is created |
    | After expiry | Message stays retrievable | Message is permanently deleted — `GET /v3/messages/{messageId}` returns `404` and it no longer appears in `GET /v3/chats/{chatId}/messages` |
    | Content on expiry | N/A | Text, formatting, and attachment references are scrubbed; the message is gone, not blanked out |
    | Cross-partner isolation | Enforced | Enforced |

    **How the 24-hour window works:**

    - The window is fixed at **24 hours from message creation** (`created_at`) and cannot be configured per message.
    - It mirrors the ephemeral *attachments* 1-day backstop, so a message and any media it carries expire together.
    - Expiry is delivery-independent — the clock starts when the message is created, not when it is delivered or read.

    **What you observe:**

    - **No expiry timestamp is exposed.** API responses and webhook payloads do not include the deletion time. If you need it, compute `created_at + 24h` yourself.
    - **No deletion webhook is sent.** There is no `message.deleted` event — a message simply stops being retrievable once its window passes.
    - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

    **When to choose ephemeral:**

    - You have a compliance requirement that the platform must not retain message content beyond a short window.
    - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
    - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

    **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
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

    async def create(
        self,
        *,
        message: MessageContentParam,
        to: SequenceNotStr[str],
        continuation_message: message_create_params.ContinuationMessage | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageCreateResponse:
        """
        Send a message to one or more recipients **without supplying a `from` number**.
        Linq resolves both the sending line and the target chat for you, then returns
        exactly which line was used, which chat the message landed in, whether a new
        chat was created, and every resulting message id.

        This fuses "create chat" and "send message" behind a single message-centric
        resource. Provide only the recipients (`to`) and the `message`; the platform
        decides the rest.

        ## How the from-number and chat are chosen

        - **Reuse** — if a chat with exactly these recipients already exists and the
          line it lives on is healthy, the message is sent into that chat on its
          existing line (`from_selection.reason = reused_active_chat`).
        - **New** — if no such chat exists, a new chat is created on the best available
          line (`from_selection.reason = new_best_number`).
        - **Failover** — if a matching chat exists but its line has been flagged, a
          **new** chat is created on a fresh best line and the flagged chat is abandoned
          (`from_selection.reason = failover_flagged`, `previous_chat_id` set). If you
          supply `continuation_message`, that text is sent as the single message INSTEAD
          of `message` (useful as a fresh-number-appropriate opener). Exactly one
          message is sent either way.

        Recipients (`to`) are an order-independent set: a single handle is a direct
        chat, multiple handles a group chat.

        ## Differences from POST /v3/chats

        - The first message **may contain a link** (including for a newly created chat).
          Note: sending a link as the very first message on a freshly selected line can
          elevate that line's flagging risk — it is allowed, not recommended.
        - Voice memos are **not** supported here. To send an iMessage voice-memo bubble,
          use `POST /v3/chats/{chatId}/voicememo` with a known chat id.

        ## Service preference, effects, decorations

        Set `message.preferred_service` (`iMessage` | `RCS` | `SMS`), `message.effect`,
        and per-part `text_decorations` exactly as on the other send endpoints.

        Always responds `202 Accepted` — chat creation is incidental to the send.

        Args:
          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

          to: Recipient handles (E.164 phone numbers or email addresses). One handle is a
              direct chat; multiple handles a group chat. Order-independent — the set
              identifies the chat.

          continuation_message: Text-only fallback that **replaces** `message` ONLY on the failover branch —
              when a chat with these recipients already existed but its line was flagged, so a
              new chat is created on a fresh line. On that branch this text is sent as the
              single message instead of `message` (the recipient is on a new number, so you
              typically want a fresh-number-appropriate opener rather than the original
              content). Ignored otherwise (a healthy reuse, or genuine first contact). Carries
              no parts, media, or effects — exactly one message is ever sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v3/messages",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "to": to,
                    "continuation_message": continuation_message,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    async def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """Retrieve a specific message by its ID.

        This endpoint returns the full message
        details including text, attachments, reactions, and metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def update(
        self,
        message_id: str,
        *,
        text: str,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Edit the text content of a specific part of a previously sent message.

        **Note:** A message can be edited up to 5 times, and only within 15 minutes of
        when it was originally sent.

        Args:
          text: New text content for the message part

          part_index: Index of the message part to edit. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._patch(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "part_index": part_index,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def delete(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a message from the Linq API only.

        This does NOT unsend or remove the
        message from the actual chat — recipients will still see the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/messages/{message_id}", message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_reaction(
        self,
        message_id: str,
        *,
        operation: Literal["add", "remove"],
        type: ReactionType,
        custom_emoji: str | Omit = omit,
        part_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageAddReactionResponse:
        """Add or remove emoji reactions to messages.

        Reactions let users express their
        response to a message without sending a new message.

        **Supported Reactions:**

        - love ❤️
        - like 👍
        - dislike 👎
        - laugh 😂
        - emphasize ‼️
        - question ❓
        - custom - any emoji (use `custom_emoji` field to specify)

        Args:
          operation: Whether to add or remove the reaction

          type: Type of reaction. Standard iMessage tapbacks are love, like, dislike, laugh,
              emphasize, question. Custom emoji reactions have type "custom" with the actual
              emoji in the custom_emoji field. Sticker reactions have type "sticker" with
              sticker attachment details in the sticker field.

          custom_emoji: Custom emoji string. Required when type is "custom".

          part_index: Optional index of the message part to react to. If not provided, reacts to the
              entire message (part 0).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/v3/messages/{message_id}/reactions", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "operation": operation,
                    "type": type,
                    "custom_emoji": custom_emoji,
                    "part_index": part_index,
                },
                message_add_reaction_params.MessageAddReactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAddReactionResponse,
        )

    def list_messages_thread(
        self,
        message_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncListMessagesPagination[Message]]:
        """Retrieve all messages in a conversation thread.

        Given any message ID in the
        thread, returns the originator message and all replies in chronological order.

        If the message is not part of a thread, returns just that single message.

        Supports pagination and configurable ordering.

        Args:
          cursor: Pagination cursor from previous next_cursor response

          limit: Maximum number of messages to return

          order: Sort order for messages (asc = oldest first, desc = newest first)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            path_template("/v3/messages/{message_id}/thread", message_id=message_id),
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
                        "order": order,
                    },
                    message_list_messages_thread_params.MessageListMessagesThreadParams,
                ),
            ),
            model=Message,
        )

    async def update_app_card(
        self,
        message_id: str,
        *,
        layout: message_update_app_card_params.Layout,
        fallback_text: str | Omit = omit,
        interactive: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateAppCardResponse:
        """
        Replaces a previously delivered `imessage_app` card on the recipient's screen
        with new content, instead of posting a new bubble (like a game move redrawing
        the board).

        The update is delivered as a **new message** with its own id and delivery
        lifecycle (`message.sent` / `message.delivered` / `message.failed` webhooks fire
        for the new id). To update the card again, reference the message id returned by
        this call.

        Constraints:

        - The referenced message must be an `imessage_app` card sent by you (`400`
          otherwise — inbound cards cannot be updated).
        - The referenced card must already be delivered (`409` otherwise — retry after
          the `message.delivered` webhook for it).
        - The app identity (`team_id`, `bundle_id`, name) is inherited from the original
          card and cannot change; only `url`, `fallback_text`, and `layout` are
          replaced.
        - iMessage-only, like all app cards.
        - Concurrent updates against the same card are not serialized server-side; the
          last one delivered wins on the recipient's screen. Serialize updates by always
          referencing the message id returned by the previous call.

        Args:
          layout: Visible layout of the card. At least one of `caption`, `subcaption`,
              `trailing_caption`, `trailing_subcaption`, or `image_url` must be set, otherwise
              the card renders as an empty bubble.

              `image_url` displays a preview image at the top of the card. The image renders
              on the recipient's card whether or not they have your app installed. The small
              icon beside the caption is the app's own icon and is not settable here.

              `* Note - requires a trusted chat w/ inbound activity`

              `image_title` and `image_subtitle` render as text overlaid on the image (title
              bold, subtitle beneath it). They only appear when `image_url` is set — without
              an image there is nothing to overlay — so setting either without `image_url` is
              rejected.

          fallback_text: Text shown on surfaces that cannot render the card (notifications, lock screen).
              Defaults to the caption when omitted.

          interactive: Whether the updated card renders as your app's interactive balloon for
              recipients who have your iMessage app installed. `true` (default) lets your
              installed extension draw its live view; `false` always shows the static `layout`
              card. Recipients without your app always see the static card regardless of this
              flag.

              Defaults to `true` when omitted — it is **not** inherited from the original
              card. To keep a card static across updates, re-send `interactive: false` on each
              update.

          url: URL the recipient's app opens when they tap the updated card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/v3/messages/{message_id}/update", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "layout": layout,
                    "fallback_text": fallback_text,
                    "interactive": interactive,
                    "url": url,
                },
                message_update_app_card_params.MessageUpdateAppCardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateAppCardResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )
        self.add_reaction = to_raw_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = to_raw_response_wrapper(
            messages.list_messages_thread,
        )
        self.update_app_card = to_raw_response_wrapper(
            messages.update_app_card,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )
        self.add_reaction = async_to_raw_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = async_to_raw_response_wrapper(
            messages.list_messages_thread,
        )
        self.update_app_card = async_to_raw_response_wrapper(
            messages.update_app_card,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )
        self.add_reaction = to_streamed_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = to_streamed_response_wrapper(
            messages.list_messages_thread,
        )
        self.update_app_card = to_streamed_response_wrapper(
            messages.update_app_card,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )
        self.add_reaction = async_to_streamed_response_wrapper(
            messages.add_reaction,
        )
        self.list_messages_thread = async_to_streamed_response_wrapper(
            messages.list_messages_thread,
        )
        self.update_app_card = async_to_streamed_response_wrapper(
            messages.update_app_card,
        )
