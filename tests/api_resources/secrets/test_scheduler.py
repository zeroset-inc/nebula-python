# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types.secrets import SchedulerStopResponse, SchedulerStartResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduler:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Nebula) -> None:
        scheduler = client.secrets.scheduler.start()
        assert_matches_type(SchedulerStartResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Nebula) -> None:
        response = client.secrets.scheduler.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduler = response.parse()
        assert_matches_type(SchedulerStartResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Nebula) -> None:
        with client.secrets.scheduler.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduler = response.parse()
            assert_matches_type(SchedulerStartResponse, scheduler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Nebula) -> None:
        scheduler = client.secrets.scheduler.stop()
        assert_matches_type(SchedulerStopResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Nebula) -> None:
        response = client.secrets.scheduler.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduler = response.parse()
        assert_matches_type(SchedulerStopResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Nebula) -> None:
        with client.secrets.scheduler.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduler = response.parse()
            assert_matches_type(SchedulerStopResponse, scheduler, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScheduler:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncNebula) -> None:
        scheduler = await async_client.secrets.scheduler.start()
        assert_matches_type(SchedulerStartResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncNebula) -> None:
        response = await async_client.secrets.scheduler.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduler = await response.parse()
        assert_matches_type(SchedulerStartResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncNebula) -> None:
        async with async_client.secrets.scheduler.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduler = await response.parse()
            assert_matches_type(SchedulerStartResponse, scheduler, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncNebula) -> None:
        scheduler = await async_client.secrets.scheduler.stop()
        assert_matches_type(SchedulerStopResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncNebula) -> None:
        response = await async_client.secrets.scheduler.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduler = await response.parse()
        assert_matches_type(SchedulerStopResponse, scheduler, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncNebula) -> None:
        async with async_client.secrets.scheduler.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduler = await response.parse()
            assert_matches_type(SchedulerStopResponse, scheduler, path=["response"])

        assert cast(Any, response.is_closed) is True
