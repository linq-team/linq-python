# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import CallVoiceRecord, CallVoiceListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallVoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        call_voice = client.call_voice.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CallVoiceRecord, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.call_voice.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_voice = response.parse()
        assert_matches_type(CallVoiceRecord, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.call_voice.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_voice = response.parse()
            assert_matches_type(CallVoiceRecord, call_voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_voice_id` but received ''"):
            client.call_voice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LinqAPIV3) -> None:
        call_voice = client.call_voice.list(
            phone_number="+14254758217",
        )
        assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LinqAPIV3) -> None:
        call_voice = client.call_voice.list(
            phone_number="+14254758217",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LinqAPIV3) -> None:
        response = client.call_voice.with_raw_response.list(
            phone_number="+14254758217",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_voice = response.parse()
        assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LinqAPIV3) -> None:
        with client.call_voice.with_streaming_response.list(
            phone_number="+14254758217",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_voice = response.parse()
            assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.call_voice.with_raw_response.list(
                phone_number="",
            )


class TestAsyncCallVoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        call_voice = await async_client.call_voice.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CallVoiceRecord, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.call_voice.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_voice = await response.parse()
        assert_matches_type(CallVoiceRecord, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.call_voice.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_voice = await response.parse()
            assert_matches_type(CallVoiceRecord, call_voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_voice_id` but received ''"):
            await async_client.call_voice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinqAPIV3) -> None:
        call_voice = await async_client.call_voice.list(
            phone_number="+14254758217",
        )
        assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        call_voice = await async_client.call_voice.list(
            phone_number="+14254758217",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.call_voice.with_raw_response.list(
            phone_number="+14254758217",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_voice = await response.parse()
        assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.call_voice.with_streaming_response.list(
            phone_number="+14254758217",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_voice = await response.parse()
            assert_matches_type(CallVoiceListResponse, call_voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.call_voice.with_raw_response.list(
                phone_number="",
            )
