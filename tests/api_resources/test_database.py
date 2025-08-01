# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bluehive import BlueHive, AsyncBlueHive
from tests.utils import assert_matches_type
from bluehive.types import DatabaseCheckHealthResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_health(self, client: BlueHive) -> None:
        database = client.database.check_health()
        assert_matches_type(DatabaseCheckHealthResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_health(self, client: BlueHive) -> None:
        response = client.database.with_raw_response.check_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseCheckHealthResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_health(self, client: BlueHive) -> None:
        with client.database.with_streaming_response.check_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseCheckHealthResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatabase:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_health(self, async_client: AsyncBlueHive) -> None:
        database = await async_client.database.check_health()
        assert_matches_type(DatabaseCheckHealthResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_health(self, async_client: AsyncBlueHive) -> None:
        response = await async_client.database.with_raw_response.check_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseCheckHealthResponse, database, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_health(self, async_client: AsyncBlueHive) -> None:
        async with async_client.database.with_streaming_response.check_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseCheckHealthResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True
