# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import (
    Chat,
    ChatCreateResponse,
    ChatUpdateResponse,
    ChatLeaveChatResponse,
    ChatSendVoicememoResponse,
)
from tests.utils import assert_matches_type
from linq.pagination import SyncListChatsPagination, AsyncListChatsPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LinqAPIV3) -> None:
        chat = client.chats.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                    }
                ]
            },
            to=["+12052532136"],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LinqAPIV3) -> None:
        chat = client.chats.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                        "text_decorations": [
                            {
                                "range": [0, 5],
                                "animation": "shake",
                                "style": "bold",
                            },
                            {
                                "range": [6, 11],
                                "animation": "shake",
                                "style": "bold",
                            },
                        ],
                    }
                ],
                "effect": {
                    "name": "confetti",
                    "type": "screen",
                },
                "idempotency_key": "msg-abc123xyz",
                "preferred_service": "iMessage",
                "reply_to": {
                    "message_id": "550e8400-e29b-41d4-a716-446655440000",
                    "part_index": 0,
                },
            },
            to=["+12052532136"],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                    }
                ]
            },
            to=["+12052532136"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                    }
                ]
            },
            to=["+12052532136"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        chat = client.chats.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LinqAPIV3) -> None:
        chat = client.chats.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LinqAPIV3) -> None:
        chat = client.chats.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            display_name="Team Discussion",
            group_chat_icon="https://example.com/icon.png",
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatUpdateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.update(
                chat_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_leave_chat(self, client: LinqAPIV3) -> None:
        chat = client.chats.leave_chat(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ChatLeaveChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_leave_chat(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.leave_chat(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatLeaveChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_leave_chat(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.leave_chat(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatLeaveChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_leave_chat(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.leave_chat(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_chats(self, client: LinqAPIV3) -> None:
        chat = client.chats.list_chats()
        assert_matches_type(SyncListChatsPagination[Chat], chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_chats_with_all_params(self, client: LinqAPIV3) -> None:
        chat = client.chats.list_chats(
            cursor="20",
            from_="+13343284472",
            limit=20,
            to="+13343284472",
        )
        assert_matches_type(SyncListChatsPagination[Chat], chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_chats(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.list_chats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(SyncListChatsPagination[Chat], chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_chats(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.list_chats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(SyncListChatsPagination[Chat], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_as_read(self, client: LinqAPIV3) -> None:
        chat = client.chats.mark_as_read(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_as_read(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.mark_as_read(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_as_read(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.mark_as_read(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_mark_as_read(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.mark_as_read(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_voicememo(self, client: LinqAPIV3) -> None:
        chat = client.chats.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
        )
        assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_voicememo_with_all_params(self, client: LinqAPIV3) -> None:
        chat = client.chats.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
            attachment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_memo_url="https://example.com/voice-memo.m4a",
        )
        assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_voicememo(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_voicememo(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_voicememo(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.send_voicememo(
                chat_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_share_contact_card(self, client: LinqAPIV3) -> None:
        chat = client.chats.share_contact_card(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_share_contact_card(self, client: LinqAPIV3) -> None:
        response = client.chats.with_raw_response.share_contact_card(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_share_contact_card(self, client: LinqAPIV3) -> None:
        with client.chats.with_streaming_response.share_contact_card(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_share_contact_card(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.share_contact_card(
                "",
            )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                    }
                ]
            },
            to=["+12052532136"],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                        "text_decorations": [
                            {
                                "range": [0, 5],
                                "animation": "shake",
                                "style": "bold",
                            },
                            {
                                "range": [6, 11],
                                "animation": "shake",
                                "style": "bold",
                            },
                        ],
                    }
                ],
                "effect": {
                    "name": "confetti",
                    "type": "screen",
                },
                "idempotency_key": "msg-abc123xyz",
                "preferred_service": "iMessage",
                "reply_to": {
                    "message_id": "550e8400-e29b-41d4-a716-446655440000",
                    "part_index": 0,
                },
            },
            to=["+12052532136"],
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                    }
                ]
            },
            to=["+12052532136"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.create(
            from_="+12052535597",
            message={
                "parts": [
                    {
                        "type": "text",
                        "value": "Hello! How can I help you today?",
                    }
                ]
            },
            to=["+12052532136"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
            display_name="Team Discussion",
            group_chat_icon="https://example.com/icon.png",
        )
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatUpdateResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.update(
            chat_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatUpdateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.update(
                chat_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_leave_chat(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.leave_chat(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ChatLeaveChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_leave_chat(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.leave_chat(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatLeaveChatResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_leave_chat(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.leave_chat(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatLeaveChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_leave_chat(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.leave_chat(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_chats(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.list_chats()
        assert_matches_type(AsyncListChatsPagination[Chat], chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_chats_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.list_chats(
            cursor="20",
            from_="+13343284472",
            limit=20,
            to="+13343284472",
        )
        assert_matches_type(AsyncListChatsPagination[Chat], chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_chats(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.list_chats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(AsyncListChatsPagination[Chat], chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_chats(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.list_chats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(AsyncListChatsPagination[Chat], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_as_read(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.mark_as_read(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_as_read(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.mark_as_read(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_as_read(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.mark_as_read(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_mark_as_read(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.mark_as_read(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_voicememo(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
        )
        assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_voicememo_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
            attachment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            voice_memo_url="https://example.com/voice-memo.m4a",
        )
        assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_voicememo(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_voicememo(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.send_voicememo(
            chat_id="f19ee7b8-8533-4c5c-83ec-4ef8d6d1ddbd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSendVoicememoResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_voicememo(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.send_voicememo(
                chat_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_share_contact_card(self, async_client: AsyncLinqAPIV3) -> None:
        chat = await async_client.chats.share_contact_card(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_share_contact_card(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.chats.with_raw_response.share_contact_card(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_share_contact_card(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.chats.with_streaming_response.share_contact_card(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_share_contact_card(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.share_contact_card(
                "",
            )
