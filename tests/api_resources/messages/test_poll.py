# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from tests.utils import assert_matches_type
from linq.types.chats import PollEnvelope

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPoll:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        poll = client.messages.poll.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.messages.poll.with_raw_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.messages.poll.with_streaming_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.poll.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_options(self, client: LinqAPIV3) -> None:
        poll = client.messages.poll.add_options(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            options=[{"text": "Pizza"}],
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_options(self, client: LinqAPIV3) -> None:
        response = client.messages.poll.with_raw_response.add_options(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            options=[{"text": "Pizza"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_options(self, client: LinqAPIV3) -> None:
        with client.messages.poll.with_streaming_response.add_options(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            options=[{"text": "Pizza"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_options(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.poll.with_raw_response.add_options(
                message_id="",
                options=[{"text": "Pizza"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_vote(self, client: LinqAPIV3) -> None:
        poll = client.messages.poll.vote(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_vote(self, client: LinqAPIV3) -> None:
        response = client.messages.poll.with_raw_response.vote(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_vote(self, client: LinqAPIV3) -> None:
        with client.messages.poll.with_streaming_response.vote(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_vote(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.poll.with_raw_response.vote(
                message_id="",
                operation="add",
                option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
            )


class TestAsyncPoll:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        poll = await async_client.messages.poll.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.poll.with_raw_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = await response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.poll.with_streaming_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = await response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.poll.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_options(self, async_client: AsyncLinqAPIV3) -> None:
        poll = await async_client.messages.poll.add_options(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            options=[{"text": "Pizza"}],
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_options(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.poll.with_raw_response.add_options(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            options=[{"text": "Pizza"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = await response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_options(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.poll.with_streaming_response.add_options(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            options=[{"text": "Pizza"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = await response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_options(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.poll.with_raw_response.add_options(
                message_id="",
                options=[{"text": "Pizza"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_vote(self, async_client: AsyncLinqAPIV3) -> None:
        poll = await async_client.messages.poll.vote(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
        )
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_vote(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.poll.with_raw_response.vote(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll = await response.parse()
        assert_matches_type(PollEnvelope, poll, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_vote(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.poll.with_streaming_response.vote(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll = await response.parse()
            assert_matches_type(PollEnvelope, poll, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_vote(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.poll.with_raw_response.vote(
                message_id="",
                operation="add",
                option_id="97ce8c17-7ef6-4bbc-a89a-6b93d189712f",
            )
