# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import SnapshotExportResponse, SnapshotImportResponse
from nebula._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_export(self, client: Nebula) -> None:
        snapshot = client.snapshots.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotExportResponse, snapshot, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Nebula) -> None:
        response = client.snapshots.with_raw_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotExportResponse, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Nebula) -> None:
        with client.snapshots.with_streaming_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotExportResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_import(self, client: Nebula) -> None:
        snapshot = client.snapshots.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
            },
        )
        assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

    @parametrize
    def test_method_import_with_all_params(self, client: Nebula) -> None:
        snapshot = client.snapshots.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "format_version": 0,
                "generation": 0,
                "graph": {
                    "entities": [
                        {
                            "id": "id",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "engram_id": "engram_id",
                            "name": "name",
                            "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "category": "category",
                            "chunk_ids": ["string"],
                            "collection_id": "collection_id",
                            "description": "description",
                            "fts_terms": {"foo": 0},
                            "metadata": {"foo": "bar"},
                            "relationship_count": 0,
                        }
                    ],
                    "entity_description_embeddings": {
                        "dim": 0,
                        "encoding": "npy-base64",
                        "mask_b64": "mask_b64",
                        "values_b64": "values_b64",
                    },
                    "relationship_description_embeddings": {
                        "dim": 0,
                        "encoding": "npy-base64",
                        "mask_b64": "mask_b64",
                        "values_b64": "values_b64",
                    },
                    "relationship_relation_embeddings": {
                        "dim": 0,
                        "encoding": "npy-base64",
                        "mask_b64": "mask_b64",
                        "values_b64": "values_b64",
                    },
                    "relationships": [
                        {
                            "id": "id",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "object_id": "object_id",
                            "subject_id": "subject_id",
                            "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "category": "category",
                            "chunk_ids": ["string"],
                            "collection_id": "collection_id",
                            "description": "description",
                            "engram_id": "engram_id",
                            "inference_metadata": {"foo": "bar"},
                            "metadata": {"foo": "bar"},
                            "object": "object",
                            "predicate": "predicate",
                            "relationship_type": "relationship_type",
                            "subject": "subject",
                            "temporal_precision": "temporal_precision",
                            "valid_span": {"foo": "bar"},
                            "weight": 0,
                        }
                    ],
                },
            },
        )
        assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Nebula) -> None:
        response = client.snapshots.with_raw_response.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Nebula) -> None:
        with client.snapshots.with_streaming_response.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_export(self, async_client: AsyncNebula) -> None:
        snapshot = await async_client.snapshots.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SnapshotExportResponse, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncNebula) -> None:
        response = await async_client.snapshots.with_raw_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotExportResponse, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncNebula) -> None:
        async with async_client.snapshots.with_streaming_response.export(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotExportResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_import(self, async_client: AsyncNebula) -> None:
        snapshot = await async_client.snapshots.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
            },
        )
        assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncNebula) -> None:
        snapshot = await async_client.snapshots.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "format_version": 0,
                "generation": 0,
                "graph": {
                    "entities": [
                        {
                            "id": "id",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "engram_id": "engram_id",
                            "name": "name",
                            "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "category": "category",
                            "chunk_ids": ["string"],
                            "collection_id": "collection_id",
                            "description": "description",
                            "fts_terms": {"foo": 0},
                            "metadata": {"foo": "bar"},
                            "relationship_count": 0,
                        }
                    ],
                    "entity_description_embeddings": {
                        "dim": 0,
                        "encoding": "npy-base64",
                        "mask_b64": "mask_b64",
                        "values_b64": "values_b64",
                    },
                    "relationship_description_embeddings": {
                        "dim": 0,
                        "encoding": "npy-base64",
                        "mask_b64": "mask_b64",
                        "values_b64": "values_b64",
                    },
                    "relationship_relation_embeddings": {
                        "dim": 0,
                        "encoding": "npy-base64",
                        "mask_b64": "mask_b64",
                        "values_b64": "values_b64",
                    },
                    "relationships": [
                        {
                            "id": "id",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "object_id": "object_id",
                            "subject_id": "subject_id",
                            "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "category": "category",
                            "chunk_ids": ["string"],
                            "collection_id": "collection_id",
                            "description": "description",
                            "engram_id": "engram_id",
                            "inference_metadata": {"foo": "bar"},
                            "metadata": {"foo": "bar"},
                            "object": "object",
                            "predicate": "predicate",
                            "relationship_type": "relationship_type",
                            "subject": "subject",
                            "temporal_precision": "temporal_precision",
                            "valid_span": {"foo": "bar"},
                            "weight": 0,
                        }
                    ],
                },
            },
        )
        assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncNebula) -> None:
        response = await async_client.snapshots.with_raw_response.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncNebula) -> None:
        async with async_client.snapshots.with_streaming_response.import_(
            snapshot={
                "collection_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "root_hash": "root_hash",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotImportResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True
