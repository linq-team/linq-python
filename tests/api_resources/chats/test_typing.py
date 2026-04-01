# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTyping:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: LinqAPIV3) -> None:
        typing = client.chats.typing.start(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: LinqAPIV3) -> None:
        response = client.chats.typing.with_raw_response.start(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typing = response.parse()
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: LinqAPIV3) -> None:
        with client.chats.typing.with_streaming_response.start(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            typing = response.parse()
            assert typing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.typing.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: LinqAPIV3) -> None:
        typing = client.chats.typing.stop(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: LinqAPIV3) -> None:
        response = client.chats.typing.with_raw_response.stop(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typing = response.parse()
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: LinqAPIV3) -> None:
        with client.chats.typing.with_streaming_response.stop(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            typing = response.parse()
            assert typing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.typing.with_raw_response.stop(
                "",
            )


class TestAsyncTyping:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncLinqAPIV3) -> None:
        typing = await async_client.chats.typing.start(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.typing.with_raw_response.start(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typing = await response.parse()
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.typing.with_streaming_response.start(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            typing = await response.parse()
            assert typing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.typing.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncLinqAPIV3) -> None:
        typing = await async_client.chats.typing.stop(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.typing.with_raw_response.stop(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typing = await response.parse()
        assert typing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.typing.with_streaming_response.stop(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            typing = await response.parse()
            assert typing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.typing.with_raw_response.stop(
                "",
            )
