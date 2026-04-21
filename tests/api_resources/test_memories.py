# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    MemoryAppendResponse,
    MemorySearchResponse,
    MemoryDeleteMultipleResponse,
    NebulaResultsGenericBooleanResponse,
    PaginatedNebulaResultListChunkResponse,
    PaginatedNebulaResultListCollectionResponse,
)
from nebula._utils import parse_datetime
from nebula.types.memories import NebulaResultsEngramResponse
from nebula.types.collections import NebulaResultsGenericMessageResponse, PaginatedNebulaResultListEngramResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Nebula) -> None:
        memory = client.memories.create(
            collection_ref="collection_ref",
            engram_type="conversation",
        )
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.create(
            collection_ref="collection_ref",
            engram_type="conversation",
            chunks=["string"],
            ingestion_config={
                "app": {
                    "allowed_webhook_ips": ["string"],
                    "app_base_url": "app_base_url",
                    "audio_lm": "audio_lm",
                    "default_max_chunks_per_user": 0,
                    "default_max_collections_per_user": 0,
                    "default_max_documents_per_user": 0,
                    "default_max_upload_size": 0,
                    "extra_fields": {"foo": "bar"},
                    "fast_llm": "fast_llm",
                    "max_upload_size_by_type": {"foo": 0},
                    "planning_llm": "planning_llm",
                    "project_name": "project_name",
                    "quality_llm": "quality_llm",
                    "reasoning_llm": "reasoning_llm",
                    "require_service_api_key": True,
                    "service_api_key": "service_api_key",
                    "stripe_secret_key": "stripe_secret_key",
                    "stripe_webhook_secret": "stripe_webhook_secret",
                    "user_tools_path": "user_tools_path",
                    "vlm": "vlm",
                    "webhook_hmac_secret": "webhook_hmac_secret",
                    "webhook_hmac_secret_previous": "webhook_hmac_secret_previous",
                    "webhook_ip_validation_enabled": True,
                    "webhook_rate_limit_max_requests": 0,
                    "webhook_rate_limit_window_seconds": 0,
                    "webhook_signature_validation_enabled": True,
                },
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "generation_config": {
                        "add_generation_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "extended_thinking": True,
                        "functions": [{"foo": "bar"}],
                        "max_tokens_to_sample": 4096,
                        "model": "openai/gpt-4.1",
                        "reasoning_effort": "reasoning_effort",
                        "response_format": {"foo": "bar"},
                        "stream": False,
                        "temperature": 0,
                        "thinking_budget": 0,
                        "tools": [{"foo": "bar"}],
                        "top_p": 1,
                        "verbosity": "verbosity",
                    },
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "recursive",
                "chunks_for_document_summary": 0,
                "document_summary_max_length": 0,
                "document_summary_model": "document_summary_model",
                "document_summary_system_prompt": "document_summary_system_prompt",
                "document_summary_task_prompt": "document_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_fields": {"foo": "bar"},
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "skip_document_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                    "authority": 0,
                    "metadata": {"foo": "bar"},
                }
            ],
            metadata={"foo": "bar"},
            name="name",
            raw_text="raw_text",
        )
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.create(
            collection_ref="collection_ref",
            engram_type="conversation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.create(
            collection_ref="collection_ref",
            engram_type="conversation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        memory = client.memories.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        memory = client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            merge_metadata=True,
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        memory = client.memories.list()
        assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.list(
            collection_ids=["string"],
            ids=["string"],
            include_summary_embeddings=True,
            limit=1,
            metadata_filters="metadata_filters",
            offset=0,
            owner_only=True,
        )
        assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        memory = client.memories.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_append(self, client: Nebula) -> None:
        memory = client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_append_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chunks=["string"],
            ingestion_config={
                "app": {
                    "allowed_webhook_ips": ["string"],
                    "app_base_url": "app_base_url",
                    "audio_lm": "audio_lm",
                    "default_max_chunks_per_user": 0,
                    "default_max_collections_per_user": 0,
                    "default_max_documents_per_user": 0,
                    "default_max_upload_size": 0,
                    "extra_fields": {"foo": "bar"},
                    "fast_llm": "fast_llm",
                    "max_upload_size_by_type": {"foo": 0},
                    "planning_llm": "planning_llm",
                    "project_name": "project_name",
                    "quality_llm": "quality_llm",
                    "reasoning_llm": "reasoning_llm",
                    "require_service_api_key": True,
                    "service_api_key": "service_api_key",
                    "stripe_secret_key": "stripe_secret_key",
                    "stripe_webhook_secret": "stripe_webhook_secret",
                    "user_tools_path": "user_tools_path",
                    "vlm": "vlm",
                    "webhook_hmac_secret": "webhook_hmac_secret",
                    "webhook_hmac_secret_previous": "webhook_hmac_secret_previous",
                    "webhook_ip_validation_enabled": True,
                    "webhook_rate_limit_max_requests": 0,
                    "webhook_rate_limit_window_seconds": 0,
                    "webhook_signature_validation_enabled": True,
                },
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "generation_config": {
                        "add_generation_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "extended_thinking": True,
                        "functions": [{"foo": "bar"}],
                        "max_tokens_to_sample": 4096,
                        "model": "openai/gpt-4.1",
                        "reasoning_effort": "reasoning_effort",
                        "response_format": {"foo": "bar"},
                        "stream": False,
                        "temperature": 0,
                        "thinking_budget": 0,
                        "tools": [{"foo": "bar"}],
                        "top_p": 1,
                        "verbosity": "verbosity",
                    },
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "recursive",
                "chunks_for_document_summary": 0,
                "document_summary_max_length": 0,
                "document_summary_model": "document_summary_model",
                "document_summary_system_prompt": "document_summary_system_prompt",
                "document_summary_task_prompt": "document_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_fields": {"foo": "bar"},
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "skip_document_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[{"foo": "bar"}],
            metadata={"foo": "bar"},
            raw_text="raw_text",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_append(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.append(
                id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deduplicate_entities(self, client: Nebula) -> None:
        memory = client.memories.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deduplicate_entities_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automatic_clustering=True,
            automatic_deduplication=True,
            chunk_merge_count=0,
            conversation_context_enabled=True,
            conversation_context_window_size=0,
            conversation_summary_update_frequency=0,
            entity_deduplication={
                "auto_merge_threshold": 0,
                "candidate_pool_limit": 0,
                "collection_scope": True,
                "create_audit_relationships": True,
                "cross_engram_deduplication": True,
                "dedup_candidate_search_limit": 0,
                "dedup_llm_per_chunk_limit": 0,
                "dedup_max_concurrent_chunks": 0,
                "dedup_timeout_seconds": 0,
                "embedding_cache_enabled": True,
                "enabled": True,
                "link_threshold": 0,
                "max_candidate_entities": 0,
                "max_concurrent_llm_calls": 0,
                "max_recursive_iterations": 0,
                "merge_prompt_template": "merge_prompt_template",
                "preserve_entities": True,
                "query_time_resolution": True,
                "recursive_deduplication": True,
                "retrieval_top_k": 0,
                "semantic_similarity_threshold": 0,
                "show_duplicate_relationships": True,
                "strategy": "strategy",
                "use_engram_context": True,
                "use_llm_for_merging": True,
                "vector_doc_chunk_size": 0,
                "vector_query_chunk_size": 0,
            },
            entity_types=["string"],
            generation_config={
                "add_generation_kwargs": {"foo": "bar"},
                "api_base": "api_base",
                "extended_thinking": True,
                "functions": [{"foo": "bar"}],
                "max_tokens_to_sample": 4096,
                "model": "openai/gpt-4.1",
                "reasoning_effort": "reasoning_effort",
                "response_format": {"foo": "bar"},
                "stream": False,
                "temperature": 0,
                "thinking_budget": 0,
                "tools": [{"foo": "bar"}],
                "top_p": 1,
                "verbosity": "verbosity",
            },
            graph_entity_description_prompt="graph_entity_description_prompt",
            graph_extraction_prompt="graph_extraction_prompt",
            idle_check_interval_minutes=0,
            idle_full_clustering=True,
            incremental_clustering=True,
            incremental_jaccard_filter=0,
            incremental_jaccard_reuse_threshold=0,
            incremental_min_cluster_size=1,
            incremental_neighbor_hops=0,
            incremental_structural_affinity_threshold=0,
            max_concurrent_entities_per_extraction=0,
            max_concurrent_relationships_per_extraction=0,
            max_description_input_length=0,
            max_knowledge_relationships=0,
            relation_types=["string"],
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deduplicate_entities(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deduplicate_entities(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deduplicate_entities(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.deduplicate_entities(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_filter(self, client: Nebula) -> None:
        memory = client.memories.delete_by_filter(
            body={"foo": "bar"},
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_by_filter(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete_by_filter(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_filter(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete_by_filter(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_multiple_overload_1(self, client: Nebula) -> None:
        memory = client.memories.delete_multiple(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_multiple_overload_1(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete_multiple(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_multiple_overload_1(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete_multiple(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_multiple_overload_2(self, client: Nebula) -> None:
        memory = client.memories.delete_multiple(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_multiple_overload_2(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.delete_multiple(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_multiple_overload_2(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.delete_multiple(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download_content(self, client: Nebula) -> None:
        memory = client.memories.download_content(
            "id",
        )
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download_content(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.download_content(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download_content(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.download_content(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_download_content(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.download_content(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download_zip(self, client: Nebula) -> None:
        memory = client.memories.download_zip()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download_zip_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.download_zip(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            engram_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download_zip(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.download_zip()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download_zip(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.download_zip() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export(self, client: Nebula) -> None:
        memory = client.memories.export()
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.export(
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_entities(self, client: Nebula) -> None:
        memory = client.memories.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_entities_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automatic_clustering=True,
            automatic_deduplication=True,
            chunk_merge_count=0,
            conversation_context_enabled=True,
            conversation_context_window_size=0,
            conversation_summary_update_frequency=0,
            entity_deduplication={
                "auto_merge_threshold": 0,
                "candidate_pool_limit": 0,
                "collection_scope": True,
                "create_audit_relationships": True,
                "cross_engram_deduplication": True,
                "dedup_candidate_search_limit": 0,
                "dedup_llm_per_chunk_limit": 0,
                "dedup_max_concurrent_chunks": 0,
                "dedup_timeout_seconds": 0,
                "embedding_cache_enabled": True,
                "enabled": True,
                "link_threshold": 0,
                "max_candidate_entities": 0,
                "max_concurrent_llm_calls": 0,
                "max_recursive_iterations": 0,
                "merge_prompt_template": "merge_prompt_template",
                "preserve_entities": True,
                "query_time_resolution": True,
                "recursive_deduplication": True,
                "retrieval_top_k": 0,
                "semantic_similarity_threshold": 0,
                "show_duplicate_relationships": True,
                "strategy": "strategy",
                "use_engram_context": True,
                "use_llm_for_merging": True,
                "vector_doc_chunk_size": 0,
                "vector_query_chunk_size": 0,
            },
            entity_types=["string"],
            generation_config={
                "add_generation_kwargs": {"foo": "bar"},
                "api_base": "api_base",
                "extended_thinking": True,
                "functions": [{"foo": "bar"}],
                "max_tokens_to_sample": 4096,
                "model": "openai/gpt-4.1",
                "reasoning_effort": "reasoning_effort",
                "response_format": {"foo": "bar"},
                "stream": False,
                "temperature": 0,
                "thinking_budget": 0,
                "tools": [{"foo": "bar"}],
                "top_p": 1,
                "verbosity": "verbosity",
            },
            graph_entity_description_prompt="graph_entity_description_prompt",
            graph_extraction_prompt="graph_extraction_prompt",
            idle_check_interval_minutes=0,
            idle_full_clustering=True,
            incremental_clustering=True,
            incremental_jaccard_filter=0,
            incremental_jaccard_reuse_threshold=0,
            incremental_min_cluster_size=1,
            incremental_neighbor_hops=0,
            incremental_structural_affinity_threshold=0,
            max_concurrent_entities_per_extraction=0,
            max_concurrent_relationships_per_extraction=0,
            max_description_input_length=0,
            max_knowledge_relationships=0,
            relation_types=["string"],
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_entities(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_entities(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_extract_entities(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.extract_entities(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_chunks(self, client: Nebula) -> None:
        memory = client.memories.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_chunks_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_vectors=True,
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_chunks(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_chunks(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_chunks(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.list_chunks(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_collections(self, client: Nebula) -> None:
        memory = client.memories.list_collections(
            id="id",
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_collections_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.list_collections(
            id="id",
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_collections(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.list_collections(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_collections(self, client: Nebula) -> None:
        with client.memories.with_streaming_response.list_collections(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_collections(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memories.with_raw_response.list_collections(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Nebula) -> None:
        memory = client.memories.search(
            query="query",
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Nebula) -> None:
        memory = client.memories.search(
            query="query",
            search_mode="fast",
            search_settings={
                "enable_conceptual_expansion": True,
                "filters": {"category": "bar"},
                "fulltext_weight": 1,
                "include_metadatas": True,
                "include_scores": True,
                "limit": 20,
                "search_mode": "search_mode",
                "semantic_weight": 5,
            },
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Nebula) -> None:
        response = client.memories.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.create(
            collection_ref="collection_ref",
            engram_type="conversation",
        )
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.create(
            collection_ref="collection_ref",
            engram_type="conversation",
            chunks=["string"],
            ingestion_config={
                "app": {
                    "allowed_webhook_ips": ["string"],
                    "app_base_url": "app_base_url",
                    "audio_lm": "audio_lm",
                    "default_max_chunks_per_user": 0,
                    "default_max_collections_per_user": 0,
                    "default_max_documents_per_user": 0,
                    "default_max_upload_size": 0,
                    "extra_fields": {"foo": "bar"},
                    "fast_llm": "fast_llm",
                    "max_upload_size_by_type": {"foo": 0},
                    "planning_llm": "planning_llm",
                    "project_name": "project_name",
                    "quality_llm": "quality_llm",
                    "reasoning_llm": "reasoning_llm",
                    "require_service_api_key": True,
                    "service_api_key": "service_api_key",
                    "stripe_secret_key": "stripe_secret_key",
                    "stripe_webhook_secret": "stripe_webhook_secret",
                    "user_tools_path": "user_tools_path",
                    "vlm": "vlm",
                    "webhook_hmac_secret": "webhook_hmac_secret",
                    "webhook_hmac_secret_previous": "webhook_hmac_secret_previous",
                    "webhook_ip_validation_enabled": True,
                    "webhook_rate_limit_max_requests": 0,
                    "webhook_rate_limit_window_seconds": 0,
                    "webhook_signature_validation_enabled": True,
                },
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "generation_config": {
                        "add_generation_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "extended_thinking": True,
                        "functions": [{"foo": "bar"}],
                        "max_tokens_to_sample": 4096,
                        "model": "openai/gpt-4.1",
                        "reasoning_effort": "reasoning_effort",
                        "response_format": {"foo": "bar"},
                        "stream": False,
                        "temperature": 0,
                        "thinking_budget": 0,
                        "tools": [{"foo": "bar"}],
                        "top_p": 1,
                        "verbosity": "verbosity",
                    },
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "recursive",
                "chunks_for_document_summary": 0,
                "document_summary_max_length": 0,
                "document_summary_model": "document_summary_model",
                "document_summary_system_prompt": "document_summary_system_prompt",
                "document_summary_task_prompt": "document_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_fields": {"foo": "bar"},
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "skip_document_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                    "authority": 0,
                    "metadata": {"foo": "bar"},
                }
            ],
            metadata={"foo": "bar"},
            name="name",
            raw_text="raw_text",
        )
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.create(
            collection_ref="collection_ref",
            engram_type="conversation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.create(
            collection_ref="collection_ref",
            engram_type="conversation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            merge_metadata=True,
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(NebulaResultsEngramResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list()
        assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list(
            collection_ids=["string"],
            ids=["string"],
            include_summary_embeddings=True,
            limit=1,
            metadata_filters="metadata_filters",
            offset=0,
            owner_only=True,
        )
        assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(PaginatedNebulaResultListEngramResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_append(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_append_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.append(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            chunks=["string"],
            ingestion_config={
                "app": {
                    "allowed_webhook_ips": ["string"],
                    "app_base_url": "app_base_url",
                    "audio_lm": "audio_lm",
                    "default_max_chunks_per_user": 0,
                    "default_max_collections_per_user": 0,
                    "default_max_documents_per_user": 0,
                    "default_max_upload_size": 0,
                    "extra_fields": {"foo": "bar"},
                    "fast_llm": "fast_llm",
                    "max_upload_size_by_type": {"foo": 0},
                    "planning_llm": "planning_llm",
                    "project_name": "project_name",
                    "quality_llm": "quality_llm",
                    "reasoning_llm": "reasoning_llm",
                    "require_service_api_key": True,
                    "service_api_key": "service_api_key",
                    "stripe_secret_key": "stripe_secret_key",
                    "stripe_webhook_secret": "stripe_webhook_secret",
                    "user_tools_path": "user_tools_path",
                    "vlm": "vlm",
                    "webhook_hmac_secret": "webhook_hmac_secret",
                    "webhook_hmac_secret_previous": "webhook_hmac_secret_previous",
                    "webhook_ip_validation_enabled": True,
                    "webhook_rate_limit_max_requests": 0,
                    "webhook_rate_limit_window_seconds": 0,
                    "webhook_signature_validation_enabled": True,
                },
                "audio_transcription_model": "audio_transcription_model",
                "automatic_extraction": True,
                "chunk_enrichment_settings": {
                    "chunk_enrichment_prompt": "chunk_enrichment_prompt",
                    "enable_chunk_enrichment": True,
                    "generation_config": {
                        "add_generation_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "extended_thinking": True,
                        "functions": [{"foo": "bar"}],
                        "max_tokens_to_sample": 4096,
                        "model": "openai/gpt-4.1",
                        "reasoning_effort": "reasoning_effort",
                        "response_format": {"foo": "bar"},
                        "stream": False,
                        "temperature": 0,
                        "thinking_budget": 0,
                        "tools": [{"foo": "bar"}],
                        "top_p": 1,
                        "verbosity": "verbosity",
                    },
                    "n_chunks": 0,
                },
                "chunk_overlap": 0,
                "chunk_size": 0,
                "chunking_strategy": "recursive",
                "chunks_for_document_summary": 0,
                "document_summary_max_length": 0,
                "document_summary_model": "document_summary_model",
                "document_summary_system_prompt": "document_summary_system_prompt",
                "document_summary_task_prompt": "document_summary_task_prompt",
                "excluded_parsers": ["string"],
                "extra_fields": {"foo": "bar"},
                "extra_parsers": {"foo": "bar"},
                "max_concurrent_vlm_tasks": 0,
                "parser_overrides": {"foo": "string"},
                "provider": "provider",
                "skip_document_summary": True,
                "vlm": "vlm",
                "vlm_batch_size": 0,
                "vlm_max_tokens_to_sample": 0,
                "vlm_ocr_one_page_per_chunk": True,
            },
            ingestion_mode="hi-res",
            messages=[{"foo": "bar"}],
            metadata={"foo": "bar"},
            raw_text="raw_text",
        )
        assert_matches_type(MemoryAppendResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_append(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.append(
                id="",
                collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deduplicate_entities(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deduplicate_entities_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automatic_clustering=True,
            automatic_deduplication=True,
            chunk_merge_count=0,
            conversation_context_enabled=True,
            conversation_context_window_size=0,
            conversation_summary_update_frequency=0,
            entity_deduplication={
                "auto_merge_threshold": 0,
                "candidate_pool_limit": 0,
                "collection_scope": True,
                "create_audit_relationships": True,
                "cross_engram_deduplication": True,
                "dedup_candidate_search_limit": 0,
                "dedup_llm_per_chunk_limit": 0,
                "dedup_max_concurrent_chunks": 0,
                "dedup_timeout_seconds": 0,
                "embedding_cache_enabled": True,
                "enabled": True,
                "link_threshold": 0,
                "max_candidate_entities": 0,
                "max_concurrent_llm_calls": 0,
                "max_recursive_iterations": 0,
                "merge_prompt_template": "merge_prompt_template",
                "preserve_entities": True,
                "query_time_resolution": True,
                "recursive_deduplication": True,
                "retrieval_top_k": 0,
                "semantic_similarity_threshold": 0,
                "show_duplicate_relationships": True,
                "strategy": "strategy",
                "use_engram_context": True,
                "use_llm_for_merging": True,
                "vector_doc_chunk_size": 0,
                "vector_query_chunk_size": 0,
            },
            entity_types=["string"],
            generation_config={
                "add_generation_kwargs": {"foo": "bar"},
                "api_base": "api_base",
                "extended_thinking": True,
                "functions": [{"foo": "bar"}],
                "max_tokens_to_sample": 4096,
                "model": "openai/gpt-4.1",
                "reasoning_effort": "reasoning_effort",
                "response_format": {"foo": "bar"},
                "stream": False,
                "temperature": 0,
                "thinking_budget": 0,
                "tools": [{"foo": "bar"}],
                "top_p": 1,
                "verbosity": "verbosity",
            },
            graph_entity_description_prompt="graph_entity_description_prompt",
            graph_extraction_prompt="graph_extraction_prompt",
            idle_check_interval_minutes=0,
            idle_full_clustering=True,
            incremental_clustering=True,
            incremental_jaccard_filter=0,
            incremental_jaccard_reuse_threshold=0,
            incremental_min_cluster_size=1,
            incremental_neighbor_hops=0,
            incremental_structural_affinity_threshold=0,
            max_concurrent_entities_per_extraction=0,
            max_concurrent_relationships_per_extraction=0,
            max_description_input_length=0,
            max_knowledge_relationships=0,
            relation_types=["string"],
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deduplicate_entities(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deduplicate_entities(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.deduplicate_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deduplicate_entities(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.deduplicate_entities(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_filter(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete_by_filter(
            body={"foo": "bar"},
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_filter(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete_by_filter(
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_filter(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete_by_filter(
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_multiple_overload_1(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete_multiple(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_multiple_overload_1(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete_multiple(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_multiple_overload_1(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete_multiple(
            body="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_multiple_overload_2(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.delete_multiple(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_multiple_overload_2(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.delete_multiple(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_multiple_overload_2(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.delete_multiple(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryDeleteMultipleResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download_content(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.download_content(
            "id",
        )
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download_content(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.download_content(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download_content(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.download_content(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_download_content(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.download_content(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download_zip(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.download_zip()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download_zip_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.download_zip(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            engram_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download_zip(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.download_zip()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download_zip(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.download_zip() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.export()
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.export(
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(object, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_entities(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_entities_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automatic_clustering=True,
            automatic_deduplication=True,
            chunk_merge_count=0,
            conversation_context_enabled=True,
            conversation_context_window_size=0,
            conversation_summary_update_frequency=0,
            entity_deduplication={
                "auto_merge_threshold": 0,
                "candidate_pool_limit": 0,
                "collection_scope": True,
                "create_audit_relationships": True,
                "cross_engram_deduplication": True,
                "dedup_candidate_search_limit": 0,
                "dedup_llm_per_chunk_limit": 0,
                "dedup_max_concurrent_chunks": 0,
                "dedup_timeout_seconds": 0,
                "embedding_cache_enabled": True,
                "enabled": True,
                "link_threshold": 0,
                "max_candidate_entities": 0,
                "max_concurrent_llm_calls": 0,
                "max_recursive_iterations": 0,
                "merge_prompt_template": "merge_prompt_template",
                "preserve_entities": True,
                "query_time_resolution": True,
                "recursive_deduplication": True,
                "retrieval_top_k": 0,
                "semantic_similarity_threshold": 0,
                "show_duplicate_relationships": True,
                "strategy": "strategy",
                "use_engram_context": True,
                "use_llm_for_merging": True,
                "vector_doc_chunk_size": 0,
                "vector_query_chunk_size": 0,
            },
            entity_types=["string"],
            generation_config={
                "add_generation_kwargs": {"foo": "bar"},
                "api_base": "api_base",
                "extended_thinking": True,
                "functions": [{"foo": "bar"}],
                "max_tokens_to_sample": 4096,
                "model": "openai/gpt-4.1",
                "reasoning_effort": "reasoning_effort",
                "response_format": {"foo": "bar"},
                "stream": False,
                "temperature": 0,
                "thinking_budget": 0,
                "tools": [{"foo": "bar"}],
                "top_p": 1,
                "verbosity": "verbosity",
            },
            graph_entity_description_prompt="graph_entity_description_prompt",
            graph_extraction_prompt="graph_extraction_prompt",
            idle_check_interval_minutes=0,
            idle_full_clustering=True,
            incremental_clustering=True,
            incremental_jaccard_filter=0,
            incremental_jaccard_reuse_threshold=0,
            incremental_min_cluster_size=1,
            incremental_neighbor_hops=0,
            incremental_structural_affinity_threshold=0,
            max_concurrent_entities_per_extraction=0,
            max_concurrent_relationships_per_extraction=0,
            max_description_input_length=0,
            max_knowledge_relationships=0,
            relation_types=["string"],
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_entities(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_entities(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.extract_entities(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_extract_entities(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.extract_entities(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_chunks(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_chunks_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_vectors=True,
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_chunks(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_chunks(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.list_chunks(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(PaginatedNebulaResultListChunkResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_chunks(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.list_chunks(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_collections(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list_collections(
            id="id",
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_collections_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.list_collections(
            id="id",
            limit=1,
            offset=0,
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_collections(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.list_collections(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_collections(self, async_client: AsyncNebula) -> None:
        async with async_client.memories.with_streaming_response.list_collections(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(PaginatedNebulaResultListCollectionResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_collections(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memories.with_raw_response.list_collections(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.search(
            query="query",
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncNebula) -> None:
        memory = await async_client.memories.search(
            query="query",
            search_mode="fast",
            search_settings={
                "enable_conceptual_expansion": True,
                "filters": {"category": "bar"},
                "fulltext_weight": 1,
                "include_metadatas": True,
                "include_scores": True,
                "limit": 20,
                "search_mode": "search_mode",
                "semantic_weight": 5,
            },
        )
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncNebula) -> None:
        response = await async_client.memories.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemorySearchResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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
