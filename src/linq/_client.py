# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LinqApiv3Error
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        chats,
        messages,
        payments,
        capability,
        attachments,
        experiences,
        contact_card,
        phonenumbers,
        phone_numbers,
        webhook_events,
        blocked_handles,
        payment_handles,
        available_number,
        payment_requests,
        payment_providers,
        webhook_subscriptions,
    )
    from .resources.payments import PaymentsResource, AsyncPaymentsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.capability import CapabilityResource, AsyncCapabilityResource
    from .resources.attachments import AttachmentsResource, AsyncAttachmentsResource
    from .resources.chats.chats import ChatsResource, AsyncChatsResource
    from .resources.experiences import ExperiencesResource, AsyncExperiencesResource
    from .resources.contact_card import ContactCardResource, AsyncContactCardResource
    from .resources.phonenumbers import PhonenumbersResource, AsyncPhonenumbersResource
    from .resources.phone_numbers import PhoneNumbersResource, AsyncPhoneNumbersResource
    from .resources.webhook_events import WebhookEventsResource, AsyncWebhookEventsResource
    from .resources.blocked_handles import BlockedHandlesResource, AsyncBlockedHandlesResource
    from .resources.payment_handles import PaymentHandlesResource, AsyncPaymentHandlesResource
    from .resources.available_number import AvailableNumberResource, AsyncAvailableNumberResource
    from .resources.payment_requests import PaymentRequestsResource, AsyncPaymentRequestsResource
    from .resources.messages.messages import MessagesResource, AsyncMessagesResource
    from .resources.payment_providers import PaymentProvidersResource, AsyncPaymentProvidersResource
    from .resources.webhook_subscriptions import WebhookSubscriptionsResource, AsyncWebhookSubscriptionsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LinqAPIV3",
    "AsyncLinqAPIV3",
    "Client",
    "AsyncClient",
]


