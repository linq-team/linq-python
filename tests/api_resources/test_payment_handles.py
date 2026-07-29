# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import PaymentHandleConnection
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentHandles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: LinqAPIV3) -> None:
        payment_handle = client.payment_handles.connect(
            "handle",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: LinqAPIV3) -> None:
        response = client.payment_handles.with_raw_response.connect(
            "handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: LinqAPIV3) -> None:
        with client.payment_handles.with_streaming_response.connect(
            "handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.payment_handles.with_raw_response.connect(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connection(self, client: LinqAPIV3) -> None:
        payment_handle = client.payment_handles.connection(
            "handle",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connection(self, client: LinqAPIV3) -> None:
        response = client.payment_handles.with_raw_response.connection(
            "handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connection(self, client: LinqAPIV3) -> None:
        with client.payment_handles.with_streaming_response.connection(
            "handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_connection(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.payment_handles.with_raw_response.connection(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: LinqAPIV3) -> None:
        payment_handle = client.payment_handles.revoke(
            "handle",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: LinqAPIV3) -> None:
        response = client.payment_handles.with_raw_response.revoke(
            "handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: LinqAPIV3) -> None:
        with client.payment_handles.with_streaming_response.revoke(
            "handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.payment_handles.with_raw_response.revoke(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: LinqAPIV3) -> None:
        payment_handle = client.payment_handles.verify(
            handle="handle",
            code="482913",
            connect_id="cs_01HZY8",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: LinqAPIV3) -> None:
        response = client.payment_handles.with_raw_response.verify(
            handle="handle",
            code="482913",
            connect_id="cs_01HZY8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: LinqAPIV3) -> None:
        with client.payment_handles.with_streaming_response.verify(
            handle="handle",
            code="482913",
            connect_id="cs_01HZY8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_verify(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.payment_handles.with_raw_response.verify(
                handle="",
                code="482913",
                connect_id="cs_01HZY8",
            )


class TestAsyncPaymentHandles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncLinqAPIV3) -> None:
        payment_handle = await async_client.payment_handles.connect(
            "handle",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.payment_handles.with_raw_response.connect(
            "handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = await response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.payment_handles.with_streaming_response.connect(
            "handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = await response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.payment_handles.with_raw_response.connect(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connection(self, async_client: AsyncLinqAPIV3) -> None:
        payment_handle = await async_client.payment_handles.connection(
            "handle",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connection(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.payment_handles.with_raw_response.connection(
            "handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = await response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connection(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.payment_handles.with_streaming_response.connection(
            "handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = await response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_connection(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.payment_handles.with_raw_response.connection(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncLinqAPIV3) -> None:
        payment_handle = await async_client.payment_handles.revoke(
            "handle",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.payment_handles.with_raw_response.revoke(
            "handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = await response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.payment_handles.with_streaming_response.revoke(
            "handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = await response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.payment_handles.with_raw_response.revoke(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncLinqAPIV3) -> None:
        payment_handle = await async_client.payment_handles.verify(
            handle="handle",
            code="482913",
            connect_id="cs_01HZY8",
        )
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.payment_handles.with_raw_response.verify(
            handle="handle",
            code="482913",
            connect_id="cs_01HZY8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_handle = await response.parse()
        assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.payment_handles.with_streaming_response.verify(
            handle="handle",
            code="482913",
            connect_id="cs_01HZY8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_handle = await response.parse()
            assert_matches_type(PaymentHandleConnection, payment_handle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.payment_handles.with_raw_response.verify(
                handle="",
                code="482913",
                connect_id="cs_01HZY8",
            )
