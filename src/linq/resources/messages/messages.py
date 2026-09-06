# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .poll import (
    PollResource,
    AsyncPollResource,
    PollResourceWithRawResponse,
    AsyncPollResourceWithRawResponse,
    PollResourceWithStreamingResponse,
    AsyncPollResourceWithStreamingResponse,
)
from ...types import (
    message_create_params,
    message_update_params,
    message_add_reaction_params,
    message_update_app_card_params,
    message_list_messages_thread_params,
    message_update_sticker_placement_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncListMessagesPagination, AsyncListMessagesPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message import Message
from ...types.shared.reaction_type import ReactionType
from ...types.message_content_param import MessageContentParam
from ...types.message_create_response import MessageCreateResponse
from ...types.message_add_reaction_response import MessageAddReactionResponse
from ...types.message_update_app_card_response import MessageUpdateAppCardResponse
from ...types.message_update_sticker_placement_response import MessageUpdateStickerPlacementResponse

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
    def poll(self) -> PollResource:
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
        return PollResource(self._client)

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
        exclude_from: SequenceNotStr[str] | Omit = omit,
        override_optout: bool | Omit = omit,
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

        - **Reuse** — if a chat with exactly these recipients already exists on a line
          that can still send, the message is sent into that chat on its existing line
          (`from_selection.reason = reused_active_chat`). The most-recently-active such
          chat wins; chats stranded on flagged lines (e.g. by an earlier failover) are
          skipped.
        - **New** — if no such chat exists, a new chat is created on the best available
          line (`from_selection.reason = new_best_number`).
        - **Failover** — if matching chats exist but none is on a line that can send, a
          **new** chat is created on a fresh best line and the flagged chat is abandoned
          (`from_selection.reason = failover_flagged`, `previous_chat_id` set). If you
          supply `continuation_message`, that text is sent as the single message INSTEAD
          of `message` (useful as a fresh-number-appropriate opener). Exactly one
          message is sent either way.

        Recipients (`to`) are an order-independent set: a single handle is a direct
        chat, multiple handles a group chat.

        ## Excluding lines

        `exclude_from` keeps specific lines out of **this** send's line pick. It only
        affects picking a line for a new chat — an existing chat is always reused on its
        own line, preferring a chat on a non-excluded line when the recipients have more
        than one. An exclusion never abandons a live chat or moves it to a new number,
        so if the only chat these recipients have is on an excluded line, that chat is
        still used. `from` tells you the line that was actually used.

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

              A message carries EITHER `parts` — text and attachments, which compose into one
              bubble — or a single `experience` invocation, which renders an experience inside
              Linq's iMessage app. Never both: an app card is the whole message (Apple's
              `MSMessage` cannot coexist with text), so copy and a card are two sends, not
              one.

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

          exclude_from: Lines (E.164) not to pick for this send. Applies for this request only — nothing
              is remembered between calls.

              **Exclusion only affects picking a line for a new chat.** If `to` already has a
              chat, that chat is reused on its own line, and a chat on a non-excluded line is
              preferred when there is more than one. If the only chat these recipients have is
              on an excluded line, it is still reused — an exclusion never abandons a live
              chat or moves it to a new number. Check `from` in the response to see the line
              that was actually used.

              Numbers that are not your lines are ignored. Every entry must be E.164 — a value
              like `4155551234` is rejected rather than silently skipped. Excluding every one
              of your available lines returns 400 when a line has to be picked.

          override_optout: Send even though the recipient asked you to stop (`403`, error code `2024`).
              Applies to this request only: the opt-out stays in place, so the next send
              without this flag is rejected again. Every override is recorded against your API
              key.

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
                    "exclude_from": exclude_from,
                    "override_optout": override_optout,
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
        message from the actual chat — recipients will still see the message. Re-sending
        with a deleted message's idempotency key returns 404 — a deleted message is
        never resent.

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
        attachment_id: str | Omit = omit,
        custom_emoji: str | Omit = omit,
        part_index: int | Omit = omit,
        placement: message_add_reaction_params.Placement | Omit = omit,
        url: str | Omit = omit,
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
        - sticker - an image peeled onto the message (use `url` or `attachment_id`)

        **Stickers** are iMessage-only and cannot be removed — iMessage has no unpeel
        operation, so `operation: "remove"` with `type: "sticker"` is rejected.
        Position, size and rotation are optional via `placement`, and can be changed
        afterwards with `PATCH /v3/messages/{messageId}/reactions/{reactionId}`.

        Args:
          operation: Whether to add or remove the reaction

          type: Type of reaction. Standard iMessage tapbacks are love, like, dislike, laugh,
              emphasize, question. Custom emoji reactions have type "custom" with the actual
              emoji in the custom_emoji field. Sticker reactions have type "sticker" with
              sticker attachment details in the sticker field.

          attachment_id: Reference to a sticker image pre-uploaded via `POST /v3/attachments`. Only valid
              when type is "sticker".

              Either `url` or `attachment_id` must be provided when type is "sticker", but not
              both.

          custom_emoji: Custom emoji string. Required when type is "custom".

          part_index: Optional index of the message part to react to. If not provided, reacts to the
              entire message (part 0).

          placement: Optional position, size and rotation of a sticker on the target bubble. Only
              valid when type is "sticker".

              Every field is independent and optional — omit the object entirely, or any field
              within it, to keep the default (centred, default size, unrotated).

          url: Linq attachment URL of the sticker image — the `download_url` returned by
              `POST /v3/attachments`. Only valid when type is "sticker".

              Unlike a media part, this does **not** accept an arbitrary host: reactions have
              no download step, so the image must already be stored. To send a sticker from
              elsewhere, upload it with `POST /v3/attachments` first and pass `attachment_id`.

              Either `url` or `attachment_id` must be provided when type is "sticker", but not
              both.

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
                    "attachment_id": attachment_id,
                    "custom_emoji": custom_emoji,
                    "part_index": part_index,
                    "placement": placement,
                    "url": url,
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
        app: message_update_app_card_params.App | Omit = omit,
        experience: message_update_app_card_params.Experience | Omit = omit,
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

          app: Identifies the iMessage app (Messages app extension) that backs the card.

          experience: Invokes an action on an experience — a third party that renders inside Linq's
              iMessage app. Linq resolves the recipient's connection, mints any session the
              action needs, composes the card and sends it; none of that is visible to you.

              Call `GET /v3/experiences/{experience}` for the actions you may invoke and the
              fields each accepts.

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

              Mutually exclusive with `experience` and `raw_payload_data`.

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
                    "app": app,
                    "experience": experience,
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

    def update_sticker_placement(
        self,
        reaction_id: str,
        *,
        message_id: str,
        placement: message_update_sticker_placement_params.Placement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateStickerPlacementResponse:
        """
        Move, resize or rotate a sticker that has already been peeled onto a message.
        The change is sent to every device in the conversation, exactly as dragging the
        sticker by hand would.

        Only stickers can be repositioned — a tapback has no placement, so a non-sticker
        `reactionId` is rejected. Any field omitted from `placement` keeps its current
        value.

        `reactionId` is the `id` from the reaction on the message, or from the
        `reaction.added` webhook. Stickers stack, so this id is what distinguishes one
        sticker from another on the same message.

        Stickers peeled before this endpoint existed cannot be moved: addressing one
        requires an identifier that was not recorded at the time, and it returns 404.

        Args:
          placement: Optional position, size and rotation of a sticker on the target bubble. Only
              valid when type is "sticker".

              Every field is independent and optional — omit the object entirely, or any field
              within it, to keep the default (centred, default size, unrotated).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not reaction_id:
            raise ValueError(f"Expected a non-empty value for `reaction_id` but received {reaction_id!r}")
        return self._patch(
            path_template(
                "/v3/messages/{message_id}/reactions/{reaction_id}", message_id=message_id, reaction_id=reaction_id
            ),
            body=maybe_transform(
                {"placement": placement}, message_update_sticker_placement_params.MessageUpdateStickerPlacementParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateStickerPlacementResponse,
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
    def poll(self) -> AsyncPollResource:
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
        return AsyncPollResource(self._client)

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
        exclude_from: SequenceNotStr[str] | Omit = omit,
        override_optout: bool | Omit = omit,
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

        - **Reuse** — if a chat with exactly these recipients already exists on a line
          that can still send, the message is sent into that chat on its existing line
          (`from_selection.reason = reused_active_chat`). The most-recently-active such
          chat wins; chats stranded on flagged lines (e.g. by an earlier failover) are
          skipped.
        - **New** — if no such chat exists, a new chat is created on the best available
          line (`from_selection.reason = new_best_number`).
        - **Failover** — if matching chats exist but none is on a line that can send, a
          **new** chat is created on a fresh best line and the flagged chat is abandoned
          (`from_selection.reason = failover_flagged`, `previous_chat_id` set). If you
          supply `continuation_message`, that text is sent as the single message INSTEAD
          of `message` (useful as a fresh-number-appropriate opener). Exactly one
          message is sent either way.

        Recipients (`to`) are an order-independent set: a single handle is a direct
        chat, multiple handles a group chat.

        ## Excluding lines

        `exclude_from` keeps specific lines out of **this** send's line pick. It only
        affects picking a line for a new chat — an existing chat is always reused on its
        own line, preferring a chat on a non-excluded line when the recipients have more
        than one. An exclusion never abandons a live chat or moves it to a new number,
        so if the only chat these recipients have is on an excluded line, that chat is
        still used. `from` tells you the line that was actually used.

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

              A message carries EITHER `parts` — text and attachments, which compose into one
              bubble — or a single `experience` invocation, which renders an experience inside
              Linq's iMessage app. Never both: an app card is the whole message (Apple's
              `MSMessage` cannot coexist with text), so copy and a card are two sends, not
              one.

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

          exclude_from: Lines (E.164) not to pick for this send. Applies for this request only — nothing
              is remembered between calls.

              **Exclusion only affects picking a line for a new chat.** If `to` already has a
              chat, that chat is reused on its own line, and a chat on a non-excluded line is
              preferred when there is more than one. If the only chat these recipients have is
              on an excluded line, it is still reused — an exclusion never abandons a live
              chat or moves it to a new number. Check `from` in the response to see the line
              that was actually used.

              Numbers that are not your lines are ignored. Every entry must be E.164 — a value
              like `4155551234` is rejected rather than silently skipped. Excluding every one
              of your available lines returns 400 when a line has to be picked.

          override_optout: Send even though the recipient asked you to stop (`403`, error code `2024`).
              Applies to this request only: the opt-out stays in place, so the next send
              without this flag is rejected again. Every override is recorded against your API
              key.

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
                    "exclude_from": exclude_from,
                    "override_optout": override_optout,
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
        message from the actual chat — recipients will still see the message. Re-sending
        with a deleted message's idempotency key returns 404 — a deleted message is
        never resent.

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
        attachment_id: str | Omit = omit,
        custom_emoji: str | Omit = omit,
        part_index: int | Omit = omit,
        placement: message_add_reaction_params.Placement | Omit = omit,
        url: str | Omit = omit,
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
        - sticker - an image peeled onto the message (use `url` or `attachment_id`)

        **Stickers** are iMessage-only and cannot be removed — iMessage has no unpeel
        operation, so `operation: "remove"` with `type: "sticker"` is rejected.
        Position, size and rotation are optional via `placement`, and can be changed
        afterwards with `PATCH /v3/messages/{messageId}/reactions/{reactionId}`.

        Args:
          operation: Whether to add or remove the reaction

          type: Type of reaction. Standard iMessage tapbacks are love, like, dislike, laugh,
              emphasize, question. Custom emoji reactions have type "custom" with the actual
              emoji in the custom_emoji field. Sticker reactions have type "sticker" with
              sticker attachment details in the sticker field.

          attachment_id: Reference to a sticker image pre-uploaded via `POST /v3/attachments`. Only valid
              when type is "sticker".

              Either `url` or `attachment_id` must be provided when type is "sticker", but not
              both.

          custom_emoji: Custom emoji string. Required when type is "custom".

          part_index: Optional index of the message part to react to. If not provided, reacts to the
              entire message (part 0).

          placement: Optional position, size and rotation of a sticker on the target bubble. Only
              valid when type is "sticker".

              Every field is independent and optional — omit the object entirely, or any field
              within it, to keep the default (centred, default size, unrotated).

          url: Linq attachment URL of the sticker image — the `download_url` returned by
              `POST /v3/attachments`. Only valid when type is "sticker".

              Unlike a media part, this does **not** accept an arbitrary host: reactions have
              no download step, so the image must already be stored. To send a sticker from
              elsewhere, upload it with `POST /v3/attachments` first and pass `attachment_id`.

              Either `url` or `attachment_id` must be provided when type is "sticker", but not
              both.

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
                    "attachment_id": attachment_id,
                    "custom_emoji": custom_emoji,
                    "part_index": part_index,
                    "placement": placement,
                    "url": url,
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
        app: message_update_app_card_params.App | Omit = omit,
        experience: message_update_app_card_params.Experience | Omit = omit,
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

          app: Identifies the iMessage app (Messages app extension) that backs the card.

          experience: Invokes an action on an experience — a third party that renders inside Linq's
              iMessage app. Linq resolves the recipient's connection, mints any session the
              action needs, composes the card and sends it; none of that is visible to you.

              Call `GET /v3/experiences/{experience}` for the actions you may invoke and the
              fields each accepts.

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

              Mutually exclusive with `experience` and `raw_payload_data`.

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
                    "app": app,
                    "experience": experience,
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

    async def update_sticker_placement(
        self,
        reaction_id: str,
        *,
        message_id: str,
        placement: message_update_sticker_placement_params.Placement,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateStickerPlacementResponse:
        """
        Move, resize or rotate a sticker that has already been peeled onto a message.
        The change is sent to every device in the conversation, exactly as dragging the
        sticker by hand would.

        Only stickers can be repositioned — a tapback has no placement, so a non-sticker
        `reactionId` is rejected. Any field omitted from `placement` keeps its current
        value.

        `reactionId` is the `id` from the reaction on the message, or from the
        `reaction.added` webhook. Stickers stack, so this id is what distinguishes one
        sticker from another on the same message.

        Stickers peeled before this endpoint existed cannot be moved: addressing one
        requires an identifier that was not recorded at the time, and it returns 404.

        Args:
          placement: Optional position, size and rotation of a sticker on the target bubble. Only
              valid when type is "sticker".

              Every field is independent and optional — omit the object entirely, or any field
              within it, to keep the default (centred, default size, unrotated).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not reaction_id:
            raise ValueError(f"Expected a non-empty value for `reaction_id` but received {reaction_id!r}")
        return await self._patch(
            path_template(
                "/v3/messages/{message_id}/reactions/{reaction_id}", message_id=message_id, reaction_id=reaction_id
            ),
            body=await async_maybe_transform(
                {"placement": placement}, message_update_sticker_placement_params.MessageUpdateStickerPlacementParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateStickerPlacementResponse,
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
        self.update_sticker_placement = to_raw_response_wrapper(
            messages.update_sticker_placement,
        )

    @cached_property
    def poll(self) -> PollResourceWithRawResponse:
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
        return PollResourceWithRawResponse(self._messages.poll)


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
        self.update_sticker_placement = async_to_raw_response_wrapper(
            messages.update_sticker_placement,
        )

    @cached_property
    def poll(self) -> AsyncPollResourceWithRawResponse:
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
        return AsyncPollResourceWithRawResponse(self._messages.poll)


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
        self.update_sticker_placement = to_streamed_response_wrapper(
            messages.update_sticker_placement,
        )

    @cached_property
    def poll(self) -> PollResourceWithStreamingResponse:
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
        return PollResourceWithStreamingResponse(self._messages.poll)


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
        self.update_sticker_placement = async_to_streamed_response_wrapper(
            messages.update_sticker_placement,
        )

    @cached_property
    def poll(self) -> AsyncPollResourceWithStreamingResponse:
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
        return AsyncPollResourceWithStreamingResponse(self._messages.poll)
