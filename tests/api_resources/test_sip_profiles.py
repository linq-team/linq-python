# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linq import LinqAPIV3, AsyncLinqAPIV3
from linq.types import (
    SipProfile,
    SipProfileListResponse,
    SipProfileAssignResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSipProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
            backup_uri="sips:inbound-backup@sip.partner.example",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LinqAPIV3) -> None:
        response = client.sip_profiles.with_raw_response.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = response.parse()
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LinqAPIV3) -> None:
        with client.sip_profiles.with_streaming_response.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = response.parse()
            assert_matches_type(SipProfile, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.retrieve(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LinqAPIV3) -> None:
        response = client.sip_profiles.with_raw_response.retrieve(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = response.parse()
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LinqAPIV3) -> None:
        with client.sip_profiles.with_streaming_response.retrieve(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = response.parse()
            assert_matches_type(SipProfile, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sip_profile_id` but received ''"):
            client.sip_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
            backup_uri="backup_uri",
            name="byoc-east",
            primary_uri="primary_uri",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LinqAPIV3) -> None:
        response = client.sip_profiles.with_raw_response.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = response.parse()
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LinqAPIV3) -> None:
        with client.sip_profiles.with_streaming_response.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = response.parse()
            assert_matches_type(SipProfile, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sip_profile_id` but received ''"):
            client.sip_profiles.with_raw_response.update(
                sip_profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.list()
        assert_matches_type(SipProfileListResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LinqAPIV3) -> None:
        response = client.sip_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = response.parse()
        assert_matches_type(SipProfileListResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LinqAPIV3) -> None:
        with client.sip_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = response.parse()
            assert_matches_type(SipProfileListResponse, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.delete(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert sip_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LinqAPIV3) -> None:
        response = client.sip_profiles.with_raw_response.delete(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = response.parse()
        assert sip_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LinqAPIV3) -> None:
        with client.sip_profiles.with_streaming_response.delete(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = response.parse()
            assert sip_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sip_profile_id` but received ''"):
            client.sip_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assign(self, client: LinqAPIV3) -> None:
        sip_profile = client.sip_profiles.assign(
            phone_number="+14254758217",
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert_matches_type(SipProfileAssignResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_assign(self, client: LinqAPIV3) -> None:
        response = client.sip_profiles.with_raw_response.assign(
            phone_number="+14254758217",
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = response.parse()
        assert_matches_type(SipProfileAssignResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_assign(self, client: LinqAPIV3) -> None:
        with client.sip_profiles.with_streaming_response.assign(
            phone_number="+14254758217",
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = response.parse()
            assert_matches_type(SipProfileAssignResponse, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_assign(self, client: LinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.sip_profiles.with_raw_response.assign(
                phone_number="",
                sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
            )


class TestAsyncSipProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
            backup_uri="sips:inbound-backup@sip.partner.example",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.sip_profiles.with_raw_response.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = await response.parse()
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.sip_profiles.with_streaming_response.create(
            name="byoc-primary",
            primary_uri="sips:sip.partner.example",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = await response.parse()
            assert_matches_type(SipProfile, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.retrieve(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.sip_profiles.with_raw_response.retrieve(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = await response.parse()
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.sip_profiles.with_streaming_response.retrieve(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = await response.parse()
            assert_matches_type(SipProfile, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sip_profile_id` but received ''"):
            await async_client.sip_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
            backup_uri="backup_uri",
            name="byoc-east",
            primary_uri="primary_uri",
        )
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.sip_profiles.with_raw_response.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = await response.parse()
        assert_matches_type(SipProfile, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.sip_profiles.with_streaming_response.update(
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = await response.parse()
            assert_matches_type(SipProfile, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sip_profile_id` but received ''"):
            await async_client.sip_profiles.with_raw_response.update(
                sip_profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.list()
        assert_matches_type(SipProfileListResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.sip_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = await response.parse()
        assert_matches_type(SipProfileListResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.sip_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = await response.parse()
            assert_matches_type(SipProfileListResponse, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.delete(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert sip_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.sip_profiles.with_raw_response.delete(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = await response.parse()
        assert sip_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.sip_profiles.with_streaming_response.delete(
            "sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = await response.parse()
            assert sip_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sip_profile_id` but received ''"):
            await async_client.sip_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assign(self, async_client: AsyncLinqAPIV3) -> None:
        sip_profile = await async_client.sip_profiles.assign(
            phone_number="+14254758217",
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )
        assert_matches_type(SipProfileAssignResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncLinqAPIV3) -> None:
        response = await async_client.sip_profiles.with_raw_response.assign(
            phone_number="+14254758217",
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_profile = await response.parse()
        assert_matches_type(SipProfileAssignResponse, sip_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncLinqAPIV3) -> None:
        async with async_client.sip_profiles.with_streaming_response.assign(
            phone_number="+14254758217",
            sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_profile = await response.parse()
            assert_matches_type(SipProfileAssignResponse, sip_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_assign(self, async_client: AsyncLinqAPIV3) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.sip_profiles.with_raw_response.assign(
                phone_number="",
                sip_profile_id="sip_8a3f9c2b1d4e4f5a9b8c7d6e5f4a3b2c",
            )
