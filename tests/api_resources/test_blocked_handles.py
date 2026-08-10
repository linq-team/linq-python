# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import (
    BlockedHandleListResponse,
    BlockedHandleBlockResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlockedHandles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LinqAPIV3) -> None:
        blocked_handle = client.blocked_handles.list()
        assert_matches_type(BlockedHandleListResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LinqAPIV3) -> None:
        response = client.blocked_handles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_handle = response.parse()
        assert_matches_type(BlockedHandleListResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LinqAPIV3) -> None:
        with client.blocked_handles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_handle = response.parse()
            assert_matches_type(BlockedHandleListResponse, blocked_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_block(self, client: LinqAPIV3) -> None:
        blocked_handle = client.blocked_handles.block(
            handle="+12025551234",
        )
        assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_block_with_all_params(self, client: LinqAPIV3) -> None:
        blocked_handle = client.blocked_handles.block(
            handle="+12025551234",
            reason="spam",
        )
        assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_block(self, client: LinqAPIV3) -> None:
        response = client.blocked_handles.with_raw_response.block(
            handle="+12025551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_handle = response.parse()
        assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_block(self, client: LinqAPIV3) -> None:
        with client.blocked_handles.with_streaming_response.block(
            handle="+12025551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_handle = response.parse()
            assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unblock(self, client: LinqAPIV3) -> None:
        blocked_handle = client.blocked_handles.unblock(
            handle="+12025551234",
        )
        assert blocked_handle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unblock(self, client: LinqAPIV3) -> None:
        response = client.blocked_handles.with_raw_response.unblock(
            handle="+12025551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_handle = response.parse()
        assert blocked_handle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unblock(self, client: LinqAPIV3) -> None:
        with client.blocked_handles.with_streaming_response.unblock(
            handle="+12025551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_handle = response.parse()
            assert blocked_handle is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBlockedHandles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinqAPIV3) -> None:
        blocked_handle = await async_client.blocked_handles.list()
        assert_matches_type(BlockedHandleListResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.blocked_handles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_handle = await response.parse()
        assert_matches_type(BlockedHandleListResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.blocked_handles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_handle = await response.parse()
            assert_matches_type(BlockedHandleListResponse, blocked_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_block(self, async_client: AsyncLinqAPIV3) -> None:
        blocked_handle = await async_client.blocked_handles.block(
            handle="+12025551234",
        )
        assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_block_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        blocked_handle = await async_client.blocked_handles.block(
            handle="+12025551234",
            reason="spam",
        )
        assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_block(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.blocked_handles.with_raw_response.block(
            handle="+12025551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_handle = await response.parse()
        assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_block(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.blocked_handles.with_streaming_response.block(
            handle="+12025551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_handle = await response.parse()
            assert_matches_type(BlockedHandleBlockResponse, blocked_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unblock(self, async_client: AsyncLinqAPIV3) -> None:
        blocked_handle = await async_client.blocked_handles.unblock(
            handle="+12025551234",
        )
        assert blocked_handle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unblock(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.blocked_handles.with_raw_response.unblock(
            handle="+12025551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_handle = await response.parse()
        assert blocked_handle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unblock(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.blocked_handles.with_streaming_response.unblock(
            handle="+12025551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_handle = await response.parse()
            assert blocked_handle is None

        assert cast(Any, response.is_closed) is True
