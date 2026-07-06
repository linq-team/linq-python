# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import AvailableNumberRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvailableNumber:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        available_number = client.available_number.retrieve()
        assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LinqAPIV3) -> None:
        available_number = client.available_number.retrieve(
            to=["string"],
        )
        assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.available_number.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available_number = response.parse()
        assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.available_number.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available_number = response.parse()
            assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAvailableNumber:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        available_number = await async_client.available_number.retrieve()
        assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        available_number = await async_client.available_number.retrieve(
            to=["string"],
        )
        assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.available_number.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available_number = await response.parse()
        assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.available_number.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available_number = await response.parse()
            assert_matches_type(AvailableNumberRetrieveResponse, available_number, path=["response"])

        assert cast(Any, response.is_closed) is True
