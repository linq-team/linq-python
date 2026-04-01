# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import PhonenumberListResponse
from tests.utils import assert_matches_type

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhonenumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LinqAPIV3) -> None:
        with pytest.warns(DeprecationWarning):
            phonenumber = client.phonenumbers.list()

        assert_matches_type(PhonenumberListResponse, phonenumber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LinqAPIV3) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.phonenumbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phonenumber = response.parse()
        assert_matches_type(PhonenumberListResponse, phonenumber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LinqAPIV3) -> None:
        with pytest.warns(DeprecationWarning):
            with client.phonenumbers.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                phonenumber = response.parse()
                assert_matches_type(PhonenumberListResponse, phonenumber, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhonenumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.warns(DeprecationWarning):
            phonenumber = await async_client.phonenumbers.list()

        assert_matches_type(PhonenumberListResponse, phonenumber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.phonenumbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phonenumber = await response.parse()
        assert_matches_type(PhonenumberListResponse, phonenumber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.phonenumbers.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                phonenumber = await response.parse()
                assert_matches_type(PhonenumberListResponse, phonenumber, path=["response"])

        assert cast(Any, response.is_closed) is True
