# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bluehive import BlueHive, AsyncBlueHive
from tests.utils import assert_matches_type
from bluehive.types import Hl7ReplayResponse, Hl7ProcessResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHl7:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_results(self, client: BlueHive) -> None:
        hl7 = client.hl7.send_results(
            employee_id="employeeId",
            file={
                "base64": "base64",
                "name": "name",
                "type": "type",
            },
        )
        assert_matches_type(str, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_results(self, client: BlueHive) -> None:
        response = client.hl7.with_raw_response.send_results(
            employee_id="employeeId",
            file={
                "base64": "base64",
                "name": "name",
                "type": "type",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hl7 = response.parse()
        assert_matches_type(str, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_results(self, client: BlueHive) -> None:
        with client.hl7.with_streaming_response.send_results(
            employee_id="employeeId",
            file={
                "base64": "base64",
                "name": "name",
                "type": "type",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hl7 = response.parse()
            assert_matches_type(str, hl7, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process(self, client: BlueHive) -> None:
        hl7 = client.hl7.process()
        assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_with_all_params(self, client: BlueHive) -> None:
        hl7 = client.hl7.process(
            message={},
            f="f",
            interface="interface",
            login_user="login_user",
            login_passwd="login_passwd",
            message_b64="message_b64",
        )
        assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process(self, client: BlueHive) -> None:
        response = client.hl7.with_raw_response.process()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hl7 = response.parse()
        assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process(self, client: BlueHive) -> None:
        with client.hl7.with_streaming_response.process() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hl7 = response.parse()
            assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay(self, client: BlueHive) -> None:
        hl7 = client.hl7.replay(
            "logId",
        )
        assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay_with_all_params(self, client: BlueHive) -> None:
        hl7 = client.hl7.replay(
            "logId",
            destination={},
            interface_name="interface_name",
        )
        assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replay(self, client: BlueHive) -> None:
        response = client.hl7.with_raw_response.replay(
            "logId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hl7 = response.parse()
        assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replay(self, client: BlueHive) -> None:
        with client.hl7.with_streaming_response.replay(
            "logId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hl7 = response.parse()
            assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replay(self, client: BlueHive) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `log_id` but received ''"):
            client.hl7.with_raw_response.replay(
                "",
            )


class TestAsyncHl7:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_results(self, async_client: AsyncBlueHive) -> None:
        hl7 = await async_client.hl7.send_results(
            employee_id="employeeId",
            file={
                "base64": "base64",
                "name": "name",
                "type": "type",
            },
        )
        assert_matches_type(str, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_results(self, async_client: AsyncBlueHive) -> None:
        response = await async_client.hl7.with_raw_response.send_results(
            employee_id="employeeId",
            file={
                "base64": "base64",
                "name": "name",
                "type": "type",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hl7 = await response.parse()
        assert_matches_type(str, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_results(self, async_client: AsyncBlueHive) -> None:
        async with async_client.hl7.with_streaming_response.send_results(
            employee_id="employeeId",
            file={
                "base64": "base64",
                "name": "name",
                "type": "type",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hl7 = await response.parse()
            assert_matches_type(str, hl7, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process(self, async_client: AsyncBlueHive) -> None:
        hl7 = await async_client.hl7.process()
        assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_with_all_params(self, async_client: AsyncBlueHive) -> None:
        hl7 = await async_client.hl7.process(
            message={},
            f="f",
            interface="interface",
            login_user="login_user",
            login_passwd="login_passwd",
            message_b64="message_b64",
        )
        assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process(self, async_client: AsyncBlueHive) -> None:
        response = await async_client.hl7.with_raw_response.process()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hl7 = await response.parse()
        assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process(self, async_client: AsyncBlueHive) -> None:
        async with async_client.hl7.with_streaming_response.process() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hl7 = await response.parse()
            assert_matches_type(Hl7ProcessResponse, hl7, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay(self, async_client: AsyncBlueHive) -> None:
        hl7 = await async_client.hl7.replay(
            "logId",
        )
        assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay_with_all_params(self, async_client: AsyncBlueHive) -> None:
        hl7 = await async_client.hl7.replay(
            "logId",
            destination={},
            interface_name="interface_name",
        )
        assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replay(self, async_client: AsyncBlueHive) -> None:
        response = await async_client.hl7.with_raw_response.replay(
            "logId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hl7 = await response.parse()
        assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replay(self, async_client: AsyncBlueHive) -> None:
        async with async_client.hl7.with_streaming_response.replay(
            "logId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hl7 = await response.parse()
            assert_matches_type(Hl7ReplayResponse, hl7, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replay(self, async_client: AsyncBlueHive) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `log_id` but received ''"):
            await async_client.hl7.with_raw_response.replay(
                "",
            )
