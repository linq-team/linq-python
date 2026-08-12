# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import (
    ReputationAudit,
    ReputationAuditStarted,
    PhoneNumberListResponse,
    PhoneNumberUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LinqAPIV3) -> None:
        phone_number = client.phone_numbers.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarding_number="+12025559999",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LinqAPIV3) -> None:
        response = client.phone_numbers.with_raw_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarding_number="+12025559999",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LinqAPIV3) -> None:
        with client.phone_numbers.with_streaming_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarding_number="+12025559999",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_numbers.with_raw_response.update(
                phone_number_id="",
                forwarding_number="+12025559999",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LinqAPIV3) -> None:
        phone_number = client.phone_numbers.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LinqAPIV3) -> None:
        response = client.phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LinqAPIV3) -> None:
        with client.phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_reputation_audit(self, client: LinqAPIV3) -> None:
        phone_number = client.phone_numbers.get_reputation_audit(
            audit_id="auditId",
            phone_number="phoneNumber",
        )
        assert_matches_type(ReputationAudit, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_reputation_audit(self, client: LinqAPIV3) -> None:
        response = client.phone_numbers.with_raw_response.get_reputation_audit(
            audit_id="auditId",
            phone_number="phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(ReputationAudit, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_reputation_audit(self, client: LinqAPIV3) -> None:
        with client.phone_numbers.with_streaming_response.get_reputation_audit(
            audit_id="auditId",
            phone_number="phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(ReputationAudit, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_reputation_audit(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_numbers.with_raw_response.get_reputation_audit(
                audit_id="auditId",
                phone_number="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            client.phone_numbers.with_raw_response.get_reputation_audit(
                audit_id="",
                phone_number="phoneNumber",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_reputation_audit(self, client: LinqAPIV3) -> None:
        phone_number = client.phone_numbers.start_reputation_audit(
            "phoneNumber",
        )
        assert_matches_type(ReputationAuditStarted, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_reputation_audit(self, client: LinqAPIV3) -> None:
        response = client.phone_numbers.with_raw_response.start_reputation_audit(
            "phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(ReputationAuditStarted, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_reputation_audit(self, client: LinqAPIV3) -> None:
        with client.phone_numbers.with_streaming_response.start_reputation_audit(
            "phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(ReputationAuditStarted, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start_reputation_audit(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_numbers.with_raw_response.start_reputation_audit(
                "",
            )


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinqAPIV3) -> None:
        phone_number = await async_client.phone_numbers.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarding_number="+12025559999",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.phone_numbers.with_raw_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarding_number="+12025559999",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.phone_numbers.with_streaming_response.update(
            phone_number_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            forwarding_number="+12025559999",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_numbers.with_raw_response.update(
                phone_number_id="",
                forwarding_number="+12025559999",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinqAPIV3) -> None:
        phone_number = await async_client.phone_numbers.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        phone_number = await async_client.phone_numbers.get_reputation_audit(
            audit_id="auditId",
            phone_number="phoneNumber",
        )
        assert_matches_type(ReputationAudit, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.phone_numbers.with_raw_response.get_reputation_audit(
            audit_id="auditId",
            phone_number="phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(ReputationAudit, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.phone_numbers.with_streaming_response.get_reputation_audit(
            audit_id="auditId",
            phone_number="phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(ReputationAudit, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_numbers.with_raw_response.get_reputation_audit(
                audit_id="auditId",
                phone_number="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            await async_client.phone_numbers.with_raw_response.get_reputation_audit(
                audit_id="",
                phone_number="phoneNumber",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        phone_number = await async_client.phone_numbers.start_reputation_audit(
            "phoneNumber",
        )
        assert_matches_type(ReputationAuditStarted, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.phone_numbers.with_raw_response.start_reputation_audit(
            "phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(ReputationAuditStarted, phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.phone_numbers.with_streaming_response.start_reputation_audit(
            "phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(ReputationAuditStarted, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start_reputation_audit(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_numbers.with_raw_response.start_reputation_audit(
                "",
            )
