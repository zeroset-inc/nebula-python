# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types.memories import NebulaResultsEngramResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_append(self, client: Nebula) -> None:
        metadata = client.memories.metadata.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_append(self, client: Nebula) -> None:
        response = client.memories.metadata.with_raw_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_append(self, client: Nebula) -> None:
        with client.memories.metadata.with_streaming_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_append(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.metadata.with_raw_response.append(
                id="",
                body=[{"foo": "bar"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Nebula) -> None:
        metadata = client.memories.metadata.replace(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Nebula) -> None:
        response = client.memories.metadata.with_raw_response.replace(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Nebula) -> None:
        with client.memories.metadata.with_streaming_response.replace(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.metadata.with_raw_response.replace(
                id="",
                body=[{"foo": "bar"}],
            )


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_append(self, async_client: AsyncNebula) -> None:
        metadata = await async_client.memories.metadata.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_append(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.metadata.with_raw_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_append(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.metadata.with_streaming_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_append(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.metadata.with_raw_response.append(
                id="",
                body=[{"foo": "bar"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncNebula) -> None:
        metadata = await async_client.memories.metadata.replace(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.metadata.with_raw_response.replace(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.metadata.with_streaming_response.replace(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[{"foo": "bar"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(NebulaResultsEngramResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.metadata.with_raw_response.replace(
                id="",
                body=[{"foo": "bar"}],
            )
