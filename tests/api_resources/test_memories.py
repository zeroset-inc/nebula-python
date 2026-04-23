# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    MemoryListResponse,
    MemoryAppendResponse,
    MemoryCreateResponse,
    MemoryDeleteResponse,
    MemorySearchResponse,
    MemoryUpdateResponse,
    MemoryRetrieveResponse,
    MemoryDeleteManyResponse,
    MemoryCreateUploadResponse,
    MemoryDeleteUploadResponse,
)
from nebula._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Nebula) -> None:
        memory = client.memories.create()
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.create(
            chunks=["string"],
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            contents=["string"],
            engram_type="document",
            ingestion_config={
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "chunking_strategy",
                "chunks_for_engram_summary": 0,
                "engram_summary_max_length": 0,
                "engram_summary_system_prompt": "engram_summary_system_prompt",
                "engram_summary_task_prompt": "engram_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "single_chunk_summary_threshold": 0,
                "skip_engram_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "authority": 0,
                    "metadata": {"foo": "bar"},
                }
            ],
            metadata={"foo": "bar"},
            name="name",
            raw_text="raw_text",
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
            speaker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            speaker_name="speaker_name",
        )
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryCreateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        memory = client.memories.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        memory = client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            merge_metadata=True,
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        memory = client.memories.list()
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.list(
            collection_ids=["string", "string"],
            ids=["string"],
            include_summary_embeddings=True,
            limit=1,
            metadata_filters="metadata_filters",
            offset=0,
            owner_only=True,
        )
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryListResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        memory = client.memories.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_append(self, client: Nebula) -> None:
        memory = client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @parametrize
    def test_method_append_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chunks=["string"],
            ingestion_config={
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "chunking_strategy",
                "chunks_for_engram_summary": 0,
                "engram_summary_max_length": 0,
                "engram_summary_system_prompt": "engram_summary_system_prompt",
                "engram_summary_task_prompt": "engram_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "single_chunk_summary_threshold": 0,
                "skip_engram_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "authority": 0,
                    "metadata": {"foo": "bar"},
                    "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "source_role_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            metadata={"foo": "bar"},
            raw_text="raw_text",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_append(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_append(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryAppendResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_append(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.append(
                id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_create_upload(self, client: Nebula) -> None:
        memory = client.memories.create_upload(
            content_type="content_type",
            file_size=0,
            filename="filename",
        )
        assert_matches_type(MemoryCreateUploadResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_create_upload(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.create_upload(
            content_type="content_type",
            file_size=0,
            filename="filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryCreateUploadResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_create_upload(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.create_upload(
            content_type="content_type",
            file_size=0,
            filename="filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryCreateUploadResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_many_overload_1(self, client: Nebula) -> None:
        memory = client.memories.delete_many(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_delete_many_overload_1(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete_many(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_delete_many_overload_1(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete_many(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_many_overload_2(self, client: Nebula) -> None:
        memory = client.memories.delete_many(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_delete_many_overload_2(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete_many(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_delete_many_overload_2(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete_many(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_upload(self, client: Nebula) -> None:
        memory = client.memories.delete_upload(
            s3_key="s3_key",
        )
        assert_matches_type(MemoryDeleteUploadResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_delete_upload(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete_upload(
            s3_key="s3_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteUploadResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_delete_upload(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete_upload(
            s3_key="s3_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteUploadResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Nebula) -> None:
        memory = client.memories.search(
            query="query",
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.search(
            query="query",
            collection_ids=["string"],
            effort="auto",
            filters={"foo": "bar"},
            search_settings={
                "effort": "auto",
                "enable_conceptual_expansion": True,
                "filters": {"foo": "bar"},
                "fulltext_weight": 0.2,
                "graph_settings": {"foo": "bar"},
                "has_pruning_gate": True,
                "include_scores": True,
                "semantic_weight": 0.8,
                "verbose": False,
            },
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
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemorySearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.create()
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.create(
            chunks=["string"],
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            contents=["string"],
            engram_type="document",
            ingestion_config={
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "chunking_strategy",
                "chunks_for_engram_summary": 0,
                "engram_summary_max_length": 0,
                "engram_summary_system_prompt": "engram_summary_system_prompt",
                "engram_summary_task_prompt": "engram_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "single_chunk_summary_threshold": 0,
                "skip_engram_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "authority": 0,
                    "metadata": {"foo": "bar"},
                }
            ],
            metadata={"foo": "bar"},
            name="name",
            raw_text="raw_text",
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
            speaker_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            speaker_name="speaker_name",
        )
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryCreateResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryCreateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            merge_metadata=True,
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryUpdateResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list()
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list(
            collection_ids=["string", "string"],
            ids=["string"],
            include_summary_embeddings=True,
            limit=1,
            metadata_filters="metadata_filters",
            offset=0,
            owner_only=True,
        )
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryListResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryListResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_append(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @parametrize
    async def test_method_append_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chunks=["string"],
            ingestion_config={
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "chunking_strategy",
                "chunks_for_engram_summary": 0,
                "engram_summary_max_length": 0,
                "engram_summary_system_prompt": "engram_summary_system_prompt",
                "engram_summary_task_prompt": "engram_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "single_chunk_summary_threshold": 0,
                "skip_engram_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "authority": 0,
                    "metadata": {"foo": "bar"},
                    "parent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "source_role_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            metadata={"foo": "bar"},
            raw_text="raw_text",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_append(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_append(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryAppendResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_append(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.append(
                id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_create_upload(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.create_upload(
            content_type="content_type",
            file_size=0,
            filename="filename",
        )
        assert_matches_type(MemoryCreateUploadResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_create_upload(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.create_upload(
            content_type="content_type",
            file_size=0,
            filename="filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryCreateUploadResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_create_upload(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.create_upload(
            content_type="content_type",
            file_size=0,
            filename="filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryCreateUploadResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_many_overload_1(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete_many(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_delete_many_overload_1(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete_many(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_delete_many_overload_1(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete_many(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_many_overload_2(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete_many(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_delete_many_overload_2(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete_many(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_delete_many_overload_2(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete_many(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteManyResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_upload(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete_upload(
            s3_key="s3_key",
        )
        assert_matches_type(MemoryDeleteUploadResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_delete_upload(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete_upload(
            s3_key="s3_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteUploadResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_delete_upload(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete_upload(
            s3_key="s3_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteUploadResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.search(
            query="query",
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.search(
            query="query",
            collection_ids=["string"],
            effort="auto",
            filters={"foo": "bar"},
            search_settings={
                "effort": "auto",
                "enable_conceptual_expansion": True,
                "filters": {"foo": "bar"},
                "fulltext_weight": 0.2,
                "graph_settings": {"foo": "bar"},
                "has_pruning_gate": True,
                "include_scores": True,
                "semantic_weight": 0.8,
                "verbose": False,
            },
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
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemorySearchResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True
