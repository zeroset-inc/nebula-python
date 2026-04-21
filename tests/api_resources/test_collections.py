# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    NebulaResultsCollectionResponse,
    NebulaResultsGenericBooleanResponse,
    PaginatedNebulaResultListCollectionResponse,
)
from nebula.types.collections import NebulaResultsGenericMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Nebula) -> None:
        collection = client.collections.create(
            name="name",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.create(
            name="name",
            description="description",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Nebula) -> None:
        collection = client.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Nebula) -> None:
        collection = client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_tier="access_tier",
            description="description",
            generate_description=True,
            name="name",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Nebula) -> None:
        collection = client.collections.list()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.list(
            ids=["string"],
            limit=1,
            offset=0,
            owner_only=True,
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Nebula) -> None:
        collection = client.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export(self, client: Nebula) -> None:
        collection = client.collections.export()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.export(
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract(self, client: Nebula) -> None:
        collection = client.collections.extract(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.extract(
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
        assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.extract(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.extract(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_extract(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.extract(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_documents_with_memories(self, client: Nebula) -> None:
        collection = client.collections.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_documents_with_memories_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_embeddings=True,
            limit=1,
            offset=0,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_documents_with_memories(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_documents_with_memories(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_documents_with_memories(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.get_documents_with_memories(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_metrics(self, client: Nebula) -> None:
        collection = client.collections.get_metrics(
            collection_id="collection_id",
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_metrics_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.get_metrics(
            collection_id="collection_id",
            days=0,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_metrics(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.get_metrics(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_metrics(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.get_metrics(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_metrics(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.get_metrics(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_name(self, client: Nebula) -> None:
        collection = client.collections.retrieve_by_name(
            collection_name="collection_name",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_name_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.retrieve_by_name(
            collection_name="collection_name",
            owner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_name(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.retrieve_by_name(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.retrieve_by_name(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_name(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_name` but received ''"):
            client.collections.with_raw_response.retrieve_by_name(
                collection_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_status(self, client: Nebula) -> None:
        collection = client.collections.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_status_with_all_params(self, client: Nebula) -> None:
        collection = client.collections.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force_update=True,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_status(self, client: Nebula) -> None:
        response = client.collections.with_raw_response.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_status(self, client: Nebula) -> None:
        with client.collections.with_streaming_response.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_validate_status(self, client: Nebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.collections.with_raw_response.validate_status(
                id="",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.create(
            name="name",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.create(
            name="name",
            description="description",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_tier="access_tier",
            description="description",
            generate_description=True,
            name="name",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.list()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.list(
            ids=["string"],
            limit=1,
            offset=0,
            owner_only=True,
        )
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(PaginatedNebulaResultListCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsGenericBooleanResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.export()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.export(
            columns=["string"],
            filters={"foo": "bar"},
            include_header=True,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.extract(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.extract(
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
        assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.extract(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.extract(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsGenericMessageResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_extract(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.extract(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_documents_with_memories(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_documents_with_memories_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_embeddings=True,
            limit=1,
            offset=0,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_documents_with_memories(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_documents_with_memories(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.get_documents_with_memories(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_documents_with_memories(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.get_documents_with_memories(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_metrics(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.get_metrics(
            collection_id="collection_id",
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_metrics_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.get_metrics(
            collection_id="collection_id",
            days=0,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_metrics(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.get_metrics(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_metrics(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.get_metrics(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_metrics(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.get_metrics(
                collection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.retrieve_by_name(
            collection_name="collection_name",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_name_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.retrieve_by_name(
            collection_name="collection_name",
            owner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.retrieve_by_name(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.retrieve_by_name(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(NebulaResultsCollectionResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_name(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_name` but received ''"):
            await async_client.collections.with_raw_response.retrieve_by_name(
                collection_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_status(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_status_with_all_params(self, async_client: AsyncNebula) -> None:
        collection = await async_client.collections.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force_update=True,
        )
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_status(self, async_client: AsyncNebula) -> None:
        response = await async_client.collections.with_raw_response.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_status(self, async_client: AsyncNebula) -> None:
        async with async_client.collections.with_streaming_response.validate_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_validate_status(self, async_client: AsyncNebula) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.collections.with_raw_response.validate_status(
                id="",
            )
