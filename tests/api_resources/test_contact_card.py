# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import (
    SetContactCard,
    ContactCardRetrieveResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContactCard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LinqAPIV3) -> None:
        contact_card = client.contact_card.create(
            first_name="Acme",
            phone_number="+15551234567",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LinqAPIV3) -> None:
        contact_card = client.contact_card.create(
            first_name="Acme",
            phone_number="+15551234567",
            image_url="https://cdn.linqapp.com/contact-card/example.jpg",
            last_name="Support",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LinqAPIV3) -> None:
        response = client.contact_card.with_raw_response.create(
            first_name="Acme",
            phone_number="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = response.parse()
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LinqAPIV3) -> None:
        with client.contact_card.with_streaming_response.create(
            first_name="Acme",
            phone_number="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = response.parse()
            assert_matches_type(SetContactCard, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        contact_card = client.contact_card.retrieve()
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LinqAPIV3) -> None:
        contact_card = client.contact_card.retrieve(
            phone_number="+15551234567",
        )
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.contact_card.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = response.parse()
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.contact_card.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = response.parse()
            assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LinqAPIV3) -> None:
        contact_card = client.contact_card.update(
            phone_number="+15551234567",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LinqAPIV3) -> None:
        contact_card = client.contact_card.update(
            phone_number="+15551234567",
            first_name="John",
            image_url="https://cdn.linqapp.com/contact-card/example.jpg",
            last_name="Doe",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LinqAPIV3) -> None:
        response = client.contact_card.with_raw_response.update(
            phone_number="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = response.parse()
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LinqAPIV3) -> None:
        with client.contact_card.with_streaming_response.update(
            phone_number="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = response.parse()
            assert_matches_type(SetContactCard, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContactCard:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLinqAPIV3) -> None:
        contact_card = await async_client.contact_card.create(
            first_name="Acme",
            phone_number="+15551234567",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        contact_card = await async_client.contact_card.create(
            first_name="Acme",
            phone_number="+15551234567",
            image_url="https://cdn.linqapp.com/contact-card/example.jpg",
            last_name="Support",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.contact_card.with_raw_response.create(
            first_name="Acme",
            phone_number="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = await response.parse()
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.contact_card.with_streaming_response.create(
            first_name="Acme",
            phone_number="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = await response.parse()
            assert_matches_type(SetContactCard, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        contact_card = await async_client.contact_card.retrieve()
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        contact_card = await async_client.contact_card.retrieve(
            phone_number="+15551234567",
        )
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.contact_card.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = await response.parse()
        assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.contact_card.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = await response.parse()
            assert_matches_type(ContactCardRetrieveResponse, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinqAPIV3) -> None:
        contact_card = await async_client.contact_card.update(
            phone_number="+15551234567",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        contact_card = await async_client.contact_card.update(
            phone_number="+15551234567",
            first_name="John",
            image_url="https://cdn.linqapp.com/contact-card/example.jpg",
            last_name="Doe",
        )
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.contact_card.with_raw_response.update(
            phone_number="+15551234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact_card = await response.parse()
        assert_matches_type(SetContactCard, contact_card, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.contact_card.with_streaming_response.update(
            phone_number="+15551234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact_card = await response.parse()
            assert_matches_type(SetContactCard, contact_card, path=["response"])

        assert cast(Any, response.is_closed) is True
