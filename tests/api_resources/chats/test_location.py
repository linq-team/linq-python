# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from tests.utils import assert_matches_type
from linq.types.chats import GetChatLocationResponse, LocationRequestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        location = client.chats.location.retrieve(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )
        assert_matches_type(GetChatLocationResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.chats.location.with_raw_response.retrieve(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(GetChatLocationResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.chats.location.with_streaming_response.retrieve(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(GetChatLocationResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.location.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request(self, client: LinqAPIV3) -> None:
        location = client.chats.location.request(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )
        assert_matches_type(LocationRequestResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request(self, client: LinqAPIV3) -> None:
        response = client.chats.location.with_raw_response.request(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationRequestResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request(self, client: LinqAPIV3) -> None:
        with client.chats.location.with_streaming_response.request(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationRequestResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.location.with_raw_response.request(
                "",
            )


class TestAsyncLocation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        location = await async_client.chats.location.retrieve(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )
        assert_matches_type(GetChatLocationResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.location.with_raw_response.retrieve(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(GetChatLocationResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.location.with_streaming_response.retrieve(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(GetChatLocationResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.location.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request(self, async_client: AsyncLinqAPIV3) -> None:
        location = await async_client.chats.location.request(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )
        assert_matches_type(LocationRequestResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.location.with_raw_response.request(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationRequestResponse, location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.location.with_streaming_response.request(
            "975d0776-bd17-4273-8337-f346b4c661b0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationRequestResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.location.with_raw_response.request(
                "",
            )
