# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from tests.utils import assert_matches_type
from linq.types.chats import (
    ParticipantAddResponse,
    ParticipantRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParticipants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: LinqAPIV3) -> None:
        participant = client.chats.participants.add(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )
        assert_matches_type(ParticipantAddResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: LinqAPIV3) -> None:
        response = client.chats.participants.with_raw_response.add(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantAddResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: LinqAPIV3) -> None:
        with client.chats.participants.with_streaming_response.add(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantAddResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.participants.with_raw_response.add(
                chat_id="",
                handle="+12052499136",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: LinqAPIV3) -> None:
        participant = client.chats.participants.remove(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )
        assert_matches_type(ParticipantRemoveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: LinqAPIV3) -> None:
        response = client.chats.participants.with_raw_response.remove(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(ParticipantRemoveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: LinqAPIV3) -> None:
        with client.chats.participants.with_streaming_response.remove(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(ParticipantRemoveResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.participants.with_raw_response.remove(
                chat_id="",
                handle="+12052499136",
            )


class TestAsyncParticipants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncLinqAPIV3) -> None:
        participant = await async_client.chats.participants.add(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )
        assert_matches_type(ParticipantAddResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.participants.with_raw_response.add(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantAddResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.participants.with_streaming_response.add(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantAddResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.participants.with_raw_response.add(
                chat_id="",
                handle="+12052499136",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncLinqAPIV3) -> None:
        participant = await async_client.chats.participants.remove(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )
        assert_matches_type(ParticipantRemoveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.participants.with_raw_response.remove(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(ParticipantRemoveResponse, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.participants.with_streaming_response.remove(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            handle="+12052499136",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(ParticipantRemoveResponse, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.participants.with_raw_response.remove(
                chat_id="",
                handle="+12052499136",
            )
