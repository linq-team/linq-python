# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBackground:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: LinqAPIV3) -> None:
        background = client.chats.background.remove(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: LinqAPIV3) -> None:
        response = client.chats.background.with_raw_response.remove(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        background = response.parse()
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: LinqAPIV3) -> None:
        with client.chats.background.with_streaming_response.remove(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            background = response.parse()
            assert background is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.background.with_raw_response.remove(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set(self, client: LinqAPIV3) -> None:
        background = client.chats.background.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
        )
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_with_all_params(self, client: LinqAPIV3) -> None:
        background = client.chats.background.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
            image_url="https://example.com",
            shades=["string", "string"],
            style="sky",
            variant="mango",
        )
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: LinqAPIV3) -> None:
        response = client.chats.background.with_raw_response.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        background = response.parse()
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: LinqAPIV3) -> None:
        with client.chats.background.with_streaming_response.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            background = response.parse()
            assert background is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.background.with_raw_response.set(
                chat_id="",
                type="color",
            )


class TestAsyncBackground:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncLinqAPIV3) -> None:
        background = await async_client.chats.background.remove(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.background.with_raw_response.remove(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        background = await response.parse()
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.background.with_streaming_response.remove(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            background = await response.parse()
            assert background is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.background.with_raw_response.remove(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncLinqAPIV3) -> None:
        background = await async_client.chats.background.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
        )
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        background = await async_client.chats.background.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
            image_url="https://example.com",
            shades=["string", "string"],
            style="sky",
            variant="mango",
        )
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.background.with_raw_response.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        background = await response.parse()
        assert background is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.background.with_streaming_response.set(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            type="color",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            background = await response.parse()
            assert background is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.background.with_raw_response.set(
                chat_id="",
                type="color",
            )