class LinqAPIV3(SyncAPIClient):
    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LinqAPIV3 client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `LINQ_API_V3_API_KEY`
        - `webhook_secret` from `LINQ_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("LINQ_API_V3_API_KEY")
        if api_key is None:
            raise LinqApiv3Error(
                "The api_key client option must be set either by passing api_key to the client or by setting the LINQ_API_V3_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("LINQ_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("LINQ_API_V3_BASE_URL")
        if base_url is None:
            base_url = f"https://api.linqapp.com/api/partner"

        custom_headers_env = os.environ.get("LINQ_API_V3_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def chats(self) -> ChatsResource:
        from .resources.chats import ChatsResource

        return ChatsResource(self)

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
        - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
        - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

        **When to choose ephemeral:**

        - You have a compliance requirement that the platform must not retain message content beyond a short window.
        - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
        - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

        **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
        """
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def attachments(self) -> AttachmentsResource:
        """
        Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
        Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

        ## Sending Media via URL (up to 10MB)

        Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

        ```json
        {
          "parts": [
            { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
          ]
        }
        ```

        This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

        ## Pre-Upload (required for files over 10MB)

        Use `POST /v3/attachments` when you want to:
        - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
        - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
        - **Reduce message send latency** — the file is already stored, so sending is faster

        **How it works:**
        1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
        2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
        3. Reference the `attachment_id` in your media part when sending messages (no expiration)

        **Key difference:** When you provide an external `url`, we download and process the file on every send.
        When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

        ## Domain Allowlisting

        Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
        - `url` fields in media and voice memo message parts
        - `download_url` fields in attachment and upload response objects

        If your application enforces domain allowlists (e.g., for SSRF protection), add:

        ```
        cdn.linqapp.com
        ```

        ## Supported File Types

        - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
        - **Videos:** MP4, MOV, M4V
        - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
        - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
        - **Contact & Calendar:** VCF, ICS

        ## Audio: Attachment vs Voice Memo

        Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
        To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
        use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

        ## File Size Limits

        - **URL-based (`url` field):** 10MB maximum
        - **Pre-upload (`attachment_id`):** 100MB maximum

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy — unless the line also has **ephemeral messages** enabled (see the Messages page), in which case the message and its parts are deleted 24 hours after creation |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AttachmentsResource

        return AttachmentsResource(self)

    @cached_property
    def phonenumbers(self) -> PhonenumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phonenumbers import PhonenumbersResource

        return PhonenumbersResource(self)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phone_numbers import PhoneNumbersResource

        return PhoneNumbersResource(self)

    @cached_property
    def available_number(self) -> AvailableNumberResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.available_number import AvailableNumberResource

        return AvailableNumberResource(self)

    @cached_property
    def payment_requests(self) -> PaymentRequestsResource:
        """Request a payment from a recipient over iMessage.

        You create a payment
        request, send its `checkout_url` to the recipient, and they pay with Apple
        Pay or card. Funds settle **directly to your own Stripe account** — Linq
        never holds the money.

        ## How it works

        1. **Create** a payment request with an amount and currency. You get back a
           `checkout_url` and a `status` of `requested`.
        2. **Send** the `checkout_url` to the recipient as a `link` message part so
           it arrives as a tappable card (see *Sending the link* below).
        3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
           supported iPhone, web checkout everywhere else).
        4. You receive a **`payment.succeeded`** webhook and the request's `status`
           becomes `succeeded`. Requests you don't collect eventually `expire`.

        ## Connected accounts (Stripe Standard, direct charges)

        Payments run on **Stripe Connect Standard accounts** using **direct
        charges**: the charge is created on *your* connected account and **you are
        the merchant of record**. That means the money, the payout schedule, the
        customer relationship, and the compliance surface are all yours — Linq
        orchestrates the request and the checkout but is never in the funds flow.

        **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
        Dashboard.** Because charges settle directly to your account, Linq has no
        custody of the funds and cannot issue refunds or contest disputes on your
        behalf — and there is no refund/dispute endpoint in this API by design. Use
        the Stripe Dashboard (or the Stripe API on your own account) for the money
        lifecycle after a payment succeeds.

        ## Getting set up

        Open **Agent Pay** in your Linq dashboard
        (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
        and complete Stripe's onboarding (business details + a bank account). When
        your account reaches `charges_enabled`, request creation unlocks; until you
        connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
        collecting even while Stripe finishes background verification.

        ## Subscriptions

        Set `mode: subscription` on `POST /v3/payment_requests` to start an
        **auto-renewing subscription** instead of a one-time charge. Instead of an
        amount, you pass a `price_id` — an active **recurring Price** on your
        connected Stripe account (create one in your Stripe Dashboard under
        Product catalog; if you sell through Stripe Payment Links today, reuse the
        price your link is built from). The recipient pays the first invoice at
        the same checkout, and their payment method is saved to the subscription
        for automatic renewals.

        The division of labor is deliberate: **Linq handles the first payment,
        your Stripe account handles the rest.** The request reaches `succeeded`
        when the first invoice is paid; from then on the subscription lives
        entirely on your connected account. The response's `stripe` object gives
        you the join keys — `customer_id` and `subscription_id` — so renewals,
        plan changes, dunning, and cancellation are managed with your own Stripe
        Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
        the Customer and Subscription, so correlating in either direction is
        trivial. There are no renewal webhooks from Linq by design.

        ### Discounts

        Pass a `discount` with a **coupon** or **promotion code** from your
        connected Stripe account to apply it to the subscription. Create either in
        your Stripe Dashboard under Product catalog → Coupons; Linq only forwards
        the id.

        ```json
        {
          "mode": "subscription",
          "price_id": "price_1QAbCdEfGhIjKlMn",
          "discount": {
            "coupon": "7fKCMvBh",
            "label": "50% OFF FIRST MONTH"
          }
        }
        ```

        Stripe applies the coupon and prices the first invoice; the `amount` we
        return is that invoice's amount due, so a `$50.00/month` price with a
        50%-off-first-month coupon comes back as `2500` and the recipient is
        charged **$25.00** at checkout. A coupon that covers the whole first
        invoice returns `amount: 0`; checkout shows $0.00 and collects the card for
        the renewal rather than charging now. Renewals bill at the full price
        automatically — how long a discount lasts is the coupon's `duration`,
        enforced by Stripe on your account, and Linq never re-prices anything.

        Use `promotion_code` instead of `coupon` to apply a promotion code by id
        (`promo_...`, not the customer-facing code string); pass one or the other,
        never both.

        `label` is the customer-facing promotion name displayed at checkout instead
        of the coupon or promotion code ID. The label is displayed exactly as
        provided, so include important terms such as "FIRST MONTH" or
        "FIRST 3 MONTHS" when applicable. These terms are not displayed elsewhere
        on the checkout screen.

        If omitted, Stripe uses the coupon's name as the promotion label.

        ### Free trials

        Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
        subscription with a free trial. The checkout still collects the
        recipient's payment method — the pay sheet shows "$0 due today" with the
        first charge date — and saves it to the subscription; Stripe bills it
        automatically when the trial ends. The request reaches `succeeded` when
        the card is collected, and the response carries `trial_end`. If the trial
        would end without a payment method on file, the subscription cancels
        rather than generating unpayable invoices. Trial lifecycle after checkout
        (extending, ending early) is managed in your own Stripe account via
        `stripe.subscription_id`.

        A subscription request you cancel (or that expires unpaid) cancels the
        incomplete Stripe subscription — nothing lingers on your account.

        ## Pre-created customers

        By default each request stands alone: payment mode attaches no Customer,
        and subscription mode creates a fresh one. If you already manage
        Customers on your connected account, pass their id as `customer_id`
        (`cus_...`) on create — in payment mode the charge lands on that
        customer's payment history, and in subscription mode the subscription is
        created on them instead of on a new Customer. The id must reference an
        existing, non-deleted customer on your connected account or the request
        fails with `400`. We never modify a customer you pass — no metadata is
        stamped on it.

        ## Sending the link

        Deliver the `checkout_url` as a **`link` message part** via
        `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
        branding (title, amount, image) instead of a bare URL, which converts far
        better. A `link` part must be the only part in the message. See
        [Rich Link Previews](/guides/messaging/sending-messages).

        On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
        no-install checkout sheet. Everywhere else (Android, desktop, iPhones
        without the App Clip yet) the same URL opens the web checkout, so the link
        always works. The App Clip experience for your payment links is registered
        automatically by Linq and refreshed whenever you update your payments
        branding; a newly registered experience can take up to ~24 hours to
        activate on Apple's side, during which links open the web checkout.

        ## Sending it as a card instead

        A `link` part is one way to deliver a request. The other is the
        **`agentpay` experience**, which sends the same request as a native card
        in Linq's iMessage app — the amount and reason are drawn in the bubble,
        and it turns itself into "Paid" in place once the payment succeeds,
        without a second message.

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

        `checkout_url` is the only required field — pass back exactly what
        `POST /v3/payment_requests` returned. **The amount and reason are read
        from that request, never from you**, so the card can never claim a
        different figure than the checkout will charge. Optional `title` and
        `note` override the copy only. The link must be one of your own payment
        requests; another partner's is rejected.

        The trade-off against a `link` part: a card is an app card, so it is
        iMessage-only, and recipients without the app see a static version of it.
        A link works everywhere and is what opens the Apple Pay App Clip. Send
        whichever suits the conversation — both settle the same payment request
        and fire the same webhooks.

        ## Webhooks

        Subscribe to payment lifecycle events to reconcile server-side rather than
        polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
        Each event carries the payment request id, amount, currency, and your
        `metadata`. See [Webhooks](/guides/webhooks).
        """
        from .resources.payment_requests import PaymentRequestsResource

        return PaymentRequestsResource(self)

    @cached_property
    def payment_providers(self) -> PaymentProvidersResource:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_providers import PaymentProvidersResource

        return PaymentProvidersResource(self)

    @cached_property
    def payment_handles(self) -> PaymentHandlesResource:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_handles import PaymentHandlesResource

        return PaymentHandlesResource(self)

    @cached_property
    def payments(self) -> PaymentsResource:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payments import PaymentsResource

        return PaymentsResource(self)

    @cached_property
    def blocked_handles(self) -> BlockedHandlesResource:
        """Block handles — phone numbers, email addresses, SMS short codes, or
        sender IDs.

        Inbound messages from a blocked handle are dropped before
        they reach your webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include
        unblocked members are not restricted.
        """
        from .resources.blocked_handles import BlockedHandlesResource

        return BlockedHandlesResource(self)

    @cached_property
    def experiences(self) -> ExperiencesResource:
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
        from .resources.experiences import ExperiencesResource

        return ExperiencesResource(self)

    @cached_property
    def webhook_events(self) -> WebhookEventsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import WebhookEventsResource

        return WebhookEventsResource(self)

    @cached_property
    def webhook_subscriptions(self) -> WebhookSubscriptionsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import WebhookSubscriptionsResource

        return WebhookSubscriptionsResource(self)

    @cached_property
    def capability(self) -> CapabilityResource:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import CapabilityResource

        return CapabilityResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def contact_card(self) -> ContactCardResource:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import ContactCardResource

        return ContactCardResource(self)

    @cached_property
    def with_raw_response(self) -> LinqAPIV3WithRawResponse:
        return LinqAPIV3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinqAPIV3WithStreamedResponse:
        return LinqAPIV3WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("bearer_auth", False):
            for key, value in self._bearer_auth.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)


class AsyncLinqAPIV3(AsyncAPIClient):
    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLinqAPIV3 client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `LINQ_API_V3_API_KEY`
        - `webhook_secret` from `LINQ_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("LINQ_API_V3_API_KEY")
        if api_key is None:
            raise LinqApiv3Error(
                "The api_key client option must be set either by passing api_key to the client or by setting the LINQ_API_V3_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("LINQ_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("LINQ_API_V3_BASE_URL")
        if base_url is None:
            base_url = f"https://api.linqapp.com/api/partner"

        custom_headers_env = os.environ.get("LINQ_API_V3_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def chats(self) -> AsyncChatsResource:
        from .resources.chats import AsyncChatsResource

        return AsyncChatsResource(self)

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
        - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
        - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

        **When to choose ephemeral:**

        - You have a compliance requirement that the platform must not retain message content beyond a short window.
        - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
        - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

        **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
        """
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def attachments(self) -> AsyncAttachmentsResource:
        """
        Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
        Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

        ## Sending Media via URL (up to 10MB)

        Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

        ```json
        {
          "parts": [
            { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
          ]
        }
        ```

        This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

        ## Pre-Upload (required for files over 10MB)

        Use `POST /v3/attachments` when you want to:
        - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
        - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
        - **Reduce message send latency** — the file is already stored, so sending is faster

        **How it works:**
        1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
        2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
        3. Reference the `attachment_id` in your media part when sending messages (no expiration)

        **Key difference:** When you provide an external `url`, we download and process the file on every send.
        When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

        ## Domain Allowlisting

        Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
        - `url` fields in media and voice memo message parts
        - `download_url` fields in attachment and upload response objects

        If your application enforces domain allowlists (e.g., for SSRF protection), add:

        ```
        cdn.linqapp.com
        ```

        ## Supported File Types

        - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
        - **Videos:** MP4, MOV, M4V
        - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
        - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
        - **Contact & Calendar:** VCF, ICS

        ## Audio: Attachment vs Voice Memo

        Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
        To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
        use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

        ## File Size Limits

        - **URL-based (`url` field):** 10MB maximum
        - **Pre-upload (`attachment_id`):** 100MB maximum

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy — unless the line also has **ephemeral messages** enabled (see the Messages page), in which case the message and its parts are deleted 24 hours after creation |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AsyncAttachmentsResource

        return AsyncAttachmentsResource(self)

    @cached_property
    def phonenumbers(self) -> AsyncPhonenumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phonenumbers import AsyncPhonenumbersResource

        return AsyncPhonenumbersResource(self)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResource

        return AsyncPhoneNumbersResource(self)

    @cached_property
    def available_number(self) -> AsyncAvailableNumberResource:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.available_number import AsyncAvailableNumberResource

        return AsyncAvailableNumberResource(self)

    @cached_property
    def payment_requests(self) -> AsyncPaymentRequestsResource:
        """Request a payment from a recipient over iMessage.

        You create a payment
        request, send its `checkout_url` to the recipient, and they pay with Apple
        Pay or card. Funds settle **directly to your own Stripe account** — Linq
        never holds the money.

        ## How it works

        1. **Create** a payment request with an amount and currency. You get back a
           `checkout_url` and a `status` of `requested`.
        2. **Send** the `checkout_url` to the recipient as a `link` message part so
           it arrives as a tappable card (see *Sending the link* below).
        3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
           supported iPhone, web checkout everywhere else).
        4. You receive a **`payment.succeeded`** webhook and the request's `status`
           becomes `succeeded`. Requests you don't collect eventually `expire`.

        ## Connected accounts (Stripe Standard, direct charges)

        Payments run on **Stripe Connect Standard accounts** using **direct
        charges**: the charge is created on *your* connected account and **you are
        the merchant of record**. That means the money, the payout schedule, the
        customer relationship, and the compliance surface are all yours — Linq
        orchestrates the request and the checkout but is never in the funds flow.

        **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
        Dashboard.** Because charges settle directly to your account, Linq has no
        custody of the funds and cannot issue refunds or contest disputes on your
        behalf — and there is no refund/dispute endpoint in this API by design. Use
        the Stripe Dashboard (or the Stripe API on your own account) for the money
        lifecycle after a payment succeeds.

        ## Getting set up

        Open **Agent Pay** in your Linq dashboard
        (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
        and complete Stripe's onboarding (business details + a bank account). When
        your account reaches `charges_enabled`, request creation unlocks; until you
        connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
        collecting even while Stripe finishes background verification.

        ## Subscriptions

        Set `mode: subscription` on `POST /v3/payment_requests` to start an
        **auto-renewing subscription** instead of a one-time charge. Instead of an
        amount, you pass a `price_id` — an active **recurring Price** on your
        connected Stripe account (create one in your Stripe Dashboard under
        Product catalog; if you sell through Stripe Payment Links today, reuse the
        price your link is built from). The recipient pays the first invoice at
        the same checkout, and their payment method is saved to the subscription
        for automatic renewals.

        The division of labor is deliberate: **Linq handles the first payment,
        your Stripe account handles the rest.** The request reaches `succeeded`
        when the first invoice is paid; from then on the subscription lives
        entirely on your connected account. The response's `stripe` object gives
        you the join keys — `customer_id` and `subscription_id` — so renewals,
        plan changes, dunning, and cancellation are managed with your own Stripe
        Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
        the Customer and Subscription, so correlating in either direction is
        trivial. There are no renewal webhooks from Linq by design.

        ### Discounts

        Pass a `discount` with a **coupon** or **promotion code** from your
        connected Stripe account to apply it to the subscription. Create either in
        your Stripe Dashboard under Product catalog → Coupons; Linq only forwards
        the id.

        ```json
        {
          "mode": "subscription",
          "price_id": "price_1QAbCdEfGhIjKlMn",
          "discount": {
            "coupon": "7fKCMvBh",
            "label": "50% OFF FIRST MONTH"
          }
        }
        ```

        Stripe applies the coupon and prices the first invoice; the `amount` we
        return is that invoice's amount due, so a `$50.00/month` price with a
        50%-off-first-month coupon comes back as `2500` and the recipient is
        charged **$25.00** at checkout. A coupon that covers the whole first
        invoice returns `amount: 0`; checkout shows $0.00 and collects the card for
        the renewal rather than charging now. Renewals bill at the full price
        automatically — how long a discount lasts is the coupon's `duration`,
        enforced by Stripe on your account, and Linq never re-prices anything.

        Use `promotion_code` instead of `coupon` to apply a promotion code by id
        (`promo_...`, not the customer-facing code string); pass one or the other,
        never both.

        `label` is the customer-facing promotion name displayed at checkout instead
        of the coupon or promotion code ID. The label is displayed exactly as
        provided, so include important terms such as "FIRST MONTH" or
        "FIRST 3 MONTHS" when applicable. These terms are not displayed elsewhere
        on the checkout screen.

        If omitted, Stripe uses the coupon's name as the promotion label.

        ### Free trials

        Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
        subscription with a free trial. The checkout still collects the
        recipient's payment method — the pay sheet shows "$0 due today" with the
        first charge date — and saves it to the subscription; Stripe bills it
        automatically when the trial ends. The request reaches `succeeded` when
        the card is collected, and the response carries `trial_end`. If the trial
        would end without a payment method on file, the subscription cancels
        rather than generating unpayable invoices. Trial lifecycle after checkout
        (extending, ending early) is managed in your own Stripe account via
        `stripe.subscription_id`.

        A subscription request you cancel (or that expires unpaid) cancels the
        incomplete Stripe subscription — nothing lingers on your account.

        ## Pre-created customers

        By default each request stands alone: payment mode attaches no Customer,
        and subscription mode creates a fresh one. If you already manage
        Customers on your connected account, pass their id as `customer_id`
        (`cus_...`) on create — in payment mode the charge lands on that
        customer's payment history, and in subscription mode the subscription is
        created on them instead of on a new Customer. The id must reference an
        existing, non-deleted customer on your connected account or the request
        fails with `400`. We never modify a customer you pass — no metadata is
        stamped on it.

        ## Sending the link

        Deliver the `checkout_url` as a **`link` message part** via
        `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
        branding (title, amount, image) instead of a bare URL, which converts far
        better. A `link` part must be the only part in the message. See
        [Rich Link Previews](/guides/messaging/sending-messages).

        On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
        no-install checkout sheet. Everywhere else (Android, desktop, iPhones
        without the App Clip yet) the same URL opens the web checkout, so the link
        always works. The App Clip experience for your payment links is registered
        automatically by Linq and refreshed whenever you update your payments
        branding; a newly registered experience can take up to ~24 hours to
        activate on Apple's side, during which links open the web checkout.

        ## Sending it as a card instead

        A `link` part is one way to deliver a request. The other is the
        **`agentpay` experience**, which sends the same request as a native card
        in Linq's iMessage app — the amount and reason are drawn in the bubble,
        and it turns itself into "Paid" in place once the payment succeeds,
        without a second message.

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

        `checkout_url` is the only required field — pass back exactly what
        `POST /v3/payment_requests` returned. **The amount and reason are read
        from that request, never from you**, so the card can never claim a
        different figure than the checkout will charge. Optional `title` and
        `note` override the copy only. The link must be one of your own payment
        requests; another partner's is rejected.

        The trade-off against a `link` part: a card is an app card, so it is
        iMessage-only, and recipients without the app see a static version of it.
        A link works everywhere and is what opens the Apple Pay App Clip. Send
        whichever suits the conversation — both settle the same payment request
        and fire the same webhooks.

        ## Webhooks

        Subscribe to payment lifecycle events to reconcile server-side rather than
        polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
        Each event carries the payment request id, amount, currency, and your
        `metadata`. See [Webhooks](/guides/webhooks).
        """
        from .resources.payment_requests import AsyncPaymentRequestsResource

        return AsyncPaymentRequestsResource(self)

    @cached_property
    def payment_providers(self) -> AsyncPaymentProvidersResource:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_providers import AsyncPaymentProvidersResource

        return AsyncPaymentProvidersResource(self)

    @cached_property
    def payment_handles(self) -> AsyncPaymentHandlesResource:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_handles import AsyncPaymentHandlesResource

        return AsyncPaymentHandlesResource(self)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payments import AsyncPaymentsResource

        return AsyncPaymentsResource(self)

    @cached_property
    def blocked_handles(self) -> AsyncBlockedHandlesResource:
        """Block handles — phone numbers, email addresses, SMS short codes, or
        sender IDs.

        Inbound messages from a blocked handle are dropped before
        they reach your webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include
        unblocked members are not restricted.
        """
        from .resources.blocked_handles import AsyncBlockedHandlesResource

        return AsyncBlockedHandlesResource(self)

    @cached_property
    def experiences(self) -> AsyncExperiencesResource:
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
        from .resources.experiences import AsyncExperiencesResource

        return AsyncExperiencesResource(self)

    @cached_property
    def webhook_events(self) -> AsyncWebhookEventsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import AsyncWebhookEventsResource

        return AsyncWebhookEventsResource(self)

    @cached_property
    def webhook_subscriptions(self) -> AsyncWebhookSubscriptionsResource:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import AsyncWebhookSubscriptionsResource

        return AsyncWebhookSubscriptionsResource(self)

    @cached_property
    def capability(self) -> AsyncCapabilityResource:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import AsyncCapabilityResource

        return AsyncCapabilityResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def contact_card(self) -> AsyncContactCardResource:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import AsyncContactCardResource

        return AsyncContactCardResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLinqAPIV3WithRawResponse:
        return AsyncLinqAPIV3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinqAPIV3WithStreamedResponse:
        return AsyncLinqAPIV3WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("bearer_auth", False):
            for key, value in self._bearer_auth.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)


class LinqAPIV3WithRawResponse:
    _client: LinqAPIV3

    def __init__(self, client: LinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.ChatsResourceWithRawResponse:
        from .resources.chats import ChatsResourceWithRawResponse

        return ChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
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
        - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
        - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

        **When to choose ephemeral:**

        - You have a compliance requirement that the platform must not retain message content beyond a short window.
        - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
        - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

        **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
        """
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithRawResponse:
        """
        Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
        Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

        ## Sending Media via URL (up to 10MB)

        Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

        ```json
        {
          "parts": [
            { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
          ]
        }
        ```

        This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

        ## Pre-Upload (required for files over 10MB)

        Use `POST /v3/attachments` when you want to:
        - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
        - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
        - **Reduce message send latency** — the file is already stored, so sending is faster

        **How it works:**
        1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
        2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
        3. Reference the `attachment_id` in your media part when sending messages (no expiration)

        **Key difference:** When you provide an external `url`, we download and process the file on every send.
        When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

        ## Domain Allowlisting

        Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
        - `url` fields in media and voice memo message parts
        - `download_url` fields in attachment and upload response objects

        If your application enforces domain allowlists (e.g., for SSRF protection), add:

        ```
        cdn.linqapp.com
        ```

        ## Supported File Types

        - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
        - **Videos:** MP4, MOV, M4V
        - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
        - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
        - **Contact & Calendar:** VCF, ICS

        ## Audio: Attachment vs Voice Memo

        Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
        To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
        use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

        ## File Size Limits

        - **URL-based (`url` field):** 10MB maximum
        - **Pre-upload (`attachment_id`):** 100MB maximum

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy — unless the line also has **ephemeral messages** enabled (see the Messages page), in which case the message and its parts are deleted 24 hours after creation |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AttachmentsResourceWithRawResponse

        return AttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.PhonenumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phonenumbers import PhonenumbersResourceWithRawResponse

        return PhonenumbersResourceWithRawResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phone_numbers import PhoneNumbersResourceWithRawResponse

        return PhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def available_number(self) -> available_number.AvailableNumberResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.available_number import AvailableNumberResourceWithRawResponse

        return AvailableNumberResourceWithRawResponse(self._client.available_number)

    @cached_property
    def payment_requests(self) -> payment_requests.PaymentRequestsResourceWithRawResponse:
        """Request a payment from a recipient over iMessage.

        You create a payment
        request, send its `checkout_url` to the recipient, and they pay with Apple
        Pay or card. Funds settle **directly to your own Stripe account** — Linq
        never holds the money.

        ## How it works

        1. **Create** a payment request with an amount and currency. You get back a
           `checkout_url` and a `status` of `requested`.
        2. **Send** the `checkout_url` to the recipient as a `link` message part so
           it arrives as a tappable card (see *Sending the link* below).
        3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
           supported iPhone, web checkout everywhere else).
        4. You receive a **`payment.succeeded`** webhook and the request's `status`
           becomes `succeeded`. Requests you don't collect eventually `expire`.

        ## Connected accounts (Stripe Standard, direct charges)

        Payments run on **Stripe Connect Standard accounts** using **direct
        charges**: the charge is created on *your* connected account and **you are
        the merchant of record**. That means the money, the payout schedule, the
        customer relationship, and the compliance surface are all yours — Linq
        orchestrates the request and the checkout but is never in the funds flow.

        **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
        Dashboard.** Because charges settle directly to your account, Linq has no
        custody of the funds and cannot issue refunds or contest disputes on your
        behalf — and there is no refund/dispute endpoint in this API by design. Use
        the Stripe Dashboard (or the Stripe API on your own account) for the money
        lifecycle after a payment succeeds.

        ## Getting set up

        Open **Agent Pay** in your Linq dashboard
        (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
        and complete Stripe's onboarding (business details + a bank account). When
        your account reaches `charges_enabled`, request creation unlocks; until you
        connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
        collecting even while Stripe finishes background verification.

        ## Subscriptions

        Set `mode: subscription` on `POST /v3/payment_requests` to start an
        **auto-renewing subscription** instead of a one-time charge. Instead of an
        amount, you pass a `price_id` — an active **recurring Price** on your
        connected Stripe account (create one in your Stripe Dashboard under
        Product catalog; if you sell through Stripe Payment Links today, reuse the
        price your link is built from). The recipient pays the first invoice at
        the same checkout, and their payment method is saved to the subscription
        for automatic renewals.

        The division of labor is deliberate: **Linq handles the first payment,
        your Stripe account handles the rest.** The request reaches `succeeded`
        when the first invoice is paid; from then on the subscription lives
        entirely on your connected account. The response's `stripe` object gives
        you the join keys — `customer_id` and `subscription_id` — so renewals,
        plan changes, dunning, and cancellation are managed with your own Stripe
        Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
        the Customer and Subscription, so correlating in either direction is
        trivial. There are no renewal webhooks from Linq by design.

        ### Discounts

        Pass a `discount` with a **coupon** or **promotion code** from your
        connected Stripe account to apply it to the subscription. Create either in
        your Stripe Dashboard under Product catalog → Coupons; Linq only forwards
        the id.

        ```json
        {
          "mode": "subscription",
          "price_id": "price_1QAbCdEfGhIjKlMn",
          "discount": {
            "coupon": "7fKCMvBh",
            "label": "50% OFF FIRST MONTH"
          }
        }
        ```

        Stripe applies the coupon and prices the first invoice; the `amount` we
        return is that invoice's amount due, so a `$50.00/month` price with a
        50%-off-first-month coupon comes back as `2500` and the recipient is
        charged **$25.00** at checkout. A coupon that covers the whole first
        invoice returns `amount: 0`; checkout shows $0.00 and collects the card for
        the renewal rather than charging now. Renewals bill at the full price
        automatically — how long a discount lasts is the coupon's `duration`,
        enforced by Stripe on your account, and Linq never re-prices anything.

        Use `promotion_code` instead of `coupon` to apply a promotion code by id
        (`promo_...`, not the customer-facing code string); pass one or the other,
        never both.

        `label` is the customer-facing promotion name displayed at checkout instead
        of the coupon or promotion code ID. The label is displayed exactly as
        provided, so include important terms such as "FIRST MONTH" or
        "FIRST 3 MONTHS" when applicable. These terms are not displayed elsewhere
        on the checkout screen.

        If omitted, Stripe uses the coupon's name as the promotion label.

        ### Free trials

        Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
        subscription with a free trial. The checkout still collects the
        recipient's payment method — the pay sheet shows "$0 due today" with the
        first charge date — and saves it to the subscription; Stripe bills it
        automatically when the trial ends. The request reaches `succeeded` when
        the card is collected, and the response carries `trial_end`. If the trial
        would end without a payment method on file, the subscription cancels
        rather than generating unpayable invoices. Trial lifecycle after checkout
        (extending, ending early) is managed in your own Stripe account via
        `stripe.subscription_id`.

        A subscription request you cancel (or that expires unpaid) cancels the
        incomplete Stripe subscription — nothing lingers on your account.

        ## Pre-created customers

        By default each request stands alone: payment mode attaches no Customer,
        and subscription mode creates a fresh one. If you already manage
        Customers on your connected account, pass their id as `customer_id`
        (`cus_...`) on create — in payment mode the charge lands on that
        customer's payment history, and in subscription mode the subscription is
        created on them instead of on a new Customer. The id must reference an
        existing, non-deleted customer on your connected account or the request
        fails with `400`. We never modify a customer you pass — no metadata is
        stamped on it.

        ## Sending the link

        Deliver the `checkout_url` as a **`link` message part** via
        `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
        branding (title, amount, image) instead of a bare URL, which converts far
        better. A `link` part must be the only part in the message. See
        [Rich Link Previews](/guides/messaging/sending-messages).

        On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
        no-install checkout sheet. Everywhere else (Android, desktop, iPhones
        without the App Clip yet) the same URL opens the web checkout, so the link
        always works. The App Clip experience for your payment links is registered
        automatically by Linq and refreshed whenever you update your payments
        branding; a newly registered experience can take up to ~24 hours to
        activate on Apple's side, during which links open the web checkout.

        ## Sending it as a card instead

        A `link` part is one way to deliver a request. The other is the
        **`agentpay` experience**, which sends the same request as a native card
        in Linq's iMessage app — the amount and reason are drawn in the bubble,
        and it turns itself into "Paid" in place once the payment succeeds,
        without a second message.

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

        `checkout_url` is the only required field — pass back exactly what
        `POST /v3/payment_requests` returned. **The amount and reason are read
        from that request, never from you**, so the card can never claim a
        different figure than the checkout will charge. Optional `title` and
        `note` override the copy only. The link must be one of your own payment
        requests; another partner's is rejected.

        The trade-off against a `link` part: a card is an app card, so it is
        iMessage-only, and recipients without the app see a static version of it.
        A link works everywhere and is what opens the Apple Pay App Clip. Send
        whichever suits the conversation — both settle the same payment request
        and fire the same webhooks.

        ## Webhooks

        Subscribe to payment lifecycle events to reconcile server-side rather than
        polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
        Each event carries the payment request id, amount, currency, and your
        `metadata`. See [Webhooks](/guides/webhooks).
        """
        from .resources.payment_requests import PaymentRequestsResourceWithRawResponse

        return PaymentRequestsResourceWithRawResponse(self._client.payment_requests)

    @cached_property
    def payment_providers(self) -> payment_providers.PaymentProvidersResourceWithRawResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_providers import PaymentProvidersResourceWithRawResponse

        return PaymentProvidersResourceWithRawResponse(self._client.payment_providers)

    @cached_property
    def payment_handles(self) -> payment_handles.PaymentHandlesResourceWithRawResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_handles import PaymentHandlesResourceWithRawResponse

        return PaymentHandlesResourceWithRawResponse(self._client.payment_handles)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payments import PaymentsResourceWithRawResponse

        return PaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def blocked_handles(self) -> blocked_handles.BlockedHandlesResourceWithRawResponse:
        """Block handles — phone numbers, email addresses, SMS short codes, or
        sender IDs.

        Inbound messages from a blocked handle are dropped before
        they reach your webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include
        unblocked members are not restricted.
        """
        from .resources.blocked_handles import BlockedHandlesResourceWithRawResponse

        return BlockedHandlesResourceWithRawResponse(self._client.blocked_handles)

    @cached_property
    def experiences(self) -> experiences.ExperiencesResourceWithRawResponse:
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
        from .resources.experiences import ExperiencesResourceWithRawResponse

        return ExperiencesResourceWithRawResponse(self._client.experiences)

    @cached_property
    def webhook_events(self) -> webhook_events.WebhookEventsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import WebhookEventsResourceWithRawResponse

        return WebhookEventsResourceWithRawResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.WebhookSubscriptionsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import WebhookSubscriptionsResourceWithRawResponse

        return WebhookSubscriptionsResourceWithRawResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.CapabilityResourceWithRawResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import CapabilityResourceWithRawResponse

        return CapabilityResourceWithRawResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.ContactCardResourceWithRawResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import ContactCardResourceWithRawResponse

        return ContactCardResourceWithRawResponse(self._client.contact_card)


class AsyncLinqAPIV3WithRawResponse:
    _client: AsyncLinqAPIV3

    def __init__(self, client: AsyncLinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithRawResponse:
        from .resources.chats import AsyncChatsResourceWithRawResponse

        return AsyncChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
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
        - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
        - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

        **When to choose ephemeral:**

        - You have a compliance requirement that the platform must not retain message content beyond a short window.
        - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
        - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

        **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
        """
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithRawResponse:
        """
        Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
        Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

        ## Sending Media via URL (up to 10MB)

        Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

        ```json
        {
          "parts": [
            { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
          ]
        }
        ```

        This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

        ## Pre-Upload (required for files over 10MB)

        Use `POST /v3/attachments` when you want to:
        - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
        - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
        - **Reduce message send latency** — the file is already stored, so sending is faster

        **How it works:**
        1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
        2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
        3. Reference the `attachment_id` in your media part when sending messages (no expiration)

        **Key difference:** When you provide an external `url`, we download and process the file on every send.
        When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

        ## Domain Allowlisting

        Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
        - `url` fields in media and voice memo message parts
        - `download_url` fields in attachment and upload response objects

        If your application enforces domain allowlists (e.g., for SSRF protection), add:

        ```
        cdn.linqapp.com
        ```

        ## Supported File Types

        - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
        - **Videos:** MP4, MOV, M4V
        - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
        - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
        - **Contact & Calendar:** VCF, ICS

        ## Audio: Attachment vs Voice Memo

        Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
        To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
        use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

        ## File Size Limits

        - **URL-based (`url` field):** 10MB maximum
        - **Pre-upload (`attachment_id`):** 100MB maximum

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy — unless the line also has **ephemeral messages** enabled (see the Messages page), in which case the message and its parts are deleted 24 hours after creation |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithRawResponse

        return AsyncAttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.AsyncPhonenumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phonenumbers import AsyncPhonenumbersResourceWithRawResponse

        return AsyncPhonenumbersResourceWithRawResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithRawResponse

        return AsyncPhoneNumbersResourceWithRawResponse(self._client.phone_numbers)

    @cached_property
    def available_number(self) -> available_number.AsyncAvailableNumberResourceWithRawResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.available_number import AsyncAvailableNumberResourceWithRawResponse

        return AsyncAvailableNumberResourceWithRawResponse(self._client.available_number)

    @cached_property
    def payment_requests(self) -> payment_requests.AsyncPaymentRequestsResourceWithRawResponse:
        """Request a payment from a recipient over iMessage.

        You create a payment
        request, send its `checkout_url` to the recipient, and they pay with Apple
        Pay or card. Funds settle **directly to your own Stripe account** — Linq
        never holds the money.

        ## How it works

        1. **Create** a payment request with an amount and currency. You get back a
           `checkout_url` and a `status` of `requested`.
        2. **Send** the `checkout_url` to the recipient as a `link` message part so
           it arrives as a tappable card (see *Sending the link* below).
        3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
           supported iPhone, web checkout everywhere else).
        4. You receive a **`payment.succeeded`** webhook and the request's `status`
           becomes `succeeded`. Requests you don't collect eventually `expire`.

        ## Connected accounts (Stripe Standard, direct charges)

        Payments run on **Stripe Connect Standard accounts** using **direct
        charges**: the charge is created on *your* connected account and **you are
        the merchant of record**. That means the money, the payout schedule, the
        customer relationship, and the compliance surface are all yours — Linq
        orchestrates the request and the checkout but is never in the funds flow.

        **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
        Dashboard.** Because charges settle directly to your account, Linq has no
        custody of the funds and cannot issue refunds or contest disputes on your
        behalf — and there is no refund/dispute endpoint in this API by design. Use
        the Stripe Dashboard (or the Stripe API on your own account) for the money
        lifecycle after a payment succeeds.

        ## Getting set up

        Open **Agent Pay** in your Linq dashboard
        (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
        and complete Stripe's onboarding (business details + a bank account). When
        your account reaches `charges_enabled`, request creation unlocks; until you
        connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
        collecting even while Stripe finishes background verification.

        ## Subscriptions

        Set `mode: subscription` on `POST /v3/payment_requests` to start an
        **auto-renewing subscription** instead of a one-time charge. Instead of an
        amount, you pass a `price_id` — an active **recurring Price** on your
        connected Stripe account (create one in your Stripe Dashboard under
        Product catalog; if you sell through Stripe Payment Links today, reuse the
        price your link is built from). The recipient pays the first invoice at
        the same checkout, and their payment method is saved to the subscription
        for automatic renewals.

        The division of labor is deliberate: **Linq handles the first payment,
        your Stripe account handles the rest.** The request reaches `succeeded`
        when the first invoice is paid; from then on the subscription lives
        entirely on your connected account. The response's `stripe` object gives
        you the join keys — `customer_id` and `subscription_id` — so renewals,
        plan changes, dunning, and cancellation are managed with your own Stripe
        Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
        the Customer and Subscription, so correlating in either direction is
        trivial. There are no renewal webhooks from Linq by design.

        ### Discounts

        Pass a `discount` with a **coupon** or **promotion code** from your
        connected Stripe account to apply it to the subscription. Create either in
        your Stripe Dashboard under Product catalog → Coupons; Linq only forwards
        the id.

        ```json
        {
          "mode": "subscription",
          "price_id": "price_1QAbCdEfGhIjKlMn",
          "discount": {
            "coupon": "7fKCMvBh",
            "label": "50% OFF FIRST MONTH"
          }
        }
        ```

        Stripe applies the coupon and prices the first invoice; the `amount` we
        return is that invoice's amount due, so a `$50.00/month` price with a
        50%-off-first-month coupon comes back as `2500` and the recipient is
        charged **$25.00** at checkout. A coupon that covers the whole first
        invoice returns `amount: 0`; checkout shows $0.00 and collects the card for
        the renewal rather than charging now. Renewals bill at the full price
        automatically — how long a discount lasts is the coupon's `duration`,
        enforced by Stripe on your account, and Linq never re-prices anything.

        Use `promotion_code` instead of `coupon` to apply a promotion code by id
        (`promo_...`, not the customer-facing code string); pass one or the other,
        never both.

        `label` is the customer-facing promotion name displayed at checkout instead
        of the coupon or promotion code ID. The label is displayed exactly as
        provided, so include important terms such as "FIRST MONTH" or
        "FIRST 3 MONTHS" when applicable. These terms are not displayed elsewhere
        on the checkout screen.

        If omitted, Stripe uses the coupon's name as the promotion label.

        ### Free trials

        Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
        subscription with a free trial. The checkout still collects the
        recipient's payment method — the pay sheet shows "$0 due today" with the
        first charge date — and saves it to the subscription; Stripe bills it
        automatically when the trial ends. The request reaches `succeeded` when
        the card is collected, and the response carries `trial_end`. If the trial
        would end without a payment method on file, the subscription cancels
        rather than generating unpayable invoices. Trial lifecycle after checkout
        (extending, ending early) is managed in your own Stripe account via
        `stripe.subscription_id`.

        A subscription request you cancel (or that expires unpaid) cancels the
        incomplete Stripe subscription — nothing lingers on your account.

        ## Pre-created customers

        By default each request stands alone: payment mode attaches no Customer,
        and subscription mode creates a fresh one. If you already manage
        Customers on your connected account, pass their id as `customer_id`
        (`cus_...`) on create — in payment mode the charge lands on that
        customer's payment history, and in subscription mode the subscription is
        created on them instead of on a new Customer. The id must reference an
        existing, non-deleted customer on your connected account or the request
        fails with `400`. We never modify a customer you pass — no metadata is
        stamped on it.

        ## Sending the link

        Deliver the `checkout_url` as a **`link` message part** via
        `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
        branding (title, amount, image) instead of a bare URL, which converts far
        better. A `link` part must be the only part in the message. See
        [Rich Link Previews](/guides/messaging/sending-messages).

        On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
        no-install checkout sheet. Everywhere else (Android, desktop, iPhones
        without the App Clip yet) the same URL opens the web checkout, so the link
        always works. The App Clip experience for your payment links is registered
        automatically by Linq and refreshed whenever you update your payments
        branding; a newly registered experience can take up to ~24 hours to
        activate on Apple's side, during which links open the web checkout.

        ## Sending it as a card instead

        A `link` part is one way to deliver a request. The other is the
        **`agentpay` experience**, which sends the same request as a native card
        in Linq's iMessage app — the amount and reason are drawn in the bubble,
        and it turns itself into "Paid" in place once the payment succeeds,
        without a second message.

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

        `checkout_url` is the only required field — pass back exactly what
        `POST /v3/payment_requests` returned. **The amount and reason are read
        from that request, never from you**, so the card can never claim a
        different figure than the checkout will charge. Optional `title` and
        `note` override the copy only. The link must be one of your own payment
        requests; another partner's is rejected.

        The trade-off against a `link` part: a card is an app card, so it is
        iMessage-only, and recipients without the app see a static version of it.
        A link works everywhere and is what opens the Apple Pay App Clip. Send
        whichever suits the conversation — both settle the same payment request
        and fire the same webhooks.

        ## Webhooks

        Subscribe to payment lifecycle events to reconcile server-side rather than
        polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
        Each event carries the payment request id, amount, currency, and your
        `metadata`. See [Webhooks](/guides/webhooks).
        """
        from .resources.payment_requests import AsyncPaymentRequestsResourceWithRawResponse

        return AsyncPaymentRequestsResourceWithRawResponse(self._client.payment_requests)

    @cached_property
    def payment_providers(self) -> payment_providers.AsyncPaymentProvidersResourceWithRawResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_providers import AsyncPaymentProvidersResourceWithRawResponse

        return AsyncPaymentProvidersResourceWithRawResponse(self._client.payment_providers)

    @cached_property
    def payment_handles(self) -> payment_handles.AsyncPaymentHandlesResourceWithRawResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_handles import AsyncPaymentHandlesResourceWithRawResponse

        return AsyncPaymentHandlesResourceWithRawResponse(self._client.payment_handles)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payments import AsyncPaymentsResourceWithRawResponse

        return AsyncPaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def blocked_handles(self) -> blocked_handles.AsyncBlockedHandlesResourceWithRawResponse:
        """Block handles — phone numbers, email addresses, SMS short codes, or
        sender IDs.

        Inbound messages from a blocked handle are dropped before
        they reach your webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include
        unblocked members are not restricted.
        """
        from .resources.blocked_handles import AsyncBlockedHandlesResourceWithRawResponse

        return AsyncBlockedHandlesResourceWithRawResponse(self._client.blocked_handles)

    @cached_property
    def experiences(self) -> experiences.AsyncExperiencesResourceWithRawResponse:
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
        from .resources.experiences import AsyncExperiencesResourceWithRawResponse

        return AsyncExperiencesResourceWithRawResponse(self._client.experiences)

    @cached_property
    def webhook_events(self) -> webhook_events.AsyncWebhookEventsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import AsyncWebhookEventsResourceWithRawResponse

        return AsyncWebhookEventsResourceWithRawResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.AsyncWebhookSubscriptionsResourceWithRawResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import AsyncWebhookSubscriptionsResourceWithRawResponse

        return AsyncWebhookSubscriptionsResourceWithRawResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.AsyncCapabilityResourceWithRawResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import AsyncCapabilityResourceWithRawResponse

        return AsyncCapabilityResourceWithRawResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.AsyncContactCardResourceWithRawResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import AsyncContactCardResourceWithRawResponse

        return AsyncContactCardResourceWithRawResponse(self._client.contact_card)


class LinqAPIV3WithStreamedResponse:
    _client: LinqAPIV3

    def __init__(self, client: LinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.ChatsResourceWithStreamingResponse:
        from .resources.chats import ChatsResourceWithStreamingResponse

        return ChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
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
        - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
        - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

        **When to choose ephemeral:**

        - You have a compliance requirement that the platform must not retain message content beyond a short window.
        - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
        - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

        **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
        """
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithStreamingResponse:
        """
        Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
        Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

        ## Sending Media via URL (up to 10MB)

        Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

        ```json
        {
          "parts": [
            { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
          ]
        }
        ```

        This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

        ## Pre-Upload (required for files over 10MB)

        Use `POST /v3/attachments` when you want to:
        - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
        - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
        - **Reduce message send latency** — the file is already stored, so sending is faster

        **How it works:**
        1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
        2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
        3. Reference the `attachment_id` in your media part when sending messages (no expiration)

        **Key difference:** When you provide an external `url`, we download and process the file on every send.
        When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

        ## Domain Allowlisting

        Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
        - `url` fields in media and voice memo message parts
        - `download_url` fields in attachment and upload response objects

        If your application enforces domain allowlists (e.g., for SSRF protection), add:

        ```
        cdn.linqapp.com
        ```

        ## Supported File Types

        - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
        - **Videos:** MP4, MOV, M4V
        - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
        - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
        - **Contact & Calendar:** VCF, ICS

        ## Audio: Attachment vs Voice Memo

        Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
        To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
        use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

        ## File Size Limits

        - **URL-based (`url` field):** 10MB maximum
        - **Pre-upload (`attachment_id`):** 100MB maximum

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy — unless the line also has **ephemeral messages** enabled (see the Messages page), in which case the message and its parts are deleted 24 hours after creation |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AttachmentsResourceWithStreamingResponse

        return AttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.PhonenumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phonenumbers import PhonenumbersResourceWithStreamingResponse

        return PhonenumbersResourceWithStreamingResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.PhoneNumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phone_numbers import PhoneNumbersResourceWithStreamingResponse

        return PhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def available_number(self) -> available_number.AvailableNumberResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.available_number import AvailableNumberResourceWithStreamingResponse

        return AvailableNumberResourceWithStreamingResponse(self._client.available_number)

    @cached_property
    def payment_requests(self) -> payment_requests.PaymentRequestsResourceWithStreamingResponse:
        """Request a payment from a recipient over iMessage.

        You create a payment
        request, send its `checkout_url` to the recipient, and they pay with Apple
        Pay or card. Funds settle **directly to your own Stripe account** — Linq
        never holds the money.

        ## How it works

        1. **Create** a payment request with an amount and currency. You get back a
           `checkout_url` and a `status` of `requested`.
        2. **Send** the `checkout_url` to the recipient as a `link` message part so
           it arrives as a tappable card (see *Sending the link* below).
        3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
           supported iPhone, web checkout everywhere else).
        4. You receive a **`payment.succeeded`** webhook and the request's `status`
           becomes `succeeded`. Requests you don't collect eventually `expire`.

        ## Connected accounts (Stripe Standard, direct charges)

        Payments run on **Stripe Connect Standard accounts** using **direct
        charges**: the charge is created on *your* connected account and **you are
        the merchant of record**. That means the money, the payout schedule, the
        customer relationship, and the compliance surface are all yours — Linq
        orchestrates the request and the checkout but is never in the funds flow.

        **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
        Dashboard.** Because charges settle directly to your account, Linq has no
        custody of the funds and cannot issue refunds or contest disputes on your
        behalf — and there is no refund/dispute endpoint in this API by design. Use
        the Stripe Dashboard (or the Stripe API on your own account) for the money
        lifecycle after a payment succeeds.

        ## Getting set up

        Open **Agent Pay** in your Linq dashboard
        (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
        and complete Stripe's onboarding (business details + a bank account). When
        your account reaches `charges_enabled`, request creation unlocks; until you
        connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
        collecting even while Stripe finishes background verification.

        ## Subscriptions

        Set `mode: subscription` on `POST /v3/payment_requests` to start an
        **auto-renewing subscription** instead of a one-time charge. Instead of an
        amount, you pass a `price_id` — an active **recurring Price** on your
        connected Stripe account (create one in your Stripe Dashboard under
        Product catalog; if you sell through Stripe Payment Links today, reuse the
        price your link is built from). The recipient pays the first invoice at
        the same checkout, and their payment method is saved to the subscription
        for automatic renewals.

        The division of labor is deliberate: **Linq handles the first payment,
        your Stripe account handles the rest.** The request reaches `succeeded`
        when the first invoice is paid; from then on the subscription lives
        entirely on your connected account. The response's `stripe` object gives
        you the join keys — `customer_id` and `subscription_id` — so renewals,
        plan changes, dunning, and cancellation are managed with your own Stripe
        Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
        the Customer and Subscription, so correlating in either direction is
        trivial. There are no renewal webhooks from Linq by design.

        ### Discounts

        Pass a `discount` with a **coupon** or **promotion code** from your
        connected Stripe account to apply it to the subscription. Create either in
        your Stripe Dashboard under Product catalog → Coupons; Linq only forwards
        the id.

        ```json
        {
          "mode": "subscription",
          "price_id": "price_1QAbCdEfGhIjKlMn",
          "discount": {
            "coupon": "7fKCMvBh",
            "label": "50% OFF FIRST MONTH"
          }
        }
        ```

        Stripe applies the coupon and prices the first invoice; the `amount` we
        return is that invoice's amount due, so a `$50.00/month` price with a
        50%-off-first-month coupon comes back as `2500` and the recipient is
        charged **$25.00** at checkout. A coupon that covers the whole first
        invoice returns `amount: 0`; checkout shows $0.00 and collects the card for
        the renewal rather than charging now. Renewals bill at the full price
        automatically — how long a discount lasts is the coupon's `duration`,
        enforced by Stripe on your account, and Linq never re-prices anything.

        Use `promotion_code` instead of `coupon` to apply a promotion code by id
        (`promo_...`, not the customer-facing code string); pass one or the other,
        never both.

        `label` is the customer-facing promotion name displayed at checkout instead
        of the coupon or promotion code ID. The label is displayed exactly as
        provided, so include important terms such as "FIRST MONTH" or
        "FIRST 3 MONTHS" when applicable. These terms are not displayed elsewhere
        on the checkout screen.

        If omitted, Stripe uses the coupon's name as the promotion label.

        ### Free trials

        Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
        subscription with a free trial. The checkout still collects the
        recipient's payment method — the pay sheet shows "$0 due today" with the
        first charge date — and saves it to the subscription; Stripe bills it
        automatically when the trial ends. The request reaches `succeeded` when
        the card is collected, and the response carries `trial_end`. If the trial
        would end without a payment method on file, the subscription cancels
        rather than generating unpayable invoices. Trial lifecycle after checkout
        (extending, ending early) is managed in your own Stripe account via
        `stripe.subscription_id`.

        A subscription request you cancel (or that expires unpaid) cancels the
        incomplete Stripe subscription — nothing lingers on your account.

        ## Pre-created customers

        By default each request stands alone: payment mode attaches no Customer,
        and subscription mode creates a fresh one. If you already manage
        Customers on your connected account, pass their id as `customer_id`
        (`cus_...`) on create — in payment mode the charge lands on that
        customer's payment history, and in subscription mode the subscription is
        created on them instead of on a new Customer. The id must reference an
        existing, non-deleted customer on your connected account or the request
        fails with `400`. We never modify a customer you pass — no metadata is
        stamped on it.

        ## Sending the link

        Deliver the `checkout_url` as a **`link` message part** via
        `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
        branding (title, amount, image) instead of a bare URL, which converts far
        better. A `link` part must be the only part in the message. See
        [Rich Link Previews](/guides/messaging/sending-messages).

        On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
        no-install checkout sheet. Everywhere else (Android, desktop, iPhones
        without the App Clip yet) the same URL opens the web checkout, so the link
        always works. The App Clip experience for your payment links is registered
        automatically by Linq and refreshed whenever you update your payments
        branding; a newly registered experience can take up to ~24 hours to
        activate on Apple's side, during which links open the web checkout.

        ## Sending it as a card instead

        A `link` part is one way to deliver a request. The other is the
        **`agentpay` experience**, which sends the same request as a native card
        in Linq's iMessage app — the amount and reason are drawn in the bubble,
        and it turns itself into "Paid" in place once the payment succeeds,
        without a second message.

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

        `checkout_url` is the only required field — pass back exactly what
        `POST /v3/payment_requests` returned. **The amount and reason are read
        from that request, never from you**, so the card can never claim a
        different figure than the checkout will charge. Optional `title` and
        `note` override the copy only. The link must be one of your own payment
        requests; another partner's is rejected.

        The trade-off against a `link` part: a card is an app card, so it is
        iMessage-only, and recipients without the app see a static version of it.
        A link works everywhere and is what opens the Apple Pay App Clip. Send
        whichever suits the conversation — both settle the same payment request
        and fire the same webhooks.

        ## Webhooks

        Subscribe to payment lifecycle events to reconcile server-side rather than
        polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
        Each event carries the payment request id, amount, currency, and your
        `metadata`. See [Webhooks](/guides/webhooks).
        """
        from .resources.payment_requests import PaymentRequestsResourceWithStreamingResponse

        return PaymentRequestsResourceWithStreamingResponse(self._client.payment_requests)

    @cached_property
    def payment_providers(self) -> payment_providers.PaymentProvidersResourceWithStreamingResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_providers import PaymentProvidersResourceWithStreamingResponse

        return PaymentProvidersResourceWithStreamingResponse(self._client.payment_providers)

    @cached_property
    def payment_handles(self) -> payment_handles.PaymentHandlesResourceWithStreamingResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_handles import PaymentHandlesResourceWithStreamingResponse

        return PaymentHandlesResourceWithStreamingResponse(self._client.payment_handles)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payments import PaymentsResourceWithStreamingResponse

        return PaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def blocked_handles(self) -> blocked_handles.BlockedHandlesResourceWithStreamingResponse:
        """Block handles — phone numbers, email addresses, SMS short codes, or
        sender IDs.

        Inbound messages from a blocked handle are dropped before
        they reach your webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include
        unblocked members are not restricted.
        """
        from .resources.blocked_handles import BlockedHandlesResourceWithStreamingResponse

        return BlockedHandlesResourceWithStreamingResponse(self._client.blocked_handles)

    @cached_property
    def experiences(self) -> experiences.ExperiencesResourceWithStreamingResponse:
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
        from .resources.experiences import ExperiencesResourceWithStreamingResponse

        return ExperiencesResourceWithStreamingResponse(self._client.experiences)

    @cached_property
    def webhook_events(self) -> webhook_events.WebhookEventsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import WebhookEventsResourceWithStreamingResponse

        return WebhookEventsResourceWithStreamingResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.WebhookSubscriptionsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import WebhookSubscriptionsResourceWithStreamingResponse

        return WebhookSubscriptionsResourceWithStreamingResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.CapabilityResourceWithStreamingResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import CapabilityResourceWithStreamingResponse

        return CapabilityResourceWithStreamingResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.ContactCardResourceWithStreamingResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import ContactCardResourceWithStreamingResponse

        return ContactCardResourceWithStreamingResponse(self._client.contact_card)


class AsyncLinqAPIV3WithStreamedResponse:
    _client: AsyncLinqAPIV3

    def __init__(self, client: AsyncLinqAPIV3) -> None:
        self._client = client

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithStreamingResponse:
        from .resources.chats import AsyncChatsResourceWithStreamingResponse

        return AsyncChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
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
        - **The backstop governs Linq storage.** API retrievability (the `404` behavior above) and CDN media expire at the 24-hour mark. Removal of the corresponding entries from the sending device happens asynchronously and can complete after the backstop.
        - **Delivery is unaffected.** Ephemeral messages send, deliver, and fire the usual `message.sent` / `message.received` and status webhooks exactly like standard messages. Only retention changes.

        **When to choose ephemeral:**

        - You have a compliance requirement that the platform must not retain message content beyond a short window.
        - The conversation is high-sensitivity (PHI, financial, identity verification) and you do not want it sitting in storage long-term.
        - Your application is the system of record — you capture what you need from the delivery webhook in real time and do not rely on reading message history back from Linq later.

        **Important:** ephemeral applies in *both directions* — messages you send **and** messages received by the phone numbers in that scope. Because Linq can no longer return the message after 24 hours, persist anything you need to keep from the webhook payload at the time it is delivered.
        """
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithStreamingResponse:
        """
        Send files (images, videos, documents, audio) with messages by providing a URL in a media part.
        Pre-uploading via `POST /v3/attachments` is **optional** and only needed for specific optimization scenarios.

        ## Sending Media via URL (up to 10MB)

        Provide a publicly accessible HTTPS URL with a [supported media type](#supported-file-types) in the `url` field of a media part.

        ```json
        {
          "parts": [
            { "type": "media", "url": "https://your-cdn.com/images/photo.jpg" }
          ]
        }
        ```

        This works with any URL you already host — no pre-upload step required. **Maximum file size: 10MB.**

        ## Pre-Upload (required for files over 10MB)

        Use `POST /v3/attachments` when you want to:
        - **Send files larger than 10MB** (up to 100MB) — URL-based downloads are limited to 10MB
        - **Send the same file to many recipients** — upload once, reuse the `attachment_id` without re-downloading each time
        - **Reduce message send latency** — the file is already stored, so sending is faster

        **How it works:**
        1. `POST /v3/attachments` with file metadata → returns a presigned `upload_url` (valid for **15 minutes**) and a permanent `attachment_id`
        2. PUT the raw file bytes to the `upload_url` with the `required_headers` (no JSON or multipart — just the binary content)
        3. Reference the `attachment_id` in your media part when sending messages (no expiration)

        **Key difference:** When you provide an external `url`, we download and process the file on every send.
        When you use a pre-uploaded `attachment_id`, the file is already stored — so repeated sends skip the download step entirely.

        ## Domain Allowlisting

        Attachment URLs in API responses are served from `cdn.linqapp.com`. This includes:
        - `url` fields in media and voice memo message parts
        - `download_url` fields in attachment and upload response objects

        If your application enforces domain allowlists (e.g., for SSRF protection), add:

        ```
        cdn.linqapp.com
        ```

        ## Supported File Types

        - **Images:** JPEG, PNG, GIF, HEIC, HEIF, TIFF, BMP
        - **Videos:** MP4, MOV, M4V
        - **Audio:** M4A, AAC, MP3, WAV, AIFF, CAF, AMR
        - **Documents:** PDF, TXT, RTF, CSV, Office formats, ZIP
        - **Contact & Calendar:** VCF, ICS

        ## Audio: Attachment vs Voice Memo

        Audio files sent as media parts appear as **downloadable file attachments** in iMessage.
        To send audio as an **iMessage voice memo bubble** (with native inline playback UI),
        use the dedicated `POST /v3/chats/{chatId}/voicememo` endpoint instead.

        ## File Size Limits

        - **URL-based (`url` field):** 10MB maximum
        - **Pre-upload (`attachment_id`):** 100MB maximum

        ## Security & Ownership

        Every attachment is bound to the partner account that created or received it. The API enforces ownership on every operation that touches an attachment — sending, retrieving, deleting.

        **What this means for you:**

        - An attachment created under your API key can only be referenced by your API key.
        - Submitting another partner's `attachment_id` returns `404 Not Found`. We do not disclose whether the id exists or belongs to someone else.
        - Submitting a CDN URL that resolves to another partner's attachment is rejected before the send is attempted.
        - Ownership enforcement applies uniformly across send, create-chat, voice memo, retrieve, and delete operations.

        Every attachment-affecting endpoint requires a valid partner API key. Unauthenticated calls return `401 Unauthorized`.

        ## Attachment URL Patterns

        Attachment URLs in API responses and webhook payloads use one of two layouts, depending on the attachment's tier:

        | Tier | URL pattern | TTL |
        |---|---|---|
        | Persistent (default) | `https://cdn.linqapp.com/attachments/partners/{partner_id}/{attachment_id}/{filename}` | Long-lived |
        | Ephemeral | Pre-signed URL pointing at the ephemeral prefix on `cdn.linqapp.com` | 15 minutes per signed URL — re-fetch via the API for a fresh URL |

        Inbound media you receive over webhooks uses the same layout your outbound sends produce, so the URL you store and the URL you build look identical — no special casing in your client.

        ## Ephemeral Attachments (Privacy Tier)

        For regulated or sensitive content, opt in to the **ephemeral attachments** tier by contacting your Linq support contact. You can request it at two scopes:

        | Scope | Effect |
        |---|---|
        | **Partner-wide** | Every outbound and inbound attachment on every phone number under your account is routed through the ephemeral tier. |
        | **Per phone number** | Only the specified phone numbers route their attachments through the ephemeral tier. The rest stay on the persistent tier. |

        **Behavioral differences vs the persistent default:**

        | Aspect | Persistent | Ephemeral |
        |---|---|---|
        | Download URL form | Long-lived CDN URL | Pre-signed URL with short TTL |
        | Retention floor | Indefinite (until you call `DELETE`) | **Hard backstop: 1 day** — even without an explicit `DELETE`, the platform removes the underlying bytes after 24 hours |
        | URL re-fetch | Not required | Fetch via `GET /v3/attachments/{attachmentId}` for a fresh signed URL after TTL expiry |
        | Cross-partner isolation | Enforced | Enforced |

        **When to choose ephemeral:**

        - Your downstream system processes the file immediately on receipt and does not need to re-read it later.
        - You have a compliance requirement that the platform must not retain attachments beyond a short window.
        - The content is high-sensitivity (PHI, financial documents, identity verification) and you do not want it sitting behind a long-lived URL.

        **Important:** ephemeral applies in *both directions* — outbound files you upload **and** inbound media received by the phone numbers in that scope. Download bytes you need to keep promptly, or fetch a fresh signed URL via the API when needed.

        ## Deleting an Attachment

        To permanently remove an attachment you own, use:

        ```http
        DELETE /v3/attachments/{attachmentId}
        Authorization: Bearer <your_api_key>
        ```

        **What this does:**

        1. Verifies the attachment is owned by your account. Returns `404` otherwise.
        2. Removes the underlying file from Linq storage.
        3. Records an audit entry (timestamp, partner, attachment id).

        **Response codes:**

        | Status | Meaning |
        |---|---|
        | `204 No Content` | Deletion succeeded. The attachment is removed from Linq storage. |
        | `400 Bad Request` | `attachmentId` is not a valid UUID. |
        | `401 Unauthorized` | Missing or invalid API key. |
        | `404 Not Found` | Attachment does not exist or is not owned by your account. |
        | `500 Internal Server Error` | Transient infrastructure issue — safe to retry. |

        **Effect on message history:**

        - Messages that referenced the deleted attachment remain visible.
        - The message part that pointed at the attachment is preserved with no attachment reference.
        - Webhook payloads previously delivered to you retain the original URL string, but downloads from that URL return `404` going forward.

        Deletion is **irreversible**. Once `204` is returned, the bytes are gone — there is no undelete.

        ## Inbound Media Flow

        When one of your phone numbers receives a message with media (image, video, audio, document), the platform:

        1. Stores the file under your partner account.
        2. Records metadata linked to the inbound message.
        3. Delivers a webhook whose `parts[]` array includes a `media` part with a `url` pointing at `cdn.linqapp.com`.
        4. If the receiving phone is opted in to ephemeral, the `url` is a short-TTL signed URL.

        You can acknowledge the webhook without fetching the file inline, and lazy-load via `GET /v3/attachments/{attachmentId}` later. For ephemeral attachments, retrieving via the API always returns a freshly-signed URL.

        ## Data Lifecycle Summary

        | Data | Persistent tier | Ephemeral tier |
        |---|---|---|
        | Attachment bytes | Retained until you `DELETE` | **Auto-removed after 1 day**, also removable via `DELETE` |
        | Attachment metadata (id, filename, mime type, size) | Retained until you `DELETE` | Removed alongside the bytes |
        | Message body & parts | Retained per message-retention policy | Retained per message-retention policy — unless the line also has **ephemeral messages** enabled (see the Messages page), in which case the message and its parts are deleted 24 hours after creation |
        | Audit log of deletions | Retained per platform retention policy | Retained per platform retention policy |

        **In transit:** TLS 1.2+ everywhere. **At rest:** AES-256 (server-side encryption).

        ## Compliance Checklist

        If you're integrating Linq under a security or privacy review, here is the short list:

        - Allowlist exactly one outbound domain: `cdn.linqapp.com`.
        - Decide whether you need ephemeral attachments (high-sensitivity content) — request enablement through your Linq support contact.
        - Implement `DELETE /v3/attachments/{attachmentId}` calls in your deletion workflow.
        - Persist any attachments your application needs long-term — Linq is the authoritative source until you delete, but the ephemeral tier auto-purges after 1 day.
        - For audit: every deletion is logged on Linq's side. Surface a confirmation in your application UI based on the `204` response.
        - For end-user "right to delete" requests: enumerate attachment ids and `DELETE` each. The platform does not provide a partner-wide wipe endpoint — deletion is per-attachment by design.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithStreamingResponse

        return AsyncAttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def phonenumbers(self) -> phonenumbers.AsyncPhonenumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phonenumbers import AsyncPhonenumbersResourceWithStreamingResponse

        return AsyncPhonenumbersResourceWithStreamingResponse(self._client.phonenumbers)

    @cached_property
    def phone_numbers(self) -> phone_numbers.AsyncPhoneNumbersResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.phone_numbers import AsyncPhoneNumbersResourceWithStreamingResponse

        return AsyncPhoneNumbersResourceWithStreamingResponse(self._client.phone_numbers)

    @cached_property
    def available_number(self) -> available_number.AsyncAvailableNumberResourceWithStreamingResponse:
        """Phone Numbers represent the phone numbers assigned to your partner account.

        Use the list phone numbers endpoint to discover which phone numbers are available
        for sending messages.

        When creating chats, listing chats, or sending a voice memo, use one of your assigned phone numbers
        in the `from` field.

        **Ineligible numbers.** A number can temporarily lose the ability to deliver messages.
        While it is in that state, requests that would produce new activity on it — sending a
        message, creating a chat, reacting, typing, group actions — are rejected with `403`
        (error code `2027`) before anything is created. Reads keep working, so your existing
        chats, messages, and history stay available. Omit `from` on `POST /v3/messages` and we
        pick an eligible number for you, skipping ineligible ones; if none of your assigned
        numbers are eligible, you get `409` (no `from` number was ever chosen, so there's no
        specific number to blame with a `403`).
        """
        from .resources.available_number import AsyncAvailableNumberResourceWithStreamingResponse

        return AsyncAvailableNumberResourceWithStreamingResponse(self._client.available_number)

    @cached_property
    def payment_requests(self) -> payment_requests.AsyncPaymentRequestsResourceWithStreamingResponse:
        """Request a payment from a recipient over iMessage.

        You create a payment
        request, send its `checkout_url` to the recipient, and they pay with Apple
        Pay or card. Funds settle **directly to your own Stripe account** — Linq
        never holds the money.

        ## How it works

        1. **Create** a payment request with an amount and currency. You get back a
           `checkout_url` and a `status` of `requested`.
        2. **Send** the `checkout_url` to the recipient as a `link` message part so
           it arrives as a tappable card (see *Sending the link* below).
        3. The recipient **pays** on the hosted checkout (Apple Pay App Clip on a
           supported iPhone, web checkout everywhere else).
        4. You receive a **`payment.succeeded`** webhook and the request's `status`
           becomes `succeeded`. Requests you don't collect eventually `expire`.

        ## Connected accounts (Stripe Standard, direct charges)

        Payments run on **Stripe Connect Standard accounts** using **direct
        charges**: the charge is created on *your* connected account and **you are
        the merchant of record**. That means the money, the payout schedule, the
        customer relationship, and the compliance surface are all yours — Linq
        orchestrates the request and the checkout but is never in the funds flow.

        **Refunds, disputes, and chargebacks are handled by you, in your own Stripe
        Dashboard.** Because charges settle directly to your account, Linq has no
        custody of the funds and cannot issue refunds or contest disputes on your
        behalf — and there is no refund/dispute endpoint in this API by design. Use
        the Stripe Dashboard (or the Stripe API on your own account) for the money
        lifecycle after a payment succeeds.

        ## Getting set up

        Open **Agent Pay** in your Linq dashboard
        (`https://zero.linqapp.com/organization/payments`), click **Connect Stripe**,
        and complete Stripe's onboarding (business details + a bank account). When
        your account reaches `charges_enabled`, request creation unlocks; until you
        connect Stripe, `POST /v3/payment_requests` returns `403`. You can keep
        collecting even while Stripe finishes background verification.

        ## Subscriptions

        Set `mode: subscription` on `POST /v3/payment_requests` to start an
        **auto-renewing subscription** instead of a one-time charge. Instead of an
        amount, you pass a `price_id` — an active **recurring Price** on your
        connected Stripe account (create one in your Stripe Dashboard under
        Product catalog; if you sell through Stripe Payment Links today, reuse the
        price your link is built from). The recipient pays the first invoice at
        the same checkout, and their payment method is saved to the subscription
        for automatic renewals.

        The division of labor is deliberate: **Linq handles the first payment,
        your Stripe account handles the rest.** The request reaches `succeeded`
        when the first invoice is paid; from then on the subscription lives
        entirely on your connected account. The response's `stripe` object gives
        you the join keys — `customer_id` and `subscription_id` — so renewals,
        plan changes, dunning, and cancellation are managed with your own Stripe
        Dashboard/API and your own Stripe webhooks. Your `metadata` is stamped on
        the Customer and Subscription, so correlating in either direction is
        trivial. There are no renewal webhooks from Linq by design.

        ### Discounts

        Pass a `discount` with a **coupon** or **promotion code** from your
        connected Stripe account to apply it to the subscription. Create either in
        your Stripe Dashboard under Product catalog → Coupons; Linq only forwards
        the id.

        ```json
        {
          "mode": "subscription",
          "price_id": "price_1QAbCdEfGhIjKlMn",
          "discount": {
            "coupon": "7fKCMvBh",
            "label": "50% OFF FIRST MONTH"
          }
        }
        ```

        Stripe applies the coupon and prices the first invoice; the `amount` we
        return is that invoice's amount due, so a `$50.00/month` price with a
        50%-off-first-month coupon comes back as `2500` and the recipient is
        charged **$25.00** at checkout. A coupon that covers the whole first
        invoice returns `amount: 0`; checkout shows $0.00 and collects the card for
        the renewal rather than charging now. Renewals bill at the full price
        automatically — how long a discount lasts is the coupon's `duration`,
        enforced by Stripe on your account, and Linq never re-prices anything.

        Use `promotion_code` instead of `coupon` to apply a promotion code by id
        (`promo_...`, not the customer-facing code string); pass one or the other,
        never both.

        `label` is the customer-facing promotion name displayed at checkout instead
        of the coupon or promotion code ID. The label is displayed exactly as
        provided, so include important terms such as "FIRST MONTH" or
        "FIRST 3 MONTHS" when applicable. These terms are not displayed elsewhere
        on the checkout screen.

        If omitted, Stripe uses the coupon's name as the promotion label.

        ### Free trials

        Add `trial_period_days` (or a fixed `trial_end` timestamp) to start the
        subscription with a free trial. The checkout still collects the
        recipient's payment method — the pay sheet shows "$0 due today" with the
        first charge date — and saves it to the subscription; Stripe bills it
        automatically when the trial ends. The request reaches `succeeded` when
        the card is collected, and the response carries `trial_end`. If the trial
        would end without a payment method on file, the subscription cancels
        rather than generating unpayable invoices. Trial lifecycle after checkout
        (extending, ending early) is managed in your own Stripe account via
        `stripe.subscription_id`.

        A subscription request you cancel (or that expires unpaid) cancels the
        incomplete Stripe subscription — nothing lingers on your account.

        ## Pre-created customers

        By default each request stands alone: payment mode attaches no Customer,
        and subscription mode creates a fresh one. If you already manage
        Customers on your connected account, pass their id as `customer_id`
        (`cus_...`) on create — in payment mode the charge lands on that
        customer's payment history, and in subscription mode the subscription is
        created on them instead of on a new Customer. The id must reference an
        existing, non-deleted customer on your connected account or the request
        fails with `400`. We never modify a customer you pass — no metadata is
        stamped on it.

        ## Sending the link

        Deliver the `checkout_url` as a **`link` message part** via
        `POST /v3/chats/{chatId}/messages` — it renders as a rich card with your
        branding (title, amount, image) instead of a bare URL, which converts far
        better. A `link` part must be the only part in the message. See
        [Rich Link Previews](/guides/messaging/sending-messages).

        On a supported iPhone the link opens an **Apple Pay App Clip** — a native,
        no-install checkout sheet. Everywhere else (Android, desktop, iPhones
        without the App Clip yet) the same URL opens the web checkout, so the link
        always works. The App Clip experience for your payment links is registered
        automatically by Linq and refreshed whenever you update your payments
        branding; a newly registered experience can take up to ~24 hours to
        activate on Apple's side, during which links open the web checkout.

        ## Sending it as a card instead

        A `link` part is one way to deliver a request. The other is the
        **`agentpay` experience**, which sends the same request as a native card
        in Linq's iMessage app — the amount and reason are drawn in the bubble,
        and it turns itself into "Paid" in place once the payment succeeds,
        without a second message.

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

        `checkout_url` is the only required field — pass back exactly what
        `POST /v3/payment_requests` returned. **The amount and reason are read
        from that request, never from you**, so the card can never claim a
        different figure than the checkout will charge. Optional `title` and
        `note` override the copy only. The link must be one of your own payment
        requests; another partner's is rejected.

        The trade-off against a `link` part: a card is an app card, so it is
        iMessage-only, and recipients without the app see a static version of it.
        A link works everywhere and is what opens the Apple Pay App Clip. Send
        whichever suits the conversation — both settle the same payment request
        and fire the same webhooks.

        ## Webhooks

        Subscribe to payment lifecycle events to reconcile server-side rather than
        polling: `payment.succeeded`, `payment.canceled`, and `payment.expired`.
        Each event carries the payment request id, amount, currency, and your
        `metadata`. See [Webhooks](/guides/webhooks).
        """
        from .resources.payment_requests import AsyncPaymentRequestsResourceWithStreamingResponse

        return AsyncPaymentRequestsResourceWithStreamingResponse(self._client.payment_requests)

    @cached_property
    def payment_providers(self) -> payment_providers.AsyncPaymentProvidersResourceWithStreamingResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_providers import AsyncPaymentProvidersResourceWithStreamingResponse

        return AsyncPaymentProvidersResourceWithStreamingResponse(self._client.payment_providers)

    @cached_property
    def payment_handles(self) -> payment_handles.AsyncPaymentHandlesResourceWithStreamingResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payment_handles import AsyncPaymentHandlesResourceWithStreamingResponse

        return AsyncPaymentHandlesResourceWithStreamingResponse(self._client.payment_handles)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        """
        Let an agent pay on a customer's behalf with a single-use virtual card.
        Connect a customer once, then create a payment — a virtual card is minted
        scoped to that purchase and the card details are handed back for checkout.
        """
        from .resources.payments import AsyncPaymentsResourceWithStreamingResponse

        return AsyncPaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def blocked_handles(self) -> blocked_handles.AsyncBlockedHandlesResourceWithStreamingResponse:
        """Block handles — phone numbers, email addresses, SMS short codes, or
        sender IDs.

        Inbound messages from a blocked handle are dropped before
        they reach your webhooks, and direct sends to a blocked handle are
        rejected with `403` (error code `2026`). Group sends that include
        unblocked members are not restricted.
        """
        from .resources.blocked_handles import AsyncBlockedHandlesResourceWithStreamingResponse

        return AsyncBlockedHandlesResourceWithStreamingResponse(self._client.blocked_handles)

    @cached_property
    def experiences(self) -> experiences.AsyncExperiencesResourceWithStreamingResponse:
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
        from .resources.experiences import AsyncExperiencesResourceWithStreamingResponse

        return AsyncExperiencesResourceWithStreamingResponse(self._client.experiences)

    @cached_property
    def webhook_events(self) -> webhook_events.AsyncWebhookEventsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_events import AsyncWebhookEventsResourceWithStreamingResponse

        return AsyncWebhookEventsResourceWithStreamingResponse(self._client.webhook_events)

    @cached_property
    def webhook_subscriptions(self) -> webhook_subscriptions.AsyncWebhookSubscriptionsResourceWithStreamingResponse:
        """
        Webhook Subscriptions allow you to receive real-time notifications when events
        occur on your account.

        Configure webhook endpoints to receive events such as messages sent/received,
        delivery status changes, reactions, typing indicators, and more.

        Failed deliveries (5xx, 429, network errors) are retried up to 10 times over
        ~25 minutes with exponential backoff. Each event includes a unique ID for
        deduplication.

        ## Webhook Headers

        All webhook requests include two sets of headers. **If you have an existing integration
        using the `X-Webhook-*` headers, nothing changes** — those headers are still sent on
        every delivery and work exactly as before. The new `webhook-*` headers follow the
        [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) specification.
        You can safely ignore them if your current verification code works and you don't want to use this convention.

        ### Standard Webhooks Headers (Recommended)

        Used by [our SDK](https://github.com/linq-team/linq-node) and any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks).

        | Header | Description |
        |--------|-------------|
        | `webhook-id` | Unique event identifier (use as idempotency key) |
        | `webhook-timestamp` | Unix timestamp (seconds) when the webhook was sent |
        | `webhook-signature` | Standard Webhooks signature (`v1,{base64}` format) |

        ### Legacy Headers (Deprecated)

        Still sent on every delivery for backwards compatibility. Existing verification code
        using these headers continues to work — no changes required.

        | Header | Description |
        |--------|-------------|
        | `X-Webhook-Event` | *(deprecated)* Event type (e.g., `message.sent`) |
        | `X-Webhook-Subscription-ID` | *(deprecated)* Webhook subscription ID |
        | `X-Webhook-Timestamp` | *(deprecated)* Unix timestamp (seconds) |
        | `X-Webhook-Signature` | *(deprecated)* HMAC-SHA256 signature (hex-encoded) |

        ## Signing Secrets

        Signing secrets use the Standard Webhooks format: a `whsec_` prefix followed
        by base64-encoded random bytes (e.g., `whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw7Jxx2Oll+OE=`).

        Strip the `whsec_` prefix and base64-decode the remainder to get the raw key bytes.

        ## Verifying Webhook Signatures

        Webhooks are signed following the [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks).
        You can use any [Standard Webhooks library](https://github.com/standard-webhooks/standard-webhooks) to verify
        signatures, or implement verification manually:

        **Signed content:** `{webhook-id}.{webhook-timestamp}.{body}`

        **Verification Steps:**

        1. Extract the `webhook-id`, `webhook-timestamp`, and `webhook-signature` headers
        2. Reject if the timestamp is more than 5 minutes old (replay protection)
        3. Get the raw request body bytes (do not parse and re-serialize)
        4. Construct signed content: `"{webhook-id}.{webhook-timestamp}.{body}"`
        5. Strip the `whsec_` prefix from your secret and base64-decode to get key bytes
        6. Compute HMAC-SHA256 using the key bytes over the signed content
        7. Base64-encode the result and compare with the value after `v1,` in `webhook-signature`
        8. Use constant-time comparison to prevent timing attacks

        **Example (Python):**

        ```python
        import base64, hmac, hashlib


        def verify_webhook(secret, body, headers):
            msg_id = headers["webhook-id"]
            timestamp = headers["webhook-timestamp"]
            signature = headers["webhook-signature"]

            secret_str = secret.removeprefix("whsec_")
            key = base64.b64decode(secret_str)

            signed_content = f"{msg_id}.{timestamp}.{body}"
            expected = base64.b64encode(hmac.new(key, signed_content.encode(), hashlib.sha256).digest()).decode()

            for sig in signature.split(" "):
                if sig.startswith("v1,") and hmac.compare_digest(expected, sig[3:]):
                    return True
            return False
        ```

        **Example (Node.js):**

        ```javascript
        const crypto = require('crypto');

        function verifyWebhook(secret, rawBody, headers) {
          const msgId = headers['webhook-id'];
          const timestamp = headers['webhook-timestamp'];
          const signature = headers['webhook-signature'];

          const secretStr = secret.startsWith('whsec_') ? secret.slice(6) : secret;
          const keyBytes = Buffer.from(secretStr, 'base64');
          const signedContent = `${msgId}.${timestamp}.${rawBody}`;
          const expected = crypto
            .createHmac('sha256', keyBytes)
            .update(signedContent)
            .digest('base64');

          return signature.split(' ').some(sig => {
            if (!sig.startsWith('v1,')) return false;
            try {
              return crypto.timingSafeEqual(
                Buffer.from(expected, 'base64'),
                Buffer.from(sig.slice(3), 'base64')
              );
            } catch { return false; }
          });
        }
        ```

        **Security Best Practices:**

        - Reject webhooks with timestamps older than 5 minutes to prevent replay attacks
        - Always use constant-time comparison for signature verification
        - Store your signing secret securely (e.g., environment variable, secrets manager)
        - Return a 2xx status code quickly, then process the webhook asynchronously
        """
        from .resources.webhook_subscriptions import AsyncWebhookSubscriptionsResourceWithStreamingResponse

        return AsyncWebhookSubscriptionsResourceWithStreamingResponse(self._client.webhook_subscriptions)

    @cached_property
    def capability(self) -> capability.AsyncCapabilityResourceWithStreamingResponse:
        """
        Check whether a recipient address supports iMessage or RCS before sending a message.
        """
        from .resources.capability import AsyncCapabilityResourceWithStreamingResponse

        return AsyncCapabilityResourceWithStreamingResponse(self._client.capability)

    @cached_property
    def contact_card(self) -> contact_card.AsyncContactCardResourceWithStreamingResponse:
        """
        Contact Card lets you set and share your contact information (name and profile photo) with chat participants via iMessage Name and Photo Sharing.

        Use `POST /v3/contact_card` to create or update a card for a phone number.
        Use `PATCH /v3/contact_card` to update an existing active card.
        Use `GET /v3/contact_card` to retrieve the active card(s) for your partner account.

        **Sharing behavior:** Sharing may not take effect in every chat due to limitations outside our control. We recommend calling the share endpoint once per day, after the first outbound activity.
        """
        from .resources.contact_card import AsyncContactCardResourceWithStreamingResponse

        return AsyncContactCardResourceWithStreamingResponse(self._client.contact_card)


Client = LinqAPIV3

AsyncClient = AsyncLinqAPIV3
