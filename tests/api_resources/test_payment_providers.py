# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import PaymentProvider, PaymentProviderConnectResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        payment_provider = client.payment_providers.retrieve(
            "provider",
        )
        assert_matches_type(PaymentProvider, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.payment_providers.with_raw_response.retrieve(
            "provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_provider = response.parse()
        assert_matches_type(PaymentProvider, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.payment_providers.with_streaming_response.retrieve(
            "provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_provider = response.parse()
            assert_matches_type(PaymentProvider, payment_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.payment_providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: LinqAPIV3) -> None:
        payment_provider = client.payment_providers.connect(
            provider="provider",
            return_url="https://partner.example/settings/payments",
        )
        assert_matches_type(PaymentProviderConnectResponse, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: LinqAPIV3) -> None:
        response = client.payment_providers.with_raw_response.connect(
            provider="provider",
            return_url="https://partner.example/settings/payments",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_provider = response.parse()
        assert_matches_type(PaymentProviderConnectResponse, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: LinqAPIV3) -> None:
        with client.payment_providers.with_streaming_response.connect(
            provider="provider",
            return_url="https://partner.example/settings/payments",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_provider = response.parse()
            assert_matches_type(PaymentProviderConnectResponse, payment_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.payment_providers.with_raw_response.connect(
                provider="",
                return_url="https://partner.example/settings/payments",
            )


class TestAsyncPaymentProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        payment_provider = await async_client.payment_providers.retrieve(
            "provider",
        )
        assert_matches_type(PaymentProvider, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.payment_providers.with_raw_response.retrieve(
            "provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_provider = await response.parse()
        assert_matches_type(PaymentProvider, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.payment_providers.with_streaming_response.retrieve(
            "provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_provider = await response.parse()
            assert_matches_type(PaymentProvider, payment_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.payment_providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncLinqAPIV3) -> None:
        payment_provider = await async_client.payment_providers.connect(
            provider="provider",
            return_url="https://partner.example/settings/payments",
        )
        assert_matches_type(PaymentProviderConnectResponse, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.payment_providers.with_raw_response.connect(
            provider="provider",
            return_url="https://partner.example/settings/payments",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_provider = await response.parse()
        assert_matches_type(PaymentProviderConnectResponse, payment_provider, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.payment_providers.with_streaming_response.connect(
            provider="provider",
            return_url="https://partner.example/settings/payments",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_provider = await response.parse()
            assert_matches_type(PaymentProviderConnectResponse, payment_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.payment_providers.with_raw_response.connect(
                provider="",
                return_url="https://partner.example/settings/payments",
            )
