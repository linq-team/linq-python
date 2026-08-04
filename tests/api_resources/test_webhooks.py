# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from datetime import datetime, timezone

import pytest
import standardwebhooks

from linq import LinqAPIV3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_unwrap(self, client: LinqAPIV3, client_opt: str | None, method_opt: str | bytes | None) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        client = client.with_options(webhook_secret=client_opt)

        data = """{"api_version":"v3","created_at":"2025-11-23T17:30:00Z","data":{"id":"550e8400-e29b-41d4-a716-446655440001","chat":{"id":"550e8400-e29b-41d4-a716-446655440000","health_status":{"doc_url":"https://docs.linqapp.com/guides/chats/chat-health#at-risk","status":"AT_RISK","updated_at":"2026-05-01T18:28:25Z"},"is_group":true,"owner_handle":{"id":"550e8400-e29b-41d4-a716-446655440000","handle":"+15551234567","joined_at":"2025-05-21T15:30:00.000-05:00","service":"iMessage","is_me":false,"left_at":"2019-12-27T18:11:19.117Z","status":"active"}},"direction":"outbound","parts":[{"type":"text","value":"Hello!","text_decorations":[{"range":[0,5],"animation":"shake","style":"bold"}]}],"sender_handle":{"id":"550e8400-e29b-41d4-a716-446655440000","handle":"+15551234567","joined_at":"2025-05-21T15:30:00.000-05:00","service":"iMessage","is_me":false,"left_at":"2019-12-27T18:11:19.117Z","status":"active"},"service":"iMessage","delivered_at":"2026-01-30T20:49:20.352Z","effect":{"name":"gentle","type":"bubble"},"idempotency_key":"unique-key","preferred_service":"iMessage","read_at":null,"reconciled_at":"2026-01-30T22:05:00.000Z","reply_to":{"message_id":"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e","part_index":0},"sent_at":"2026-01-30T20:49:19.704Z"},"event_id":"550e8400-e29b-41d4-a716-446655440000","event_type":"message.sent","partner_id":"partner_abc123","trace_id":"abc123def456","webhook_version":"2025-01-01"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=method_opt)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_unwrap(
        self, async_client: LinqAPIV3, client_opt: str | None, method_opt: str | bytes | None
    ) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        async_client = async_client.with_options(webhook_secret=client_opt)

        data = """{"api_version":"v3","created_at":"2025-11-23T17:30:00Z","data":{"id":"550e8400-e29b-41d4-a716-446655440001","chat":{"id":"550e8400-e29b-41d4-a716-446655440000","health_status":{"doc_url":"https://docs.linqapp.com/guides/chats/chat-health#at-risk","status":"AT_RISK","updated_at":"2026-05-01T18:28:25Z"},"is_group":true,"owner_handle":{"id":"550e8400-e29b-41d4-a716-446655440000","handle":"+15551234567","joined_at":"2025-05-21T15:30:00.000-05:00","service":"iMessage","is_me":false,"left_at":"2019-12-27T18:11:19.117Z","status":"active"}},"direction":"outbound","parts":[{"type":"text","value":"Hello!","text_decorations":[{"range":[0,5],"animation":"shake","style":"bold"}]}],"sender_handle":{"id":"550e8400-e29b-41d4-a716-446655440000","handle":"+15551234567","joined_at":"2025-05-21T15:30:00.000-05:00","service":"iMessage","is_me":false,"left_at":"2019-12-27T18:11:19.117Z","status":"active"},"service":"iMessage","delivered_at":"2026-01-30T20:49:20.352Z","effect":{"name":"gentle","type":"bubble"},"idempotency_key":"unique-key","preferred_service":"iMessage","read_at":null,"reconciled_at":"2026-01-30T22:05:00.000Z","reply_to":{"message_id":"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e","part_index":0},"sent_at":"2026-01-30T20:49:19.704Z"},"event_id":"550e8400-e29b-41d4-a716-446655440000","event_type":"message.sent","partner_id":"partner_abc123","trace_id":"abc123def456","webhook_version":"2025-01-01"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = async_client.webhooks.unwrap(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = async_client.webhooks.unwrap(data, headers=bad_header, key=method_opt)
