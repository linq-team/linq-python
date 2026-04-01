# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import (
    WebhookSubscription,
    WebhookSubscriptionListResponse,
    WebhookSubscriptionCreateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LinqAPIV3) -> None:
        webhook_subscription = client.webhook_subscriptions.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
        )
        assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LinqAPIV3) -> None:
        webhook_subscription = client.webhook_subscriptions.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
            phone_numbers=["+12025551234", "+12025559876"],
        )
        assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LinqAPIV3) -> None:
        response = client.webhook_subscriptions.with_raw_response.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LinqAPIV3) -> None:
        with client.webhook_subscriptions.with_streaming_response.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        webhook_subscription = client.webhook_subscriptions.retrieve(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.webhook_subscriptions.with_raw_response.retrieve(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.webhook_subscriptions.with_streaming_response.retrieve(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.webhook_subscriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LinqAPIV3) -> None:
        webhook_subscription = client.webhook_subscriptions.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LinqAPIV3) -> None:
        webhook_subscription = client.webhook_subscriptions.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
            is_active=True,
            phone_numbers=["+12025551234"],
            subscribed_events=["message.sent", "message.delivered"],
            target_url="https://webhooks.example.com/linq/events",
        )
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LinqAPIV3) -> None:
        response = client.webhook_subscriptions.with_raw_response.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LinqAPIV3) -> None:
        with client.webhook_subscriptions.with_streaming_response.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.webhook_subscriptions.with_raw_response.update(
                subscription_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LinqAPIV3) -> None:
        webhook_subscription = client.webhook_subscriptions.list()
        assert_matches_type(WebhookSubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LinqAPIV3) -> None:
        response = client.webhook_subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert_matches_type(WebhookSubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LinqAPIV3) -> None:
        with client.webhook_subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert_matches_type(WebhookSubscriptionListResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LinqAPIV3) -> None:
        webhook_subscription = client.webhook_subscriptions.delete(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LinqAPIV3) -> None:
        response = client.webhook_subscriptions.with_raw_response.delete(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LinqAPIV3) -> None:
        with client.webhook_subscriptions.with_streaming_response.delete(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.webhook_subscriptions.with_raw_response.delete(
                "",
            )


class TestAsyncWebhookSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLinqAPIV3) -> None:
        webhook_subscription = await async_client.webhook_subscriptions.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
        )
        assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        webhook_subscription = await async_client.webhook_subscriptions.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
            phone_numbers=["+12025551234", "+12025559876"],
        )
        assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.webhook_subscriptions.with_raw_response.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.webhook_subscriptions.with_streaming_response.create(
            subscribed_events=["message.sent", "message.delivered", "message.read"],
            target_url="https://webhooks.example.com/linq/events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(WebhookSubscriptionCreateResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        webhook_subscription = await async_client.webhook_subscriptions.retrieve(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.webhook_subscriptions.with_raw_response.retrieve(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.webhook_subscriptions.with_streaming_response.retrieve(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.webhook_subscriptions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinqAPIV3) -> None:
        webhook_subscription = await async_client.webhook_subscriptions.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        webhook_subscription = await async_client.webhook_subscriptions.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
            is_active=True,
            phone_numbers=["+12025551234"],
            subscribed_events=["message.sent", "message.delivered"],
            target_url="https://webhooks.example.com/linq/events",
        )
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.webhook_subscriptions.with_raw_response.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.webhook_subscriptions.with_streaming_response.update(
            subscription_id="b2c3d4e5-f6a7-8901-bcde-f23456789012",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(WebhookSubscription, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.webhook_subscriptions.with_raw_response.update(
                subscription_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinqAPIV3) -> None:
        webhook_subscription = await async_client.webhook_subscriptions.list()
        assert_matches_type(WebhookSubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.webhook_subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert_matches_type(WebhookSubscriptionListResponse, webhook_subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.webhook_subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert_matches_type(WebhookSubscriptionListResponse, webhook_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLinqAPIV3) -> None:
        webhook_subscription = await async_client.webhook_subscriptions.delete(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.webhook_subscriptions.with_raw_response.delete(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_subscription = await response.parse()
        assert webhook_subscription is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.webhook_subscriptions.with_streaming_response.delete(
            "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_subscription = await response.parse()
            assert webhook_subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.webhook_subscriptions.with_raw_response.delete(
                "",
            )
