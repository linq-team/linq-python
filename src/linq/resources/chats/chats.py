# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .typing import (
    TypingResource,
    AsyncTypingResource,
    TypingResourceWithRawResponse,
    AsyncTypingResourceWithRawResponse,
    TypingResourceWithStreamingResponse,
    AsyncTypingResourceWithStreamingResponse,
)
from ...types import (
    chat_create_params,
    chat_update_params,
    chat_list_chats_params,
    chat_send_voicememo_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .location import (
    LocationResource,
    AsyncLocationResource,
    LocationResourceWithRawResponse,
    AsyncLocationResourceWithRawResponse,
    LocationResourceWithStreamingResponse,
    AsyncLocationResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncListChatsPagination, AsyncListChatsPagination
from ...types.chat import Chat
from .participants import (
    ParticipantsResource,
    AsyncParticipantsResource,
    ParticipantsResourceWithRawResponse,
    AsyncParticipantsResourceWithRawResponse,
    ParticipantsResourceWithStreamingResponse,
    AsyncParticipantsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.chat_create_response import ChatCreateResponse
from ...types.chat_update_response import ChatUpdateResponse
from ...types.message_content_param import MessageContentParam
from ...types.chat_leave_chat_response import ChatLeaveChatResponse
from ...types.chat_send_voicememo_response import ChatSendVoicememoResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def participants(self) -> ParticipantsResource:
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
        return ParticipantsResource(self._client)

    @cached_property
    def typing(self) -> TypingResource:
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
        return TypingResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
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
        return MessagesResource(self._client)

    @cached_property
    def location(self) -> LocationResource:
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
        return LocationResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        from_: str,
        message: MessageContentParam,
        to: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """Create a new chat with specified participants and send an initial message.

        The
        initial message is required when creating a chat.

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
        must not overlap with other animations or styles. Text decorations only render
        for iMessage recipients. For SMS/RCS, text decorations are not applied.

        ## First-Message Link Restriction

        To protect sender deliverability, the **first outbound message** of a new chat
        cannot be a link. The request is rejected with `400` (error code `1005`) when:

        - The message contains a `link` part (explicit rich-preview link), or
        - Any `text` part contains a URL.

        This rule applies only to `POST /v3/chats`. Follow-up messages on an existing
        chat (`POST /v3/chats/{chatId}/messages`) are not subject to this restriction.

        ## Reusing an Existing Chat

        Chats are keyed on the `from` line plus the exact set of `to` handles. Repeating
        this request with the same `from` and `to` returns the **existing** chat and
        sends the message into it instead of starting a second conversation.

        A group chat that has a `display_name` is excluded from that matching. To run
        several parallel groups over the same participants, name each one with
        `PUT /v3/chats/{chatId}` before creating the next: the following
        `POST /v3/chats` with the same `to` then returns a new, separate `chat_id`. Two
        other cases also produce a new chat instead of reusing one — the participant set
        changed (a participant was added or removed), or the `from` line left the group.

        Whenever the response is a new chat, the first-message rules above apply to that
        request: no link in the first message, and no `reply_to` or message effect. To
        send into a chat you already know, use `POST /v3/chats/{chatId}/messages` with
        its `chat_id`.

        Args:
          from_: Sender phone number in E.164 format. Must be a phone number that the
              authenticated partner has permission to send from.

          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

          to: Array of recipient handles (phone numbers in E.164 format or email addresses).
              For individual chats, provide one recipient. For group chats, provide multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/chats",
            body=maybe_transform(
                {
                    "from_": from_,
                    "message": message,
                    "to": to,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
        )

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
    ) -> Chat:
        """
        Retrieve a chat by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/v3/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
        )

    def update(
        self,
        chat_id: str,
        *,
        display_name: str | Omit = omit,
        group_chat_icon: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatUpdateResponse:
        """
        Update chat properties such as display name and group chat icon.

        Listen for `chat.group_name_updated`, `chat.group_icon_updated`,
        `chat.group_name_update_failed`, or `chat.group_icon_update_failed` webhook
        events to confirm the outcome.

        Args:
          display_name: New display name for the chat (group chats only)

          group_chat_icon: URL of an image to set as the group chat icon (group chats only)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._put(
            path_template("/v3/chats/{chat_id}", chat_id=chat_id),
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "group_chat_icon": group_chat_icon,
                },
                chat_update_params.ChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatUpdateResponse,
        )

    def leave_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatLeaveChatResponse:
        """Removes your phone number from a group chat.

        Once you leave, you will no longer
        receive messages from the group and all interaction endpoints (send message,
        typing, mark read, etc.) will return 409.

        A `participant.removed` webhook will fire once the leave has been processed.

        **Supported**

        - iMessage group chats with 4 or more active participants (including yourself)

        **Not supported**

        - DM (1-on-1) chats — use the chat directly to continue the conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v3/chats/{chat_id}/leave", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatLeaveChatResponse,
        )

    def list_chats(
        self,
        *,
        cursor: str | Omit = omit,
        from_: str | Omit = omit,
        limit: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncListChatsPagination[Chat]:
        """
        Retrieves a paginated list of chats for the authenticated partner.

        **Filtering:**

        - If `from` is provided, returns chats for that specific phone number
        - If `from` is omitted, returns chats across all phone numbers owned by the
          partner
        - If `to` is provided, only returns chats where the specified handle is a
          participant

        **Pagination:**

        - Use `limit` to control page size (default: 20, max: 100)
        - The response includes `next_cursor` for fetching the next page
        - When `next_cursor` is `null`, there are no more results to fetch
        - Pass the `next_cursor` value as the `cursor` parameter for the next request

        **Example pagination flow:**

        1. First request: `GET /v3/chats?from=%2B12223334444&limit=20`
        2. Response includes `next_cursor: "20"` (more results exist)
        3. Next request: `GET /v3/chats?from=%2B12223334444&limit=20&cursor=20`
        4. Response includes `next_cursor: null` (no more results)

        Args:
          cursor: Pagination cursor from the previous response's `next_cursor` field. Omit this
              parameter for the first page of results.

          from_: Phone number to filter chats by. Returns chats made from this phone number. Must
              be in E.164 format (e.g., `+13343284472`). The `+` is automatically URL-encoded
              by HTTP clients. If omitted, returns chats across all phone numbers owned by the
              partner.

          limit: Maximum number of chats to return per page

          to: Filter chats by a participant handle. Only returns chats where this handle is a
              participant. Can be an E.164 phone number (e.g., `+13343284472`) or an email
              address (e.g., `user@example.com`). For phone numbers, the `+` is automatically
              URL-encoded by HTTP clients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/chats",
            page=SyncListChatsPagination[Chat],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "to": to,
                    },
                    chat_list_chats_params.ChatListChatsParams,
                ),
            ),
            model=Chat,
        )

    def mark_as_read(
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
        Mark all messages in a chat as read.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v3/chats/{chat_id}/read", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_voicememo(
        self,
        chat_id: str,
        *,
        attachment_id: str | Omit = omit,
        voice_memo_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSendVoicememoResponse:
        """
        Send an audio file as an **iMessage voice memo bubble** to all participants in a
        chat. Voice memos appear with iMessage's native inline playback UI, unlike
        regular audio attachments sent via media parts which appear as downloadable
        files.

        **Supported audio formats:**

        - MP3 (audio/mpeg)
        - M4A (audio/x-m4a, audio/mp4)
        - AAC (audio/aac)
        - CAF (audio/x-caf) - Core Audio Format
        - WAV (audio/wav)
        - AIFF (audio/aiff, audio/x-aiff)
        - AMR (audio/amr)

        Args:
          attachment_id: Reference to a voice memo file pre-uploaded via `POST /v3/attachments`. The file
              is already stored, so sends using this ID skip the download step.

              Either `voice_memo_url` or `attachment_id` must be provided, but not both.

          voice_memo_url: URL of the voice memo audio file. Must be a publicly accessible HTTPS URL.

              Either `voice_memo_url` or `attachment_id` must be provided, but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v3/chats/{chat_id}/voicememo", chat_id=chat_id),
            body=maybe_transform(
                {
                    "attachment_id": attachment_id,
                    "voice_memo_url": voice_memo_url,
                },
                chat_send_voicememo_params.ChatSendVoicememoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSendVoicememoResponse,
        )

    def share_contact_card(
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
        Share your contact information (Name and Photo Sharing) with a chat.

        **Note:** A contact card must be configured before sharing. You can set up your
        contact card via the [Contact Card API](#tag/Contact-Card) or on the
        [Linq dashboard](https://dashboard.linqapp.com/contact-cards).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v3/chats/{chat_id}/share_contact_card", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def participants(self) -> AsyncParticipantsResource:
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
        return AsyncParticipantsResource(self._client)

    @cached_property
    def typing(self) -> AsyncTypingResource:
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
        return AsyncTypingResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
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
        return AsyncMessagesResource(self._client)

    @cached_property
    def location(self) -> AsyncLocationResource:
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
        return AsyncLocationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linq-team/linq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linq-team/linq-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        from_: str,
        message: MessageContentParam,
        to: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """Create a new chat with specified participants and send an initial message.

        The
        initial message is required when creating a chat.

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
        must not overlap with other animations or styles. Text decorations only render
        for iMessage recipients. For SMS/RCS, text decorations are not applied.

        ## First-Message Link Restriction

        To protect sender deliverability, the **first outbound message** of a new chat
        cannot be a link. The request is rejected with `400` (error code `1005`) when:

        - The message contains a `link` part (explicit rich-preview link), or
        - Any `text` part contains a URL.

        This rule applies only to `POST /v3/chats`. Follow-up messages on an existing
        chat (`POST /v3/chats/{chatId}/messages`) are not subject to this restriction.

        ## Reusing an Existing Chat

        Chats are keyed on the `from` line plus the exact set of `to` handles. Repeating
        this request with the same `from` and `to` returns the **existing** chat and
        sends the message into it instead of starting a second conversation.

        A group chat that has a `display_name` is excluded from that matching. To run
        several parallel groups over the same participants, name each one with
        `PUT /v3/chats/{chatId}` before creating the next: the following
        `POST /v3/chats` with the same `to` then returns a new, separate `chat_id`. Two
        other cases also produce a new chat instead of reusing one — the participant set
        changed (a participant was added or removed), or the `from` line left the group.

        Whenever the response is a new chat, the first-message rules above apply to that
        request: no link in the first message, and no `reply_to` or message effect. To
        send into a chat you already know, use `POST /v3/chats/{chatId}/messages` with
        its `chat_id`.

        Args:
          from_: Sender phone number in E.164 format. Must be a phone number that the
              authenticated partner has permission to send from.

          message: Message content container. Groups all message-related fields together,
              separating the "what" (message content) from the "where" (routing fields like
              from/to).

          to: Array of recipient handles (phone numbers in E.164 format or email addresses).
              For individual chats, provide one recipient. For group chats, provide multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/chats",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "message": message,
                    "to": to,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
        )

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
    ) -> Chat:
        """
        Retrieve a chat by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/v3/chats/{chat_id}", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
        )

    async def update(
        self,
        chat_id: str,
        *,
        display_name: str | Omit = omit,
        group_chat_icon: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatUpdateResponse:
        """
        Update chat properties such as display name and group chat icon.

        Listen for `chat.group_name_updated`, `chat.group_icon_updated`,
        `chat.group_name_update_failed`, or `chat.group_icon_update_failed` webhook
        events to confirm the outcome.

        Args:
          display_name: New display name for the chat (group chats only)

          group_chat_icon: URL of an image to set as the group chat icon (group chats only)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._put(
            path_template("/v3/chats/{chat_id}", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "group_chat_icon": group_chat_icon,
                },
                chat_update_params.ChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatUpdateResponse,
        )

    async def leave_chat(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatLeaveChatResponse:
        """Removes your phone number from a group chat.

        Once you leave, you will no longer
        receive messages from the group and all interaction endpoints (send message,
        typing, mark read, etc.) will return 409.

        A `participant.removed` webhook will fire once the leave has been processed.

        **Supported**

        - iMessage group chats with 4 or more active participants (including yourself)

        **Not supported**

        - DM (1-on-1) chats — use the chat directly to continue the conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v3/chats/{chat_id}/leave", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatLeaveChatResponse,
        )

    def list_chats(
        self,
        *,
        cursor: str | Omit = omit,
        from_: str | Omit = omit,
        limit: int | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Chat, AsyncListChatsPagination[Chat]]:
        """
        Retrieves a paginated list of chats for the authenticated partner.

        **Filtering:**

        - If `from` is provided, returns chats for that specific phone number
        - If `from` is omitted, returns chats across all phone numbers owned by the
          partner
        - If `to` is provided, only returns chats where the specified handle is a
          participant

        **Pagination:**

        - Use `limit` to control page size (default: 20, max: 100)
        - The response includes `next_cursor` for fetching the next page
        - When `next_cursor` is `null`, there are no more results to fetch
        - Pass the `next_cursor` value as the `cursor` parameter for the next request

        **Example pagination flow:**

        1. First request: `GET /v3/chats?from=%2B12223334444&limit=20`
        2. Response includes `next_cursor: "20"` (more results exist)
        3. Next request: `GET /v3/chats?from=%2B12223334444&limit=20&cursor=20`
        4. Response includes `next_cursor: null` (no more results)

        Args:
          cursor: Pagination cursor from the previous response's `next_cursor` field. Omit this
              parameter for the first page of results.

          from_: Phone number to filter chats by. Returns chats made from this phone number. Must
              be in E.164 format (e.g., `+13343284472`). The `+` is automatically URL-encoded
              by HTTP clients. If omitted, returns chats across all phone numbers owned by the
              partner.

          limit: Maximum number of chats to return per page

          to: Filter chats by a participant handle. Only returns chats where this handle is a
              participant. Can be an E.164 phone number (e.g., `+13343284472`) or an email
              address (e.g., `user@example.com`). For phone numbers, the `+` is automatically
              URL-encoded by HTTP clients.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/chats",
            page=AsyncListChatsPagination[Chat],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "to": to,
                    },
                    chat_list_chats_params.ChatListChatsParams,
                ),
            ),
            model=Chat,
        )

    async def mark_as_read(
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
        Mark all messages in a chat as read.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v3/chats/{chat_id}/read", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_voicememo(
        self,
        chat_id: str,
        *,
        attachment_id: str | Omit = omit,
        voice_memo_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSendVoicememoResponse:
        """
        Send an audio file as an **iMessage voice memo bubble** to all participants in a
        chat. Voice memos appear with iMessage's native inline playback UI, unlike
        regular audio attachments sent via media parts which appear as downloadable
        files.

        **Supported audio formats:**

        - MP3 (audio/mpeg)
        - M4A (audio/x-m4a, audio/mp4)
        - AAC (audio/aac)
        - CAF (audio/x-caf) - Core Audio Format
        - WAV (audio/wav)
        - AIFF (audio/aiff, audio/x-aiff)
        - AMR (audio/amr)

        Args:
          attachment_id: Reference to a voice memo file pre-uploaded via `POST /v3/attachments`. The file
              is already stored, so sends using this ID skip the download step.

              Either `voice_memo_url` or `attachment_id` must be provided, but not both.

          voice_memo_url: URL of the voice memo audio file. Must be a publicly accessible HTTPS URL.

              Either `voice_memo_url` or `attachment_id` must be provided, but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v3/chats/{chat_id}/voicememo", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "attachment_id": attachment_id,
                    "voice_memo_url": voice_memo_url,
                },
                chat_send_voicememo_params.ChatSendVoicememoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSendVoicememoResponse,
        )

    async def share_contact_card(
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
        Share your contact information (Name and Photo Sharing) with a chat.

        **Note:** A contact card must be configured before sharing. You can set up your
        contact card via the [Contact Card API](#tag/Contact-Card) or on the
        [Linq dashboard](https://dashboard.linqapp.com/contact-cards).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v3/chats/{chat_id}/share_contact_card", chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_raw_response_wrapper(
            chats.create,
        )
        self.retrieve = to_raw_response_wrapper(
            chats.retrieve,
        )
        self.update = to_raw_response_wrapper(
            chats.update,
        )
        self.leave_chat = to_raw_response_wrapper(
            chats.leave_chat,
        )
        self.list_chats = to_raw_response_wrapper(
            chats.list_chats,
        )
        self.mark_as_read = to_raw_response_wrapper(
            chats.mark_as_read,
        )
        self.send_voicememo = to_raw_response_wrapper(
            chats.send_voicememo,
        )
        self.share_contact_card = to_raw_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def participants(self) -> ParticipantsResourceWithRawResponse:
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
        return ParticipantsResourceWithRawResponse(self._chats.participants)

    @cached_property
    def typing(self) -> TypingResourceWithRawResponse:
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
        return TypingResourceWithRawResponse(self._chats.typing)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
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
        return MessagesResourceWithRawResponse(self._chats.messages)

    @cached_property
    def location(self) -> LocationResourceWithRawResponse:
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
        return LocationResourceWithRawResponse(self._chats.location)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_raw_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            chats.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            chats.update,
        )
        self.leave_chat = async_to_raw_response_wrapper(
            chats.leave_chat,
        )
        self.list_chats = async_to_raw_response_wrapper(
            chats.list_chats,
        )
        self.mark_as_read = async_to_raw_response_wrapper(
            chats.mark_as_read,
        )
        self.send_voicememo = async_to_raw_response_wrapper(
            chats.send_voicememo,
        )
        self.share_contact_card = async_to_raw_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def participants(self) -> AsyncParticipantsResourceWithRawResponse:
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
        return AsyncParticipantsResourceWithRawResponse(self._chats.participants)

    @cached_property
    def typing(self) -> AsyncTypingResourceWithRawResponse:
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
        return AsyncTypingResourceWithRawResponse(self._chats.typing)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
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
        return AsyncMessagesResourceWithRawResponse(self._chats.messages)

    @cached_property
    def location(self) -> AsyncLocationResourceWithRawResponse:
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
        return AsyncLocationResourceWithRawResponse(self._chats.location)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            chats.update,
        )
        self.leave_chat = to_streamed_response_wrapper(
            chats.leave_chat,
        )
        self.list_chats = to_streamed_response_wrapper(
            chats.list_chats,
        )
        self.mark_as_read = to_streamed_response_wrapper(
            chats.mark_as_read,
        )
        self.send_voicememo = to_streamed_response_wrapper(
            chats.send_voicememo,
        )
        self.share_contact_card = to_streamed_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def participants(self) -> ParticipantsResourceWithStreamingResponse:
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
        return ParticipantsResourceWithStreamingResponse(self._chats.participants)

    @cached_property
    def typing(self) -> TypingResourceWithStreamingResponse:
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
        return TypingResourceWithStreamingResponse(self._chats.typing)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
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
        return MessagesResourceWithStreamingResponse(self._chats.messages)

    @cached_property
    def location(self) -> LocationResourceWithStreamingResponse:
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
        return LocationResourceWithStreamingResponse(self._chats.location)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            chats.update,
        )
        self.leave_chat = async_to_streamed_response_wrapper(
            chats.leave_chat,
        )
        self.list_chats = async_to_streamed_response_wrapper(
            chats.list_chats,
        )
        self.mark_as_read = async_to_streamed_response_wrapper(
            chats.mark_as_read,
        )
        self.send_voicememo = async_to_streamed_response_wrapper(
            chats.send_voicememo,
        )
        self.share_contact_card = async_to_streamed_response_wrapper(
            chats.share_contact_card,
        )

    @cached_property
    def participants(self) -> AsyncParticipantsResourceWithStreamingResponse:
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
        return AsyncParticipantsResourceWithStreamingResponse(self._chats.participants)

    @cached_property
    def typing(self) -> AsyncTypingResourceWithStreamingResponse:
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
        return AsyncTypingResourceWithStreamingResponse(self._chats.typing)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
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
        return AsyncMessagesResourceWithStreamingResponse(self._chats.messages)

    @cached_property
    def location(self) -> AsyncLocationResourceWithStreamingResponse:
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
        return AsyncLocationResourceWithStreamingResponse(self._chats.location)
