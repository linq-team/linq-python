# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import HandleCheckResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCapability:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_i_message(self, client: LinqAPIV3) -> None:
        capability = client.capability.check_i_message(
            address="+15551234567",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_i_message_with_all_params(self, client: LinqAPIV3) -> None:
        capability = client.capability.check_i_message(
            address="+15551234567",
            from_="+15559876543",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_i_message(self, client: LinqAPIV3) -> None:
        response = client.capability.with_raw_response.check_i_message(
            address="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_i_message(self, client: LinqAPIV3) -> None:
        with client.capability.with_streaming_response.check_i_message(
            address="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(HandleCheckResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_RCS(self, client: LinqAPIV3) -> None:
        capability = client.capability.check_RCS(
            address="+15551234567",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_RCS_with_all_params(self, client: LinqAPIV3) -> None:
        capability = client.capability.check_RCS(
            address="+15551234567",
            from_="+15559876543",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_RCS(self, client: LinqAPIV3) -> None:
        response = client.capability.with_raw_response.check_RCS(
            address="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_RCS(self, client: LinqAPIV3) -> None:
        with client.capability.with_streaming_response.check_RCS(
            address="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(HandleCheckResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCapability:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_i_message(self, async_client: AsyncLinqAPIV3) -> None:
        capability = await async_client.capability.check_i_message(
            address="+15551234567",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_i_message_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        capability = await async_client.capability.check_i_message(
            address="+15551234567",
            from_="+15559876543",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_i_message(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.capability.with_raw_response.check_i_message(
            address="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_i_message(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.capability.with_streaming_response.check_i_message(
            address="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(HandleCheckResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_RCS(self, async_client: AsyncLinqAPIV3) -> None:
        capability = await async_client.capability.check_RCS(
            address="+15551234567",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_RCS_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        capability = await async_client.capability.check_RCS(
            address="+15551234567",
            from_="+15559876543",
        )
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_RCS(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.capability.with_raw_response.check_RCS(
            address="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(HandleCheckResponse, capability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_RCS(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.capability.with_streaming_response.check_RCS(
            address="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(HandleCheckResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True
