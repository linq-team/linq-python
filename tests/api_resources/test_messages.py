# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import (
    Message,
    MessageAddReactionResponse,
)
from tests.utils import assert_matches_type
from linq.pagination import SyncListMessagesPagination, AsyncListMessagesPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        message = client.messages.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.messages.with_raw_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.messages.with_streaming_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LinqAPIV3) -> None:
        message = client.messages.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LinqAPIV3) -> None:
        message = client.messages.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
            part_index=0,
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LinqAPIV3) -> None:
        response = client.messages.with_raw_response.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LinqAPIV3) -> None:
        with client.messages.with_streaming_response.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.update(
                message_id="",
                text="This is the edited message content",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LinqAPIV3) -> None:
        message = client.messages.delete(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LinqAPIV3) -> None:
        response = client.messages.with_raw_response.delete(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LinqAPIV3) -> None:
        with client.messages.with_streaming_response.delete(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_reaction(self, client: LinqAPIV3) -> None:
        message = client.messages.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
        )
        assert_matches_type(MessageAddReactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_reaction_with_all_params(self, client: LinqAPIV3) -> None:
        message = client.messages.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
            custom_emoji="custom_emoji",
            part_index=1,
        )
        assert_matches_type(MessageAddReactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_reaction(self, client: LinqAPIV3) -> None:
        response = client.messages.with_raw_response.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageAddReactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_reaction(self, client: LinqAPIV3) -> None:
        with client.messages.with_streaming_response.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageAddReactionResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_reaction(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.add_reaction(
                message_id="",
                operation="add",
                type="love",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_messages_thread(self, client: LinqAPIV3) -> None:
        message = client.messages.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert_matches_type(SyncListMessagesPagination[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_messages_thread_with_all_params(self, client: LinqAPIV3) -> None:
        message = client.messages.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            cursor="cursor",
            limit=1,
            order="asc",
        )
        assert_matches_type(SyncListMessagesPagination[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_messages_thread(self, client: LinqAPIV3) -> None:
        response = client.messages.with_raw_response.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncListMessagesPagination[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_messages_thread(self, client: LinqAPIV3) -> None:
        with client.messages.with_streaming_response.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncListMessagesPagination[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_messages_thread(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.list_messages_thread(
                message_id="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.with_raw_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.with_streaming_response.retrieve(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
            part_index=0,
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.with_raw_response.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.with_streaming_response.update(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            text="This is the edited message content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.update(
                message_id="",
                text="This is the edited message content",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.delete(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.with_raw_response.delete(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.with_streaming_response.delete(
            "69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_reaction(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
        )
        assert_matches_type(MessageAddReactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_reaction_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
            custom_emoji="custom_emoji",
            part_index=1,
        )
        assert_matches_type(MessageAddReactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_reaction(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.with_raw_response.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageAddReactionResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_reaction(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.with_streaming_response.add_reaction(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            operation="add",
            type="love",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageAddReactionResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_reaction(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.add_reaction(
                message_id="",
                operation="add",
                type="love",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_messages_thread(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )
        assert_matches_type(AsyncListMessagesPagination[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_messages_thread_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        message = await async_client.messages.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
            cursor="cursor",
            limit=1,
            order="asc",
        )
        assert_matches_type(AsyncListMessagesPagination[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_messages_thread(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.messages.with_raw_response.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncListMessagesPagination[Message], message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_messages_thread(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.messages.with_streaming_response.list_messages_thread(
            message_id="69a37c7d-af4f-4b5e-af42-e28e98ce873a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncListMessagesPagination[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_messages_thread(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.list_messages_thread(
                message_id="",
            )
