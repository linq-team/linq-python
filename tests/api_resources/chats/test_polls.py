# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from tests.utils import assert_matches_type
from linq.types.chats import PollEnvelope

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LinqAPIV3) -> None:
        poll = client.chats.polls.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LinqAPIV3) -> None:
        poll = client.chats.polls.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={
                "options": [{"text": "Tacos"}, {"text": "Sushi"}],
                "idempotency_key": "poll-abc123",
            },
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LinqAPIV3) -> None:
        response = client.chats.polls.with_raw_response.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LinqAPIV3) -> None:
        with client.chats.polls.with_streaming_response.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.polls.with_raw_response.create(
                chat_id="",
                poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
            )


class TestAsyncPolls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLinqAPIV3) -> None:
        poll = await async_client.chats.polls.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        poll = await async_client.chats.polls.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={
                "options": [{"text": "Tacos"}, {"text": "Sushi"}],
                "idempotency_key": "poll-abc123",
            },
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.polls.with_raw_response.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = await response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.polls.with_streaming_response.create(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = await response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.polls.with_raw_response.create(
                chat_id="",
                poll={"options": [{"text": "Tacos"}, {"text": "Sushi"}]},
            )
