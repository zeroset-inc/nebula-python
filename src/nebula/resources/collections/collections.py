# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import (
    collection_list_params,
    collection_create_params,
    collection_export_params,
    collection_update_params,
    collection_extract_params,
    collection_get_metrics_params,
    collection_validate_status_params,
    collection_retrieve_by_name_params,
    collection_get_documents_with_memories_params,
)
from .engrams import (
    EngramsResource,
    AsyncEngramsResource,
    EngramsResourceWithRawResponse,
    AsyncEngramsResourceWithRawResponse,
    EngramsResourceWithStreamingResponse,
    AsyncEngramsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.generation_config_param import GenerationConfigParam
from ...types.nebula_results_collection_response import NebulaResultsCollectionResponse
from ...types.nebula_results_generic_boolean_response import NebulaResultsGenericBooleanResponse
from ...types.paginated_nebula_result_list_collection_response import PaginatedNebulaResultListCollectionResponse
from ...types.collections.nebula_results_generic_message_response import NebulaResultsGenericMessageResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def engrams(self) -> EngramsResource:
        return EngramsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCollectionResponse:
        """
        Create a new collection and automatically add the creating user to it.

        This endpoint allows authenticated users to create a new collection with a
        specified name and optional description. The user creating the collection is
        automatically added as a member.

        Args:
          name: The name of the collection

          description: An optional description of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/collections",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCollectionResponse,
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
    ) -> NebulaResultsCollectionResponse:
        """
        Get details of a specific collection.

        This endpoint retrieves detailed information about a single collection
        identified by its UUID. The user must have access to the collection to view its
        details.

        Args:
          id: The unique identifier of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCollectionResponse,
        )

    def update(
        self,
        id: str,
        *,
        access_tier: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        generate_description: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCollectionResponse:
        """
        Update an existing collection's configuration.

        This endpoint allows updating the name, description, and access settings of an
        existing collection. The user must have appropriate permissions to modify the
        collection.

        Args:
          id: The unique identifier of the collection to update

          access_tier: Access tier for the collection: 'private', 'public_preview', or 'marketplace'

          description: An optional description of the collection

          generate_description: Whether to generate a new synthetic description for the collection

          name: The name of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/collections/{id}", id=id),
            body=maybe_transform(
                {
                    "access_tier": access_tier,
                    "description": description,
                    "generate_description": generate_description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCollectionResponse,
        )

    def list(
        self,
        *,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        owner_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListCollectionResponse:
        """
        Returns a paginated list of collections the authenticated user has access to.

        Results can be filtered by providing specific collection IDs. Regular users will
        only see collections they own or have access to. Superusers can see all
        collections.

        The collections are returned in order of last modification, with most recent
        first.

        Args:
          ids: A list of collection IDs to retrieve. If not provided, all collections will be
              returned.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          owner_only: If true, only returns collections owned by the user, not all accessible
              collections.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "offset": offset,
                        "owner_only": owner_only,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListCollectionResponse,
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
        """
        Delete an existing collection.

        This endpoint allows deletion of a collection identified by its UUID. The user
        must have appropriate permissions to delete the collection. Deleting a
        collection removes all associations but does not delete the engrams within it.

        Args:
          id: The unique identifier of the collection to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
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
        Export collections as a CSV file.

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
            "/v1/collections/export",
            body=maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                collection_export_params.CollectionExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def extract(
        self,
        id: str,
        *,
        automatic_clustering: bool | Omit = omit,
        automatic_deduplication: bool | Omit = omit,
        chunk_merge_count: int | Omit = omit,
        conversation_context_enabled: bool | Omit = omit,
        conversation_context_window_size: int | Omit = omit,
        conversation_summary_update_frequency: int | Omit = omit,
        entity_deduplication: Optional[collection_extract_params.EntityDeduplication] | Omit = omit,
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
            path_template("/v1/collections/{id}/extract", id=id),
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
                collection_extract_params.CollectionExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    def get_documents_with_memories(
        self,
        id: str,
        *,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get documents with their memory entries and embeddings for graph visualization.

        This endpoint retrieves documents (engrams) from a collection along with their
        associated memory entries (chunks). It includes embeddings needed for
        calculating semantic similarity in the graph visualization.

        Returns: - documents: List of documents with their memory entries - pagination:
        Pagination information

        Args:
          id: The unique identifier of the collection

          include_embeddings: Whether to include embedding vectors in the response

          limit: Number of documents to return (1-100)

          offset: Number of documents to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/collections/{id}/documents-with-memories", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_embeddings": include_embeddings,
                        "limit": limit,
                        "offset": offset,
                    },
                    collection_get_documents_with_memories_params.CollectionGetDocumentsWithMemoriesParams,
                ),
            ),
            cast_to=object,
        )

    def get_metrics(
        self,
        collection_id: str,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get metrics for a specific collection

        Args: collection_id: The collection UUID days: Number of days to include in time
        series (default: 14)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            path_template("/v1/collections/{collection_id}/metrics", collection_id=collection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"days": days}, collection_get_metrics_params.CollectionGetMetricsParams),
            ),
            cast_to=object,
        )

    def retrieve_by_name(
        self,
        collection_name: str,
        *,
        owner_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCollectionResponse:
        """
        Retrieve a collection by its (owner_id, name) combination.

        The authenticated user can only fetch collections they own, or, if superuser,
        from anyone.

        Args:
          collection_name: The name of the collection

          owner_id: (Superuser only) Specify the owner_id to retrieve a collection by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_name:
            raise ValueError(f"Expected a non-empty value for `collection_name` but received {collection_name!r}")
        return self._get(
            path_template("/v1/collections/name/{collection_name}", collection_name=collection_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"owner_id": owner_id}, collection_retrieve_by_name_params.CollectionRetrieveByNameParams
                ),
            ),
            cast_to=NebulaResultsCollectionResponse,
        )

    def validate_status(
        self,
        id: str,
        *,
        force_update: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Validate collection status against actual database state.

        This endpoint computes the collection status from the actual state of engrams
        and communities, compares it to the stored status, and updates if they are out
        of sync.

        Returns diagnostics including:

        - Stored vs computed status
        - Whether they are in sync
        - Extraction progress (engrams extracted/total)
        - Community count
        - Whether the status was updated

        Args:
          id: The unique identifier of the collection

          force_update: Force update to computed status even if already in sync

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/collections/{id}/validate-status", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force_update": force_update}, collection_validate_status_params.CollectionValidateStatusParams
                ),
            ),
            cast_to=object,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def engrams(self) -> AsyncEngramsResource:
        return AsyncEngramsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-py#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCollectionResponse:
        """
        Create a new collection and automatically add the creating user to it.

        This endpoint allows authenticated users to create a new collection with a
        specified name and optional description. The user creating the collection is
        automatically added as a member.

        Args:
          name: The name of the collection

          description: An optional description of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/collections",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCollectionResponse,
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
    ) -> NebulaResultsCollectionResponse:
        """
        Get details of a specific collection.

        This endpoint retrieves detailed information about a single collection
        identified by its UUID. The user must have access to the collection to view its
        details.

        Args:
          id: The unique identifier of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCollectionResponse,
        )

    async def update(
        self,
        id: str,
        *,
        access_tier: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        generate_description: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCollectionResponse:
        """
        Update an existing collection's configuration.

        This endpoint allows updating the name, description, and access settings of an
        existing collection. The user must have appropriate permissions to modify the
        collection.

        Args:
          id: The unique identifier of the collection to update

          access_tier: Access tier for the collection: 'private', 'public_preview', or 'marketplace'

          description: An optional description of the collection

          generate_description: Whether to generate a new synthetic description for the collection

          name: The name of the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/collections/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "access_tier": access_tier,
                    "description": description,
                    "generate_description": generate_description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsCollectionResponse,
        )

    async def list(
        self,
        *,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        owner_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedNebulaResultListCollectionResponse:
        """
        Returns a paginated list of collections the authenticated user has access to.

        Results can be filtered by providing specific collection IDs. Regular users will
        only see collections they own or have access to. Superusers can see all
        collections.

        The collections are returned in order of last modification, with most recent
        first.

        Args:
          ids: A list of collection IDs to retrieve. If not provided, all collections will be
              returned.

          limit: Specifies a limit on the number of objects to return, ranging between 1 and 100.
              Defaults to 100.

          offset: Specifies the number of objects to skip. Defaults to 0.

          owner_only: If true, only returns collections owned by the user, not all accessible
              collections.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "offset": offset,
                        "owner_only": owner_only,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=PaginatedNebulaResultListCollectionResponse,
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
        """
        Delete an existing collection.

        This endpoint allows deletion of a collection identified by its UUID. The user
        must have appropriate permissions to delete the collection. Deleting a
        collection removes all associations but does not delete the engrams within it.

        Args:
          id: The unique identifier of the collection to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericBooleanResponse,
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
        Export collections as a CSV file.

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
            "/v1/collections/export",
            body=await async_maybe_transform(
                {
                    "columns": columns,
                    "filters": filters,
                    "include_header": include_header,
                },
                collection_export_params.CollectionExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def extract(
        self,
        id: str,
        *,
        automatic_clustering: bool | Omit = omit,
        automatic_deduplication: bool | Omit = omit,
        chunk_merge_count: int | Omit = omit,
        conversation_context_enabled: bool | Omit = omit,
        conversation_context_window_size: int | Omit = omit,
        conversation_summary_update_frequency: int | Omit = omit,
        entity_deduplication: Optional[collection_extract_params.EntityDeduplication] | Omit = omit,
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
            path_template("/v1/collections/{id}/extract", id=id),
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
                collection_extract_params.CollectionExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NebulaResultsGenericMessageResponse,
        )

    async def get_documents_with_memories(
        self,
        id: str,
        *,
        include_embeddings: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get documents with their memory entries and embeddings for graph visualization.

        This endpoint retrieves documents (engrams) from a collection along with their
        associated memory entries (chunks). It includes embeddings needed for
        calculating semantic similarity in the graph visualization.

        Returns: - documents: List of documents with their memory entries - pagination:
        Pagination information

        Args:
          id: The unique identifier of the collection

          include_embeddings: Whether to include embedding vectors in the response

          limit: Number of documents to return (1-100)

          offset: Number of documents to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/collections/{id}/documents-with-memories", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_embeddings": include_embeddings,
                        "limit": limit,
                        "offset": offset,
                    },
                    collection_get_documents_with_memories_params.CollectionGetDocumentsWithMemoriesParams,
                ),
            ),
            cast_to=object,
        )

    async def get_metrics(
        self,
        collection_id: str,
        *,
        days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get metrics for a specific collection

        Args: collection_id: The collection UUID days: Number of days to include in time
        series (default: 14)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            path_template("/v1/collections/{collection_id}/metrics", collection_id=collection_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"days": days}, collection_get_metrics_params.CollectionGetMetricsParams
                ),
            ),
            cast_to=object,
        )

    async def retrieve_by_name(
        self,
        collection_name: str,
        *,
        owner_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NebulaResultsCollectionResponse:
        """
        Retrieve a collection by its (owner_id, name) combination.

        The authenticated user can only fetch collections they own, or, if superuser,
        from anyone.

        Args:
          collection_name: The name of the collection

          owner_id: (Superuser only) Specify the owner_id to retrieve a collection by name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_name:
            raise ValueError(f"Expected a non-empty value for `collection_name` but received {collection_name!r}")
        return await self._get(
            path_template("/v1/collections/name/{collection_name}", collection_name=collection_name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"owner_id": owner_id}, collection_retrieve_by_name_params.CollectionRetrieveByNameParams
                ),
            ),
            cast_to=NebulaResultsCollectionResponse,
        )

    async def validate_status(
        self,
        id: str,
        *,
        force_update: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Validate collection status against actual database state.

        This endpoint computes the collection status from the actual state of engrams
        and communities, compares it to the stored status, and updates if they are out
        of sync.

        Returns diagnostics including:

        - Stored vs computed status
        - Whether they are in sync
        - Extraction progress (engrams extracted/total)
        - Community count
        - Whether the status was updated

        Args:
          id: The unique identifier of the collection

          force_update: Force update to computed status even if already in sync

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/collections/{id}/validate-status", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force_update": force_update}, collection_validate_status_params.CollectionValidateStatusParams
                ),
            ),
            cast_to=object,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )
        self.export = to_raw_response_wrapper(
            collections.export,
        )
        self.extract = to_raw_response_wrapper(
            collections.extract,
        )
        self.get_documents_with_memories = to_raw_response_wrapper(
            collections.get_documents_with_memories,
        )
        self.get_metrics = to_raw_response_wrapper(
            collections.get_metrics,
        )
        self.retrieve_by_name = to_raw_response_wrapper(
            collections.retrieve_by_name,
        )
        self.validate_status = to_raw_response_wrapper(
            collections.validate_status,
        )

    @cached_property
    def engrams(self) -> EngramsResourceWithRawResponse:
        return EngramsResourceWithRawResponse(self._collections.engrams)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._collections.users)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
        self.export = async_to_raw_response_wrapper(
            collections.export,
        )
        self.extract = async_to_raw_response_wrapper(
            collections.extract,
        )
        self.get_documents_with_memories = async_to_raw_response_wrapper(
            collections.get_documents_with_memories,
        )
        self.get_metrics = async_to_raw_response_wrapper(
            collections.get_metrics,
        )
        self.retrieve_by_name = async_to_raw_response_wrapper(
            collections.retrieve_by_name,
        )
        self.validate_status = async_to_raw_response_wrapper(
            collections.validate_status,
        )

    @cached_property
    def engrams(self) -> AsyncEngramsResourceWithRawResponse:
        return AsyncEngramsResourceWithRawResponse(self._collections.engrams)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._collections.users)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )
        self.export = to_streamed_response_wrapper(
            collections.export,
        )
        self.extract = to_streamed_response_wrapper(
            collections.extract,
        )
        self.get_documents_with_memories = to_streamed_response_wrapper(
            collections.get_documents_with_memories,
        )
        self.get_metrics = to_streamed_response_wrapper(
            collections.get_metrics,
        )
        self.retrieve_by_name = to_streamed_response_wrapper(
            collections.retrieve_by_name,
        )
        self.validate_status = to_streamed_response_wrapper(
            collections.validate_status,
        )

    @cached_property
    def engrams(self) -> EngramsResourceWithStreamingResponse:
        return EngramsResourceWithStreamingResponse(self._collections.engrams)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._collections.users)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            collections.export,
        )
        self.extract = async_to_streamed_response_wrapper(
            collections.extract,
        )
        self.get_documents_with_memories = async_to_streamed_response_wrapper(
            collections.get_documents_with_memories,
        )
        self.get_metrics = async_to_streamed_response_wrapper(
            collections.get_metrics,
        )
        self.retrieve_by_name = async_to_streamed_response_wrapper(
            collections.retrieve_by_name,
        )
        self.validate_status = async_to_streamed_response_wrapper(
            collections.validate_status,
        )

    @cached_property
    def engrams(self) -> AsyncEngramsResourceWithStreamingResponse:
        return AsyncEngramsResourceWithStreamingResponse(self._collections.engrams)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._collections.users)
