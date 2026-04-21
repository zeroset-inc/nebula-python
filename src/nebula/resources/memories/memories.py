# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ...types import (
    SearchMode,
    IngestionMode,
    memory_list_params,
    memory_append_params,
    memory_create_params,
    memory_export_params,
    memory_search_params,
    memory_update_params,
    memory_list_chunks_params,
    memory_download_zip_params,
    memory_delete_multiple_params,
    memory_delete_by_filter_params,
    memory_extract_entities_params,
    memory_list_collections_params,
    memory_deduplicate_entities_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .relationships import (
    RelationshipsResource,
    AsyncRelationshipsResource,
    RelationshipsResourceWithRawResponse,
    AsyncRelationshipsResourceWithRawResponse,
    RelationshipsResourceWithStreamingResponse,
    AsyncRelationshipsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.search_mode import SearchMode
from ...types.ingestion_mode import IngestionMode
from ...types.search_settings_param import SearchSettingsParam
from ...types.ingestion_config_param import IngestionConfigParam
from ...types.memory_append_response import MemoryAppendResponse
from ...types.memory_search_response import MemorySearchResponse
from ...types.generation_config_param import GenerationConfigParam
from ...types.memory_delete_multiple_response import MemoryDeleteMultipleResponse
from ...types.memories.nebula_results_engram_response import NebulaResultsEngramResponse
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse
from ...types.paginated_nebula_result_list_chunk_response import PaginatedNebulaResultListChunkResponse
from ...types.paginated_nebula_result_list_collection_response import PaginatedNebulaResultListCollectionResponse
from ...types.collections.nebula_results_generic_message_response import NebulaResultsGenericMessageResponse
from ...types.collections.paginated_nebula_result_list_engram_response import PaginatedNebulaResultListEngramResponse

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def entities(self) -> EntitiesResource:
        return EntitiesResource(self._client)

    @cached_property
    def relationships(self) -> RelationshipsResource:
        return RelationshipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return MemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return MemoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_ref: str,
        engram_type: Literal["conversation", "document"],
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        ingestion_config: Optional[IngestionConfigParam] | Omit = omit,
        ingestion_mode: Optional[IngestionMode] | Omit = omit,
        messages: Optional[Iterable[memory_create_params.Message]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        raw_text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a new memory (conversation or document) using clean JSON body.

        - Use `collection_ref` (UUID or name) instead of `collection_ids`
        - Discriminated union on `engram_type`: "conversation" or "document"
        - For conversations: provide `messages` array
        - For documents: provide `raw_text` or `chunks`

        Args:
          collection_ref: Collection UUID or name

          engram_type: Type of memory to create

          chunks: Pre-chunked text for document type

          ingestion_config: Custom ingestion config for documents

          ingestion_mode: Ingestion mode for documents

          messages: Messages for conversation type

          metadata: Metadata for the memory

          name: Optional name for the memory

          raw_text: Raw text content for document type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memories",
            body=maybe_transform(
                {
                    "collection_ref": collection_ref,
                    "engram_type": engram_type,
                    "chunks": chunks,
                    "ingestion_config": ingestion_config,
                    "ingestion_mode": ingestion_mode,
                    "messages": messages,
                    "metadata": metadata,
                    "name": name,
                    "raw_text": raw_text,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """
        Retrieves detailed information about a specific engram by its ID.

        This endpoint returns the engram's metadata, status, and system information. It
        does not return the engram's content - use the `/engrams/{id}/download` endpoint
        for that.

        Users can only retrieve engrams they own or have access to through collections.
        Superusers can retrieve any engram.

        Args:
          id: The ID of the engram to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/memories/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )

    def update(
        self,
        id: str,
        *,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        merge_metadata: bool | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """
        Update memory-level properties including name, metadata, and collection
        associations.

        This endpoint allows updating properties of an entire memory (document or
        conversation) without modifying its content:

        - **name**: Updates the title field in the engrams table
        - **metadata**: Can replace or merge with existing metadata
        - **collection_ids**: Updates engram_collections table associations

        Users can only update memories they own or have access to through collections.
        At least one collection association must be maintained.

        Args:
          id: The unique identifier of the memory

          collection_ids: New collection associations

          merge_metadata: Merge with existing metadata

          metadata: Metadata to update

          name: New name for the memory

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/memories/{id}", id=id),
            body=maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "merge_metadata": merge_metadata,
                    "metadata": metadata,
                    "name": name,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )

    def list(
        self,
        *,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_summary_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filters: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        owner_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListEngramResponse:
        """
        Returns a paginated list of engrams the authenticated user has access to.

        Results can be filtered by providing specific engram IDs or collection IDs.
        Regular users will only see engrams they own or have access to through
        collections. Superusers can see all engrams.

        The engrams are returned in order of last modification, with most recent first.
        The response includes the engram's text field if available.

        Args:
          collection_ids: Optional list of collection IDs to filter engrams by. If provided, exactly one
              collection ID must be specified.

          ids: A list of engram IDs to retrieve. If not provided, all engrams will be returned.

          include_summary_embeddings: Specifies whether or not to include embeddings of each engram summary.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          metadata_filters:
              JSON string for metadata filtering. Example: '{"metadata.source": {"$eq":
              "playground"}}'

          offset: Specifies the number of objects to skip. Defaults to 0.

          owner_only: If true, only returns engrams owned by the user, not all accessible engrams.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/memories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_ids": collection_ids,
                        "ids": ids,
                        "include_summary_embeddings": include_summary_embeddings,
                        "limit": limit,
                        "metadata_filters": metadata_filters,
                        "offset": offset,
                        "owner_only": owner_only,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListEngramResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """Delete a specific engram with graph awareness.

        All chunks corresponding to the
        engram are deleted, and graph components (entities/relationships) are updated or
        deleted based on remaining chunk references from other engrams.

        This method now properly handles graph components and maintains graph integrity
        for search operations.

        Args:
          id: Engram ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/memories/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    def append(
        self,
        id: str,
        *,
        collection_id: str,
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        ingestion_config: Optional[IngestionConfigParam] | Omit = omit,
        ingestion_mode: IngestionMode | Omit = omit,
        messages: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        raw_text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryAppendResponse:
        """
        Append content to an existing engram.

        **For conversation engrams:**

        - Provide `messages` array with content, role, and optional metadata
        - Works like `/conversations/{id}/messages` endpoint

        **For document engrams:**

        - Provide either `raw_text` or `chunks` to append additional content
        - Content will be processed and added to the engram

        Args:
          id: The unique identifier of the engram

          collection_id: Target collection ID for the appended content.

          chunks: Pre-processed text chunks to append (for document engrams).

          ingestion_config: Optional ingestion configuration override (for document engrams).

          ingestion_mode: Ingestion mode for document content (ignored for conversations).

          messages: List of messages to append (for conversation engrams). Each has content, role,
              optional parent_id, metadata, authority.

          metadata: Additional metadata for the appended content.

          raw_text: Raw text content to append (for document engrams).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            MemoryAppendResponse,
            self._post(
                path_template("/v1/memories/{id}/append", id=id),
                body=maybe_transform(
                    {
                        "collection_id": collection_id,
                        "chunks": chunks,
                        "ingestion_config": ingestion_config,
                        "ingestion_mode": ingestion_mode,
                        "messages": messages,
                        "metadata": metadata,
                        "raw_text": raw_text,
                    },
                    memory_append_params.MemoryAppendParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryAppendResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def deduplicate_entities(
        self,
        id: str,
        *,
        automatic_clustering: bool | Omit = omit,
        automatic_deduplication: bool | Omit = omit,
        chunk_merge_count: int | Omit = omit,
        conversation_context_enabled: bool | Omit = omit,
        conversation_context_window_size: int | Omit = omit,
        conversation_summary_update_frequency: int | Omit = omit,
        entity_deduplication: Optional[memory_deduplicate_entities_params.EntityDeduplication] | Omit = omit,
        entity_types: SequenceNotStr[str] | Omit = omit,
        generation_config: Optional[GenerationConfigParam] | Omit = omit,
        graph_entity_description_prompt: str | Omit = omit,
        graph_extraction_prompt: str | Omit = omit,
        idle_check_interval_minutes: int | Omit = omit,
        idle_full_clustering: bool | Omit = omit,
        incremental_clustering: bool | Omit = omit,
        incremental_jaccard_filter: float | Omit = omit,
        incremental_jaccard_reuse_threshold: float | Omit = omit,
        incremental_min_cluster_size: int | Omit = omit,
        incremental_neighbor_hops: int | Omit = omit,
        incremental_structural_affinity_threshold: float | Omit = omit,
        max_concurrent_entities_per_extraction: int | Omit = omit,
        max_concurrent_relationships_per_extraction: int | Omit = omit,
        max_description_input_length: int | Omit = omit,
        max_knowledge_relationships: int | Omit = omit,
        relation_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Deduplicates entities from an engram.

        Args:
          id: The ID of the engram to extract entities and relationships from.

          automatic_clustering: Whether to automatically trigger graph clustering after entity deduplication.

          automatic_deduplication: Whether to automatically deduplicate entities.

          chunk_merge_count: The number of extractions to merge into a single graph extraction.

          conversation_context_enabled: Whether to include multi-message context windows when extracting from
              conversations. Enables temporal continuity across messages.

          conversation_context_window_size: Number of recent messages to include verbatim in engram_summary for conversation
              context. Messages beyond this window are summarized.

          conversation_summary_update_frequency: How often (in number of messages) to re-summarize older conversation context.
              Lower values give fresher summaries but cost more. Set to 0 to disable summary
              caching and always summarize on-the-fly.

          entity_deduplication: Enhanced settings for entity deduplication.

          entity_types: The types of entities to extract.

          generation_config: Configuration for text generation during graph enrichment.

          graph_entity_description_prompt: The prompt to use for entity description generation.

          graph_extraction_prompt: The prompt to use for knowledge graph extraction.

          idle_check_interval_minutes: Interval in minutes to check for idle system state for full re-clustering.

          idle_full_clustering: Whether to trigger full re-clustering during idle periods when no other
              workflows are active.

          incremental_clustering: Enable incremental (streaming) clustering updates after each ingestion.

          incremental_jaccard_filter: Lightweight Jaccard filter when in 'leiden' mode; used only to prune obviously
              unrelated communities.

          incremental_jaccard_reuse_threshold: Minimum Jaccard overlap to reuse an existing community during incremental
              updates.

          incremental_min_cluster_size: Minimum size of a new incremental cluster before considering promotion.

          incremental_neighbor_hops: Number of hops around changed entities to include in incremental subgraph.

          incremental_structural_affinity_threshold: Minimum structural affinity (local modularity proxy) to reuse an existing
              community in incremental updates.

          max_concurrent_entities_per_extraction: Maximum number of entities to create concurrently per extraction. Set to 1 for
              sequential processing.

          max_concurrent_relationships_per_extraction: Maximum number of relationships to process concurrently per extraction. Set to 1
              for sequential processing.

          max_description_input_length: The maximum length of the description for a node in the graph.

          max_knowledge_relationships: The maximum number of knowledge relationships to extract from each chunk.

          relation_types: The types of relations to extract.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/memories/{id}/deduplicate", id=id),
            body=maybe_transform(
                {
                    "automatic_clustering": automatic_clustering,
                    "automatic_deduplication": automatic_deduplication,
                    "chunk_merge_count": chunk_merge_count,
                    "conversation_context_enabled": conversation_context_enabled,
                    "conversation_context_window_size": conversation_context_window_size,
                    "conversation_summary_update_frequency": conversation_summary_update_frequency,
                    "entity_deduplication": entity_deduplication,
                    "entity_types": entity_types,
                    "generation_config": generation_config,
                    "graph_entity_description_prompt": graph_entity_description_prompt,
                    "graph_extraction_prompt": graph_extraction_prompt,
                    "idle_check_interval_minutes": idle_check_interval_minutes,
                    "idle_full_clustering": idle_full_clustering,
                    "incremental_clustering": incremental_clustering,
                    "incremental_jaccard_filter": incremental_jaccard_filter,
                    "incremental_jaccard_reuse_threshold": incremental_jaccard_reuse_threshold,
                    "incremental_min_cluster_size": incremental_min_cluster_size,
                    "incremental_neighbor_hops": incremental_neighbor_hops,
                    "incremental_structural_affinity_threshold": incremental_structural_affinity_threshold,
                    "max_concurrent_entities_per_extraction": max_concurrent_entities_per_extraction,
                    "max_concurrent_relationships_per_extraction": max_concurrent_relationships_per_extraction,
                    "max_description_input_length": max_description_input_length,
                    "max_knowledge_relationships": max_knowledge_relationships,
                    "relation_types": relation_types,
                },
                memory_deduplicate_entities_params.MemoryDeduplicateEntitiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def delete_by_filter(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete engrams based on provided filters.

        Allowed operators include: `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`. Deletion requests are limited to a user's own engrams.

        Args:
          body: JSON-encoded filters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/memories/by-filter",
            body=maybe_transform(body, memory_delete_by_filter_params.MemoryDeleteByFilterParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    @overload
    def delete_multiple(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteMultipleResponse:
        """
        Delete one or more engrams.

        This endpoint efficiently handles both single and batch deletions. When multiple
        IDs are provided, it uses optimized batch operations.

        Args: ids: Either a single UUID or a list of UUIDs to delete

        Returns: For single deletion: boolean success response For batch deletion:
        detailed results with successful and failed deletions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def delete_multiple(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteMultipleResponse:
        """
        Delete one or more engrams.

        This endpoint efficiently handles both single and batch deletions. When multiple
        IDs are provided, it uses optimized batch operations.

        Args: ids: Either a single UUID or a list of UUIDs to delete

        Returns: For single deletion: boolean success response For batch deletion:
        detailed results with successful and failed deletions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    def delete_multiple(
        self,
        *,
        body: str | SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteMultipleResponse:
        return cast(
            MemoryDeleteMultipleResponse,
            self._post(
                "/v1/memories/delete",
                body=maybe_transform(body, memory_delete_multiple_params.MemoryDeleteMultipleParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryDeleteMultipleResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def download_content(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Downloads the original file content of an engram.

        For uploaded files, returns the original file with its proper MIME type. For
        text-only engrams, returns the content as plain text.

        Users can only download engrams they own or have access to through collections.

        Args:
          id: Engram ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/v1/memories/{id}/download", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def download_zip(
        self,
        *,
        end_date: Union[str, datetime, None] | Omit = omit,
        engram_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Export multiple engrams as a zip file.

        Engrams can be filtered by IDs and/or
        date range.

        The endpoint allows downloading:

        - Specific engrams by providing their IDs
        - Engrams within a date range
        - All accessible engrams if no filters are provided

        Files are streamed as a zip archive to handle potentially large downloads
        efficiently.

        Args:
          end_date: Filter engrams created before this date.

          engram_ids: List of engram IDs to include in the export. If not provided, all accessible
              engrams will be included.

          start_date: Filter engrams created on or after this date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v1/memories/download_zip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "engram_ids": engram_ids,
                        "start_date": start_date,
                    },
                    memory_download_zip_params.MemoryDownloadZipParams,
                ),
            ),
            cast_to=NoneType,
        )

    def export(
        self,
        *,
        columns: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        include_header: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export engrams as a downloadable CSV file.

        Args:
          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memories/export",
            body=maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                memory_export_params.MemoryExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def extract_entities(
        self,
        id: str,
        *,
        automatic_clustering: bool | Omit = omit,
        automatic_deduplication: bool | Omit = omit,
        chunk_merge_count: int | Omit = omit,
        conversation_context_enabled: bool | Omit = omit,
        conversation_context_window_size: int | Omit = omit,
        conversation_summary_update_frequency: int | Omit = omit,
        entity_deduplication: Optional[memory_extract_entities_params.EntityDeduplication] | Omit = omit,
        entity_types: SequenceNotStr[str] | Omit = omit,
        generation_config: Optional[GenerationConfigParam] | Omit = omit,
        graph_entity_description_prompt: str | Omit = omit,
        graph_extraction_prompt: str | Omit = omit,
        idle_check_interval_minutes: int | Omit = omit,
        idle_full_clustering: bool | Omit = omit,
        incremental_clustering: bool | Omit = omit,
        incremental_jaccard_filter: float | Omit = omit,
        incremental_jaccard_reuse_threshold: float | Omit = omit,
        incremental_min_cluster_size: int | Omit = omit,
        incremental_neighbor_hops: int | Omit = omit,
        incremental_structural_affinity_threshold: float | Omit = omit,
        max_concurrent_entities_per_extraction: int | Omit = omit,
        max_concurrent_relationships_per_extraction: int | Omit = omit,
        max_description_input_length: int | Omit = omit,
        max_knowledge_relationships: int | Omit = omit,
        relation_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Extracts entities and relationships from an engram.

        The entities and relationships extraction process involves:

            1. Parsing engrams into semantic chunks

            2. Extracting entities and relationships using LLMs

            3. Storing the created entities and relationships in the knowledge graph

            4. Preserving the engram's metadata and content, and associating the elements with collections the engram belongs to

        Args:
          id: The ID of the engram to extract entities and relationships from.

          automatic_clustering: Whether to automatically trigger graph clustering after entity deduplication.

          automatic_deduplication: Whether to automatically deduplicate entities.

          chunk_merge_count: The number of extractions to merge into a single graph extraction.

          conversation_context_enabled: Whether to include multi-message context windows when extracting from
              conversations. Enables temporal continuity across messages.

          conversation_context_window_size: Number of recent messages to include verbatim in engram_summary for conversation
              context. Messages beyond this window are summarized.

          conversation_summary_update_frequency: How often (in number of messages) to re-summarize older conversation context.
              Lower values give fresher summaries but cost more. Set to 0 to disable summary
              caching and always summarize on-the-fly.

          entity_deduplication: Enhanced settings for entity deduplication.

          entity_types: The types of entities to extract.

          generation_config: Configuration for text generation during graph enrichment.

          graph_entity_description_prompt: The prompt to use for entity description generation.

          graph_extraction_prompt: The prompt to use for knowledge graph extraction.

          idle_check_interval_minutes: Interval in minutes to check for idle system state for full re-clustering.

          idle_full_clustering: Whether to trigger full re-clustering during idle periods when no other
              workflows are active.

          incremental_clustering: Enable incremental (streaming) clustering updates after each ingestion.

          incremental_jaccard_filter: Lightweight Jaccard filter when in 'leiden' mode; used only to prune obviously
              unrelated communities.

          incremental_jaccard_reuse_threshold: Minimum Jaccard overlap to reuse an existing community during incremental
              updates.

          incremental_min_cluster_size: Minimum size of a new incremental cluster before considering promotion.

          incremental_neighbor_hops: Number of hops around changed entities to include in incremental subgraph.

          incremental_structural_affinity_threshold: Minimum structural affinity (local modularity proxy) to reuse an existing
              community in incremental updates.

          max_concurrent_entities_per_extraction: Maximum number of entities to create concurrently per extraction. Set to 1 for
              sequential processing.

          max_concurrent_relationships_per_extraction: Maximum number of relationships to process concurrently per extraction. Set to 1
              for sequential processing.

          max_description_input_length: The maximum length of the description for a node in the graph.

          max_knowledge_relationships: The maximum number of knowledge relationships to extract from each chunk.

          relation_types: The types of relations to extract.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/memories/{id}/extract", id=id),
            body=maybe_transform(
                {
                    "automatic_clustering": automatic_clustering,
                    "automatic_deduplication": automatic_deduplication,
                    "chunk_merge_count": chunk_merge_count,
                    "conversation_context_enabled": conversation_context_enabled,
                    "conversation_context_window_size": conversation_context_window_size,
                    "conversation_summary_update_frequency": conversation_summary_update_frequency,
                    "entity_deduplication": entity_deduplication,
                    "entity_types": entity_types,
                    "generation_config": generation_config,
                    "graph_entity_description_prompt": graph_entity_description_prompt,
                    "graph_extraction_prompt": graph_extraction_prompt,
                    "idle_check_interval_minutes": idle_check_interval_minutes,
                    "idle_full_clustering": idle_full_clustering,
                    "incremental_clustering": incremental_clustering,
                    "incremental_jaccard_filter": incremental_jaccard_filter,
                    "incremental_jaccard_reuse_threshold": incremental_jaccard_reuse_threshold,
                    "incremental_min_cluster_size": incremental_min_cluster_size,
                    "incremental_neighbor_hops": incremental_neighbor_hops,
                    "incremental_structural_affinity_threshold": incremental_structural_affinity_threshold,
                    "max_concurrent_entities_per_extraction": max_concurrent_entities_per_extraction,
                    "max_concurrent_relationships_per_extraction": max_concurrent_relationships_per_extraction,
                    "max_description_input_length": max_description_input_length,
                    "max_knowledge_relationships": max_knowledge_relationships,
                    "relation_types": relation_types,
                },
                memory_extract_entities_params.MemoryExtractEntitiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def list_chunks(
        self,
        id: str,
        *,
        include_vectors: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListChunkResponse:
        """
        Retrieves the text chunks that were generated from an engram during ingestion.
        Chunks represent semantic sections of the engram and are used for retrieval and
        analysis.

        Users can only access chunks from engrams they own or have access to through
        collections. Vector embeddings are only included if specifically requested.

        Results are returned in chunk sequence order, representing their position in the
        original engram.

        Args:
          id: The ID of the engram to retrieve chunks for.

          include_vectors: Whether to include vector embeddings in the response.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/memories/{id}/chunks", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_vectors": include_vectors,
                        "limit": limit,
                        "offset": offset,
                    },
                    memory_list_chunks_params.MemoryListChunksParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListChunkResponse,
        )

    def list_collections(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListCollectionResponse:
        """Retrieves all collections that contain the specified engram.

        This endpoint is
        restricted to superusers only and provides a system-wide view of engram
        organization.

        Collections are used to organize engrams and manage access control. An engram
        can belong to multiple collections, and users can access engrams through
        collection membership.

        The results are paginated and ordered by collection creation date, with the most
        recently created collections appearing first.

        NOTE - This endpoint is only available to superusers, it will be extended to
        regular users in a future release.

        Args:
          id: Engram ID

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/memories/{id}/collections", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    memory_list_collections_params.MemoryListCollectionsParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListCollectionResponse,
        )

    def search(
        self,
        *,
        query: str,
        search_mode: SearchMode | Omit = omit,
        search_settings: SearchSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Perform a search query on the automatically generated engram summaries in the
        system.

        This endpoint allows for complex filtering of search results using
        PostgreSQL-based queries. Filters can be applied to various fields such as
        engram_id, and internal metadata values.

        Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`.

        Args:
          query: The search query to perform.

          search_mode:
              Graph search algorithm selection:

              `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
              with set transformers (max_depth=3, contextualized scoring, default)

              All modes now use depth=3 for optimal speed + relevance balance. All search
              settings can be controlled via `search_settings` regardless of mode.

          search_settings: Settings for engram search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memories/search",
            body=maybe_transform(
                {
                    "query": query,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchResponse,
        )


class AsyncMemoriesResource(AsyncAPIResource):
    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        return AsyncEntitiesResource(self._client)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResource:
        return AsyncRelationshipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncMemoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_ref: str,
        engram_type: Literal["conversation", "document"],
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        ingestion_config: Optional[IngestionConfigParam] | Omit = omit,
        ingestion_mode: Optional[IngestionMode] | Omit = omit,
        messages: Optional[Iterable[memory_create_params.Message]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        raw_text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a new memory (conversation or document) using clean JSON body.

        - Use `collection_ref` (UUID or name) instead of `collection_ids`
        - Discriminated union on `engram_type`: "conversation" or "document"
        - For conversations: provide `messages` array
        - For documents: provide `raw_text` or `chunks`

        Args:
          collection_ref: Collection UUID or name

          engram_type: Type of memory to create

          chunks: Pre-chunked text for document type

          ingestion_config: Custom ingestion config for documents

          ingestion_mode: Ingestion mode for documents

          messages: Messages for conversation type

          metadata: Metadata for the memory

          name: Optional name for the memory

          raw_text: Raw text content for document type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memories",
            body=await async_maybe_transform(
                {
                    "collection_ref": collection_ref,
                    "engram_type": engram_type,
                    "chunks": chunks,
                    "ingestion_config": ingestion_config,
                    "ingestion_mode": ingestion_mode,
                    "messages": messages,
                    "metadata": metadata,
                    "name": name,
                    "raw_text": raw_text,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """
        Retrieves detailed information about a specific engram by its ID.

        This endpoint returns the engram's metadata, status, and system information. It
        does not return the engram's content - use the `/engrams/{id}/download` endpoint
        for that.

        Users can only retrieve engrams they own or have access to through collections.
        Superusers can retrieve any engram.

        Args:
          id: The ID of the engram to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/memories/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )

    async def update(
        self,
        id: str,
        *,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        merge_metadata: bool | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsEngramResponse:
        """
        Update memory-level properties including name, metadata, and collection
        associations.

        This endpoint allows updating properties of an entire memory (document or
        conversation) without modifying its content:

        - **name**: Updates the title field in the engrams table
        - **metadata**: Can replace or merge with existing metadata
        - **collection_ids**: Updates engram_collections table associations

        Users can only update memories they own or have access to through collections.
        At least one collection association must be maintained.

        Args:
          id: The unique identifier of the memory

          collection_ids: New collection associations

          merge_metadata: Merge with existing metadata

          metadata: Metadata to update

          name: New name for the memory

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/memories/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "merge_metadata": merge_metadata,
                    "metadata": metadata,
                    "name": name,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsEngramResponse,
        )

    async def list(
        self,
        *,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_summary_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        metadata_filters: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        owner_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListEngramResponse:
        """
        Returns a paginated list of engrams the authenticated user has access to.

        Results can be filtered by providing specific engram IDs or collection IDs.
        Regular users will only see engrams they own or have access to through
        collections. Superusers can see all engrams.

        The engrams are returned in order of last modification, with most recent first.
        The response includes the engram's text field if available.

        Args:
          collection_ids: Optional list of collection IDs to filter engrams by. If provided, exactly one
              collection ID must be specified.

          ids: A list of engram IDs to retrieve. If not provided, all engrams will be returned.

          include_summary_embeddings: Specifies whether or not to include embeddings of each engram summary.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          metadata_filters:
              JSON string for metadata filtering. Example: '{"metadata.source": {"$eq":
              "playground"}}'

          offset: Specifies the number of objects to skip. Defaults to 0.

          owner_only: If true, only returns engrams owned by the user, not all accessible engrams.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/memories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collection_ids": collection_ids,
                        "ids": ids,
                        "include_summary_embeddings": include_summary_embeddings,
                        "limit": limit,
                        "metadata_filters": metadata_filters,
                        "offset": offset,
                        "owner_only": owner_only,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListEngramResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """Delete a specific engram with graph awareness.

        All chunks corresponding to the
        engram are deleted, and graph components (entities/relationships) are updated or
        deleted based on remaining chunk references from other engrams.

        This method now properly handles graph components and maintains graph integrity
        for search operations.

        Args:
          id: Engram ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/memories/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    async def append(
        self,
        id: str,
        *,
        collection_id: str,
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        ingestion_config: Optional[IngestionConfigParam] | Omit = omit,
        ingestion_mode: IngestionMode | Omit = omit,
        messages: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        raw_text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryAppendResponse:
        """
        Append content to an existing engram.

        **For conversation engrams:**

        - Provide `messages` array with content, role, and optional metadata
        - Works like `/conversations/{id}/messages` endpoint

        **For document engrams:**

        - Provide either `raw_text` or `chunks` to append additional content
        - Content will be processed and added to the engram

        Args:
          id: The unique identifier of the engram

          collection_id: Target collection ID for the appended content.

          chunks: Pre-processed text chunks to append (for document engrams).

          ingestion_config: Optional ingestion configuration override (for document engrams).

          ingestion_mode: Ingestion mode for document content (ignored for conversations).

          messages: List of messages to append (for conversation engrams). Each has content, role,
              optional parent_id, metadata, authority.

          metadata: Additional metadata for the appended content.

          raw_text: Raw text content to append (for document engrams).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            MemoryAppendResponse,
            await self._post(
                path_template("/v1/memories/{id}/append", id=id),
                body=await async_maybe_transform(
                    {
                        "collection_id": collection_id,
                        "chunks": chunks,
                        "ingestion_config": ingestion_config,
                        "ingestion_mode": ingestion_mode,
                        "messages": messages,
                        "metadata": metadata,
                        "raw_text": raw_text,
                    },
                    memory_append_params.MemoryAppendParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryAppendResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def deduplicate_entities(
        self,
        id: str,
        *,
        automatic_clustering: bool | Omit = omit,
        automatic_deduplication: bool | Omit = omit,
        chunk_merge_count: int | Omit = omit,
        conversation_context_enabled: bool | Omit = omit,
        conversation_context_window_size: int | Omit = omit,
        conversation_summary_update_frequency: int | Omit = omit,
        entity_deduplication: Optional[memory_deduplicate_entities_params.EntityDeduplication] | Omit = omit,
        entity_types: SequenceNotStr[str] | Omit = omit,
        generation_config: Optional[GenerationConfigParam] | Omit = omit,
        graph_entity_description_prompt: str | Omit = omit,
        graph_extraction_prompt: str | Omit = omit,
        idle_check_interval_minutes: int | Omit = omit,
        idle_full_clustering: bool | Omit = omit,
        incremental_clustering: bool | Omit = omit,
        incremental_jaccard_filter: float | Omit = omit,
        incremental_jaccard_reuse_threshold: float | Omit = omit,
        incremental_min_cluster_size: int | Omit = omit,
        incremental_neighbor_hops: int | Omit = omit,
        incremental_structural_affinity_threshold: float | Omit = omit,
        max_concurrent_entities_per_extraction: int | Omit = omit,
        max_concurrent_relationships_per_extraction: int | Omit = omit,
        max_description_input_length: int | Omit = omit,
        max_knowledge_relationships: int | Omit = omit,
        relation_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Deduplicates entities from an engram.

        Args:
          id: The ID of the engram to extract entities and relationships from.

          automatic_clustering: Whether to automatically trigger graph clustering after entity deduplication.

          automatic_deduplication: Whether to automatically deduplicate entities.

          chunk_merge_count: The number of extractions to merge into a single graph extraction.

          conversation_context_enabled: Whether to include multi-message context windows when extracting from
              conversations. Enables temporal continuity across messages.

          conversation_context_window_size: Number of recent messages to include verbatim in engram_summary for conversation
              context. Messages beyond this window are summarized.

          conversation_summary_update_frequency: How often (in number of messages) to re-summarize older conversation context.
              Lower values give fresher summaries but cost more. Set to 0 to disable summary
              caching and always summarize on-the-fly.

          entity_deduplication: Enhanced settings for entity deduplication.

          entity_types: The types of entities to extract.

          generation_config: Configuration for text generation during graph enrichment.

          graph_entity_description_prompt: The prompt to use for entity description generation.

          graph_extraction_prompt: The prompt to use for knowledge graph extraction.

          idle_check_interval_minutes: Interval in minutes to check for idle system state for full re-clustering.

          idle_full_clustering: Whether to trigger full re-clustering during idle periods when no other
              workflows are active.

          incremental_clustering: Enable incremental (streaming) clustering updates after each ingestion.

          incremental_jaccard_filter: Lightweight Jaccard filter when in 'leiden' mode; used only to prune obviously
              unrelated communities.

          incremental_jaccard_reuse_threshold: Minimum Jaccard overlap to reuse an existing community during incremental
              updates.

          incremental_min_cluster_size: Minimum size of a new incremental cluster before considering promotion.

          incremental_neighbor_hops: Number of hops around changed entities to include in incremental subgraph.

          incremental_structural_affinity_threshold: Minimum structural affinity (local modularity proxy) to reuse an existing
              community in incremental updates.

          max_concurrent_entities_per_extraction: Maximum number of entities to create concurrently per extraction. Set to 1 for
              sequential processing.

          max_concurrent_relationships_per_extraction: Maximum number of relationships to process concurrently per extraction. Set to 1
              for sequential processing.

          max_description_input_length: The maximum length of the description for a node in the graph.

          max_knowledge_relationships: The maximum number of knowledge relationships to extract from each chunk.

          relation_types: The types of relations to extract.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/memories/{id}/deduplicate", id=id),
            body=await async_maybe_transform(
                {
                    "automatic_clustering": automatic_clustering,
                    "automatic_deduplication": automatic_deduplication,
                    "chunk_merge_count": chunk_merge_count,
                    "conversation_context_enabled": conversation_context_enabled,
                    "conversation_context_window_size": conversation_context_window_size,
                    "conversation_summary_update_frequency": conversation_summary_update_frequency,
                    "entity_deduplication": entity_deduplication,
                    "entity_types": entity_types,
                    "generation_config": generation_config,
                    "graph_entity_description_prompt": graph_entity_description_prompt,
                    "graph_extraction_prompt": graph_extraction_prompt,
                    "idle_check_interval_minutes": idle_check_interval_minutes,
                    "idle_full_clustering": idle_full_clustering,
                    "incremental_clustering": incremental_clustering,
                    "incremental_jaccard_filter": incremental_jaccard_filter,
                    "incremental_jaccard_reuse_threshold": incremental_jaccard_reuse_threshold,
                    "incremental_min_cluster_size": incremental_min_cluster_size,
                    "incremental_neighbor_hops": incremental_neighbor_hops,
                    "incremental_structural_affinity_threshold": incremental_structural_affinity_threshold,
                    "max_concurrent_entities_per_extraction": max_concurrent_entities_per_extraction,
                    "max_concurrent_relationships_per_extraction": max_concurrent_relationships_per_extraction,
                    "max_description_input_length": max_description_input_length,
                    "max_knowledge_relationships": max_knowledge_relationships,
                    "relation_types": relation_types,
                },
                memory_deduplicate_entities_params.MemoryDeduplicateEntitiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def delete_by_filter(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericBooleanResponse:
        """
        Delete engrams based on provided filters.

        Allowed operators include: `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`. Deletion requests are limited to a user's own engrams.

        Args:
          body: JSON-encoded filters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/memories/by-filter",
            body=await async_maybe_transform(body, memory_delete_by_filter_params.MemoryDeleteByFilterParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
        )

    @overload
    async def delete_multiple(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteMultipleResponse:
        """
        Delete one or more engrams.

        This endpoint efficiently handles both single and batch deletions. When multiple
        IDs are provided, it uses optimized batch operations.

        Args: ids: Either a single UUID or a list of UUIDs to delete

        Returns: For single deletion: boolean success response For batch deletion:
        detailed results with successful and failed deletions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def delete_multiple(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteMultipleResponse:
        """
        Delete one or more engrams.

        This endpoint efficiently handles both single and batch deletions. When multiple
        IDs are provided, it uses optimized batch operations.

        Args: ids: Either a single UUID or a list of UUIDs to delete

        Returns: For single deletion: boolean success response For batch deletion:
        detailed results with successful and failed deletions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    async def delete_multiple(
        self,
        *,
        body: str | SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteMultipleResponse:
        return cast(
            MemoryDeleteMultipleResponse,
            await self._post(
                "/v1/memories/delete",
                body=await async_maybe_transform(body, memory_delete_multiple_params.MemoryDeleteMultipleParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryDeleteMultipleResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def download_content(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Downloads the original file content of an engram.

        For uploaded files, returns the original file with its proper MIME type. For
        text-only engrams, returns the content as plain text.

        Users can only download engrams they own or have access to through collections.

        Args:
          id: Engram ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/memories/{id}/download", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def download_zip(
        self,
        *,
        end_date: Union[str, datetime, None] | Omit = omit,
        engram_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Export multiple engrams as a zip file.

        Engrams can be filtered by IDs and/or
        date range.

        The endpoint allows downloading:

        - Specific engrams by providing their IDs
        - Engrams within a date range
        - All accessible engrams if no filters are provided

        Files are streamed as a zip archive to handle potentially large downloads
        efficiently.

        Args:
          end_date: Filter engrams created before this date.

          engram_ids: List of engram IDs to include in the export. If not provided, all accessible
              engrams will be included.

          start_date: Filter engrams created on or after this date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v1/memories/download_zip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "engram_ids": engram_ids,
                        "start_date": start_date,
                    },
                    memory_download_zip_params.MemoryDownloadZipParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def export(
        self,
        *,
        columns: Optional[SequenceNotStr[str]] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        include_header: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export engrams as a downloadable CSV file.

        Args:
          columns: Specific columns to export

          filters: Filters to apply to the export

          include_header: Whether to include column headers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memories/export",
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                memory_export_params.MemoryExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def extract_entities(
        self,
        id: str,
        *,
        automatic_clustering: bool | Omit = omit,
        automatic_deduplication: bool | Omit = omit,
        chunk_merge_count: int | Omit = omit,
        conversation_context_enabled: bool | Omit = omit,
        conversation_context_window_size: int | Omit = omit,
        conversation_summary_update_frequency: int | Omit = omit,
        entity_deduplication: Optional[memory_extract_entities_params.EntityDeduplication] | Omit = omit,
        entity_types: SequenceNotStr[str] | Omit = omit,
        generation_config: Optional[GenerationConfigParam] | Omit = omit,
        graph_entity_description_prompt: str | Omit = omit,
        graph_extraction_prompt: str | Omit = omit,
        idle_check_interval_minutes: int | Omit = omit,
        idle_full_clustering: bool | Omit = omit,
        incremental_clustering: bool | Omit = omit,
        incremental_jaccard_filter: float | Omit = omit,
        incremental_jaccard_reuse_threshold: float | Omit = omit,
        incremental_min_cluster_size: int | Omit = omit,
        incremental_neighbor_hops: int | Omit = omit,
        incremental_structural_affinity_threshold: float | Omit = omit,
        max_concurrent_entities_per_extraction: int | Omit = omit,
        max_concurrent_relationships_per_extraction: int | Omit = omit,
        max_description_input_length: int | Omit = omit,
        max_knowledge_relationships: int | Omit = omit,
        relation_types: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsGenericMessageResponse:
        """
        Extracts entities and relationships from an engram.

        The entities and relationships extraction process involves:

            1. Parsing engrams into semantic chunks

            2. Extracting entities and relationships using LLMs

            3. Storing the created entities and relationships in the knowledge graph

            4. Preserving the engram's metadata and content, and associating the elements with collections the engram belongs to

        Args:
          id: The ID of the engram to extract entities and relationships from.

          automatic_clustering: Whether to automatically trigger graph clustering after entity deduplication.

          automatic_deduplication: Whether to automatically deduplicate entities.

          chunk_merge_count: The number of extractions to merge into a single graph extraction.

          conversation_context_enabled: Whether to include multi-message context windows when extracting from
              conversations. Enables temporal continuity across messages.

          conversation_context_window_size: Number of recent messages to include verbatim in engram_summary for conversation
              context. Messages beyond this window are summarized.

          conversation_summary_update_frequency: How often (in number of messages) to re-summarize older conversation context.
              Lower values give fresher summaries but cost more. Set to 0 to disable summary
              caching and always summarize on-the-fly.

          entity_deduplication: Enhanced settings for entity deduplication.

          entity_types: The types of entities to extract.

          generation_config: Configuration for text generation during graph enrichment.

          graph_entity_description_prompt: The prompt to use for entity description generation.

          graph_extraction_prompt: The prompt to use for knowledge graph extraction.

          idle_check_interval_minutes: Interval in minutes to check for idle system state for full re-clustering.

          idle_full_clustering: Whether to trigger full re-clustering during idle periods when no other
              workflows are active.

          incremental_clustering: Enable incremental (streaming) clustering updates after each ingestion.

          incremental_jaccard_filter: Lightweight Jaccard filter when in 'leiden' mode; used only to prune obviously
              unrelated communities.

          incremental_jaccard_reuse_threshold: Minimum Jaccard overlap to reuse an existing community during incremental
              updates.

          incremental_min_cluster_size: Minimum size of a new incremental cluster before considering promotion.

          incremental_neighbor_hops: Number of hops around changed entities to include in incremental subgraph.

          incremental_structural_affinity_threshold: Minimum structural affinity (local modularity proxy) to reuse an existing
              community in incremental updates.

          max_concurrent_entities_per_extraction: Maximum number of entities to create concurrently per extraction. Set to 1 for
              sequential processing.

          max_concurrent_relationships_per_extraction: Maximum number of relationships to process concurrently per extraction. Set to 1
              for sequential processing.

          max_description_input_length: The maximum length of the description for a node in the graph.

          max_knowledge_relationships: The maximum number of knowledge relationships to extract from each chunk.

          relation_types: The types of relations to extract.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/memories/{id}/extract", id=id),
            body=await async_maybe_transform(
                {
                    "automatic_clustering": automatic_clustering,
                    "automatic_deduplication": automatic_deduplication,
                    "chunk_merge_count": chunk_merge_count,
                    "conversation_context_enabled": conversation_context_enabled,
                    "conversation_context_window_size": conversation_context_window_size,
                    "conversation_summary_update_frequency": conversation_summary_update_frequency,
                    "entity_deduplication": entity_deduplication,
                    "entity_types": entity_types,
                    "generation_config": generation_config,
                    "graph_entity_description_prompt": graph_entity_description_prompt,
                    "graph_extraction_prompt": graph_extraction_prompt,
                    "idle_check_interval_minutes": idle_check_interval_minutes,
                    "idle_full_clustering": idle_full_clustering,
                    "incremental_clustering": incremental_clustering,
                    "incremental_jaccard_filter": incremental_jaccard_filter,
                    "incremental_jaccard_reuse_threshold": incremental_jaccard_reuse_threshold,
                    "incremental_min_cluster_size": incremental_min_cluster_size,
                    "incremental_neighbor_hops": incremental_neighbor_hops,
                    "incremental_structural_affinity_threshold": incremental_structural_affinity_threshold,
                    "max_concurrent_entities_per_extraction": max_concurrent_entities_per_extraction,
                    "max_concurrent_relationships_per_extraction": max_concurrent_relationships_per_extraction,
                    "max_description_input_length": max_description_input_length,
                    "max_knowledge_relationships": max_knowledge_relationships,
                    "relation_types": relation_types,
                },
                memory_extract_entities_params.MemoryExtractEntitiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def list_chunks(
        self,
        id: str,
        *,
        include_vectors: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListChunkResponse:
        """
        Retrieves the text chunks that were generated from an engram during ingestion.
        Chunks represent semantic sections of the engram and are used for retrieval and
        analysis.

        Users can only access chunks from engrams they own or have access to through
        collections. Vector embeddings are only included if specifically requested.

        Results are returned in chunk sequence order, representing their position in the
        original engram.

        Args:
          id: The ID of the engram to retrieve chunks for.

          include_vectors: Whether to include vector embeddings in the response.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/memories/{id}/chunks", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_vectors": include_vectors,
                        "limit": limit,
                        "offset": offset,
                    },
                    memory_list_chunks_params.MemoryListChunksParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListChunkResponse,
        )

    async def list_collections(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListCollectionResponse:
        """Retrieves all collections that contain the specified engram.

        This endpoint is
        restricted to superusers only and provides a system-wide view of engram
        organization.

        Collections are used to organize engrams and manage access control. An engram
        can belong to multiple collections, and users can access engrams through
        collection membership.

        The results are paginated and ordered by collection creation date, with the most
        recently created collections appearing first.

        NOTE - This endpoint is only available to superusers, it will be extended to
        regular users in a future release.

        Args:
          id: Engram ID

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/memories/{id}/collections", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    memory_list_collections_params.MemoryListCollectionsParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListCollectionResponse,
        )

    async def search(
        self,
        *,
        query: str,
        search_mode: SearchMode | Omit = omit,
        search_settings: SearchSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Perform a search query on the automatically generated engram summaries in the
        system.

        This endpoint allows for complex filtering of search results using
        PostgreSQL-based queries. Filters can be applied to various fields such as
        engram_id, and internal metadata values.

        Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`,
        `ilike`, `in`, and `nin`.

        Args:
          query: The search query to perform.

          search_mode:
              Graph search algorithm selection:

              `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
              with set transformers (max_depth=3, contextualized scoring, default)

              All modes now use depth=3 for optimal speed + relevance balance. All search
              settings can be controlled via `search_settings` regardless of mode.

          search_settings: Settings for engram search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memories/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                },
                memory_search_params.MemorySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchResponse,
        )


class MemoriesResourceWithRawResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_raw_response_wrapper(
            memories.create,
        )
        self.retrieve = to_raw_response_wrapper(
            memories.retrieve,
        )
        self.update = to_raw_response_wrapper(
            memories.update,
        )
        self.list = to_raw_response_wrapper(
            memories.list,
        )
        self.delete = to_raw_response_wrapper(
            memories.delete,
        )
        self.append = to_raw_response_wrapper(
            memories.append,
        )
        self.deduplicate_entities = to_raw_response_wrapper(
            memories.deduplicate_entities,
        )
        self.delete_by_filter = to_raw_response_wrapper(
            memories.delete_by_filter,
        )
        self.delete_multiple = to_raw_response_wrapper(
            memories.delete_multiple,
        )
        self.download_content = to_raw_response_wrapper(
            memories.download_content,
        )
        self.download_zip = to_raw_response_wrapper(
            memories.download_zip,
        )
        self.export = to_raw_response_wrapper(
            memories.export,
        )
        self.extract_entities = to_raw_response_wrapper(
            memories.extract_entities,
        )
        self.list_chunks = to_raw_response_wrapper(
            memories.list_chunks,
        )
        self.list_collections = to_raw_response_wrapper(
            memories.list_collections,
        )
        self.search = to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._memories.metadata)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self._memories.entities)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithRawResponse:
        return RelationshipsResourceWithRawResponse(self._memories.relationships)


class AsyncMemoriesResourceWithRawResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_raw_response_wrapper(
            memories.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            memories.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            memories.update,
        )
        self.list = async_to_raw_response_wrapper(
            memories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            memories.delete,
        )
        self.append = async_to_raw_response_wrapper(
            memories.append,
        )
        self.deduplicate_entities = async_to_raw_response_wrapper(
            memories.deduplicate_entities,
        )
        self.delete_by_filter = async_to_raw_response_wrapper(
            memories.delete_by_filter,
        )
        self.delete_multiple = async_to_raw_response_wrapper(
            memories.delete_multiple,
        )
        self.download_content = async_to_raw_response_wrapper(
            memories.download_content,
        )
        self.download_zip = async_to_raw_response_wrapper(
            memories.download_zip,
        )
        self.export = async_to_raw_response_wrapper(
            memories.export,
        )
        self.extract_entities = async_to_raw_response_wrapper(
            memories.extract_entities,
        )
        self.list_chunks = async_to_raw_response_wrapper(
            memories.list_chunks,
        )
        self.list_collections = async_to_raw_response_wrapper(
            memories.list_collections,
        )
        self.search = async_to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._memories.metadata)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self._memories.entities)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithRawResponse:
        return AsyncRelationshipsResourceWithRawResponse(self._memories.relationships)


class MemoriesResourceWithStreamingResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_streamed_response_wrapper(
            memories.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            memories.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            memories.update,
        )
        self.list = to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = to_streamed_response_wrapper(
            memories.delete,
        )
        self.append = to_streamed_response_wrapper(
            memories.append,
        )
        self.deduplicate_entities = to_streamed_response_wrapper(
            memories.deduplicate_entities,
        )
        self.delete_by_filter = to_streamed_response_wrapper(
            memories.delete_by_filter,
        )
        self.delete_multiple = to_streamed_response_wrapper(
            memories.delete_multiple,
        )
        self.download_content = to_streamed_response_wrapper(
            memories.download_content,
        )
        self.download_zip = to_streamed_response_wrapper(
            memories.download_zip,
        )
        self.export = to_streamed_response_wrapper(
            memories.export,
        )
        self.extract_entities = to_streamed_response_wrapper(
            memories.extract_entities,
        )
        self.list_chunks = to_streamed_response_wrapper(
            memories.list_chunks,
        )
        self.list_collections = to_streamed_response_wrapper(
            memories.list_collections,
        )
        self.search = to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._memories.metadata)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self._memories.entities)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithStreamingResponse:
        return RelationshipsResourceWithStreamingResponse(self._memories.relationships)


class AsyncMemoriesResourceWithStreamingResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_streamed_response_wrapper(
            memories.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            memories.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            memories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            memories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            memories.delete,
        )
        self.append = async_to_streamed_response_wrapper(
            memories.append,
        )
        self.deduplicate_entities = async_to_streamed_response_wrapper(
            memories.deduplicate_entities,
        )
        self.delete_by_filter = async_to_streamed_response_wrapper(
            memories.delete_by_filter,
        )
        self.delete_multiple = async_to_streamed_response_wrapper(
            memories.delete_multiple,
        )
        self.download_content = async_to_streamed_response_wrapper(
            memories.download_content,
        )
        self.download_zip = async_to_streamed_response_wrapper(
            memories.download_zip,
        )
        self.export = async_to_streamed_response_wrapper(
            memories.export,
        )
        self.extract_entities = async_to_streamed_response_wrapper(
            memories.extract_entities,
        )
        self.list_chunks = async_to_streamed_response_wrapper(
            memories.list_chunks,
        )
        self.list_collections = async_to_streamed_response_wrapper(
            memories.list_collections,
        )
        self.search = async_to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._memories.metadata)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self._memories.entities)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        return AsyncRelationshipsResourceWithStreamingResponse(self._memories.relationships)
