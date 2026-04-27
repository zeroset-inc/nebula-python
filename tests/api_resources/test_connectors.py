# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    ConnectorListResponse,
    ConnectorSyncResponse,
    ConnectorConnectResponse,
    ConnectorRetrieveResponse,
    ConnectorDisconnectResponse,
    ConnectorListProvidersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        connector = client.connectors.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.connectors.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.connectors.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connectors.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        connector = client.connectors.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorListResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.connectors.with_raw_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorListResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.connectors.with_streaming_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorListResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_connect(self, client: Nebula) -> None:
        connector = client.connectors.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

    @parametrize
    def test_method_connect_with_all_params(self, client: Nebula) -> None:
        connector = client.connectors.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={"foo": "bar"},
        )
        assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_connect(self, client: Nebula) -> None:
        response = client.connectors.with_raw_response.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_connect(self, client: Nebula) -> None:
        with client.connectors.with_streaming_response.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.connectors.with_raw_response.connect(
                provider="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_disconnect(self, client: Nebula) -> None:
        connector = client.connectors.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

    @parametrize
    def test_method_disconnect_with_all_params(self, client: Nebula) -> None:
        connector = client.connectors.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delete_memories=True,
        )
        assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_disconnect(self, client: Nebula) -> None:
        response = client.connectors.with_raw_response.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_disconnect(self, client: Nebula) -> None:
        with client.connectors.with_streaming_response.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disconnect(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connectors.with_raw_response.disconnect(
                connection_id="",
            )

    @parametrize
    def test_method_list_providers(self, client: Nebula) -> None:
        connector = client.connectors.list_providers()
        assert_matches_type(ConnectorListProvidersResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_list_providers(self, client: Nebula) -> None:
        response = client.connectors.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorListProvidersResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_list_providers(self, client: Nebula) -> None:
        with client.connectors.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorListProvidersResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_sync(self, client: Nebula) -> None:
        connector = client.connectors.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorSyncResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_sync(self, client: Nebula) -> None:
        response = client.connectors.with_raw_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorSyncResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_sync(self, client: Nebula) -> None:
        with client.connectors.with_streaming_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorSyncResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connectors.with_raw_response.sync(
                "",
            )


class TestAsyncConnectors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.connectors.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.connectors.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connectors.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorListResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.connectors.with_raw_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorListResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.connectors.with_streaming_response.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorListResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_connect(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={"foo": "bar"},
        )
        assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncNebula) -> None:
        response = await async_client.connectors.with_raw_response.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncNebula) -> None:
        async with async_client.connectors.with_streaming_response.connect(
            provider="provider",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorConnectResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.connectors.with_raw_response.connect(
                provider="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_disconnect(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

    @parametrize
    async def test_method_disconnect_with_all_params(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delete_memories=True,
        )
        assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncNebula) -> None:
        response = await async_client.connectors.with_raw_response.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncNebula) -> None:
        async with async_client.connectors.with_streaming_response.disconnect(
            connection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorDisconnectResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disconnect(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connectors.with_raw_response.disconnect(
                connection_id="",
            )

    @parametrize
    async def test_method_list_providers(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.list_providers()
        assert_matches_type(ConnectorListProvidersResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_list_providers(self, async_client: AsyncNebula) -> None:
        response = await async_client.connectors.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorListProvidersResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_list_providers(self, async_client: AsyncNebula) -> None:
        async with async_client.connectors.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorListProvidersResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_sync(self, async_client: AsyncNebula) -> None:
        connector = await async_client.connectors.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorSyncResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncNebula) -> None:
        response = await async_client.connectors.with_raw_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorSyncResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncNebula) -> None:
        async with async_client.connectors.with_streaming_response.sync(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorSyncResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connectors.with_raw_response.sync(
                "",
            )
