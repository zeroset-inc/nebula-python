# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import (
    memory_list_params,
    memory_append_params,
    memory_create_params,
    memory_search_params,
    memory_update_params,
    memory_delete_many_params,
    memory_create_upload_params,
    memory_delete_upload_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.memory_list_response import MemoryListResponse
from ..types.memory_append_response import MemoryAppendResponse
from ..types.memory_create_response import MemoryCreateResponse
from ..types.memory_delete_response import MemoryDeleteResponse
from ..types.memory_search_response import MemorySearchResponse
from ..types.memory_update_response import MemoryUpdateResponse
from ..types.memory_retrieve_response import MemoryRetrieveResponse
from ..types.memory_delete_many_response import MemoryDeleteManyResponse
from ..types.memory_create_upload_response import MemoryCreateUploadResponse
from ..types.memory_delete_upload_response import MemoryDeleteUploadResponse

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
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
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        collection_id: Optional[str] | Omit = omit,
        content_parts: Optional[Iterable[memory_create_params.ContentPart]] | Omit = omit,
        contents: Optional[SequenceNotStr[str]] | Omit = omit,
        engram_type: Literal["document", "conversation"] | Omit = omit,
        ingestion_config: Optional[memory_create_params.IngestionConfig] | Omit = omit,
        ingestion_mode: Optional[Literal["hi-res", "ocr", "fast", "custom"]] | Omit = omit,
        messages: Optional[Iterable[memory_create_params.Message]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        raw_text: Optional[str] | Omit = omit,
        snapshot: Optional[memory_create_params.Snapshot] | Omit = omit,
        speaker_id: Optional[str] | Omit = omit,
        speaker_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateResponse:
        """
        Create a new memory (conversation or document) using clean JSON body.

        - Use `collection_id` (UUID)
        - `engram_type` is optional and inferred from payload shape:
          - If `messages` present -> conversation
          - Otherwise -> document
        - For conversations: provide `messages` array
        - For documents: provide `raw_text` or `chunks`
        - Use `snapshot` for device-memory mode (mutually exclusive with collection_id)

        Args:
          chunks: Pre-chunked text for document type

          collection_id: Collection UUID (mutually exclusive with snapshot)

          content_parts: Multimodal content parts (text, images, audio, documents) for document type.

          contents: Batch content strings for snapshot mode

          engram_type: Type of memory to create

          ingestion_config: Public ingestion config accepted by memory-ingestion endpoints.

              This mirrors the supported request payload shape while staying independent from
              the runtime provider config, which also carries internal-only fields such as
              `app` and `extra_fields`.

          ingestion_mode: Ingestion mode for documents

          messages: Messages for conversation type

          metadata: Metadata for the memory

          name: Optional name for the memory

          raw_text: Raw text content for document type

          snapshot: Portable full snapshot owned by the client.

          speaker_id: UUID of the SourceRole entity creating this memory

          speaker_name: Display name of the speaker/agent creating this memory

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            MemoryCreateResponse,
            self._post(
                "/v1/memories",
                body=maybe_transform(
                    {
                        "chunks": chunks,
                        "collection_id": collection_id,
                        "content_parts": content_parts,
                        "contents": contents,
                        "engram_type": engram_type,
                        "ingestion_config": ingestion_config,
                        "ingestion_mode": ingestion_mode,
                        "messages": messages,
                        "metadata": metadata,
                        "name": name,
                        "raw_text": raw_text,
                        "snapshot": snapshot,
                        "speaker_id": speaker_id,
                        "speaker_name": speaker_name,
                    },
                    memory_create_params.MemoryCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> MemoryRetrieveResponse:
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
            cast_to=MemoryRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        collection_id: Optional[str] | Omit = omit,
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
    ) -> MemoryUpdateResponse:
        """
        Update memory-level properties including name, metadata, and collection
        associations.

        This endpoint allows updating properties of an entire memory (document or
        conversation) without modifying its content:

        - **name**: Updates the authoritative engram title
        - **metadata**: Can replace or merge with existing metadata
        - **collection_ids**: Updates authoritative engram collection associations

        Users can only update memories they own or have access to through collections.
        At least one collection association must be maintained.

        If collection_id is provided and the engram is shared across collections, a
        copy-on-write will be performed to create a collection-specific copy before
        modification.

        Args:
          id: The unique identifier of the memory

          collection_id: Collection context for copy-on-write. If provided and engram is shared, creates
              a copy before modification.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"collection_id": collection_id}, memory_update_params.MemoryUpdateParams),
            ),
            cast_to=MemoryUpdateResponse,
        )

    def list(
        self,
        *,
        chunks_limit: Optional[int] | Omit = omit,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> MemoryListResponse:
        """
        Returns a paginated list of engrams the authenticated user has access to.

        Results can be filtered by providing specific engram IDs or collection IDs.
        Regular users will only see engrams they own or have access to through
        collections. Superusers can see all engrams.

        The engrams are returned in order of last modification, with most recent first.
        The response includes the engram's text field if available.

        Args:
          chunks_limit: Maximum chunks to inline per engram. Defaults to all chunks for backwards
              compatibility; pass 0 to skip chunk hydration.

          collection_ids: Optional list of collection IDs to filter engrams by. If provided, exactly one
              collection ID must be specified.

          ids: A list of engram IDs to retrieve. If not provided, all engrams will be returned.

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
                        "chunks_limit": chunks_limit,
                        "collection_ids": collection_ids,
                        "ids": ids,
                        "limit": limit,
                        "metadata_filters": metadata_filters,
                        "offset": offset,
                        "owner_only": owner_only,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            cast_to=MemoryListResponse,
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
    ) -> MemoryDeleteResponse:
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
            cast_to=MemoryDeleteResponse,
        )

    def append(
        self,
        id: str,
        *,
        collection_id: str,
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        ingestion_config: Optional[memory_append_params.IngestionConfig] | Omit = omit,
        ingestion_mode: Literal["hi-res", "ocr", "fast", "custom"] | Omit = omit,
        messages: Optional[Iterable[memory_append_params.Message]] | Omit = omit,
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

          chunks: Pre-processed text chunks to append for document memories.

          ingestion_config: Public ingestion config accepted by memory-ingestion endpoints.

              This mirrors the supported request payload shape while staying independent from
              the runtime provider config, which also carries internal-only fields such as
              `app` and `extra_fields`.

          ingestion_mode: Ingestion mode for document content.

          messages: Messages to append for conversation memories. Each message has content, role,
              and optional metadata.

          metadata: Additional metadata for the appended content.

          raw_text: Raw text content to append for document memories.

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

    def create_upload(
        self,
        *,
        content_type: str,
        file_size: int,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateUploadResponse:
        """
        Get a presigned URL for uploading large files directly to S3.

        Use this for files larger than 5MB that cannot be sent inline as base64. After
        uploading, reference the file in memory creation using S3FileReference.

        Args: filename: Original filename (e.g., "image.jpg") content_type: MIME type
        (e.g., "image/jpeg", "application/pdf") file_size: Expected file size in bytes
        (max 100MB)

        Returns: dict with: - upload_url: Presigned URL for PUT request (expires in 1
        hour) - upload_headers: Headers that must be sent with the presigned PUT
        request - s3_key: The S3 key to reference in memory creation - bucket: S3 bucket
        name - expires_in: Seconds until URL expires - max_size: Maximum allowed file
        size

        Args:
          content_type: MIME type (e.g., 'image/jpeg', 'application/pdf')

          file_size: Expected file size in bytes (max 100MB)

          filename: Original filename (e.g., 'image.jpg')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/memories/upload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "content_type": content_type,
                        "file_size": file_size,
                        "filename": filename,
                    },
                    memory_create_upload_params.MemoryCreateUploadParams,
                ),
            ),
            cast_to=MemoryCreateUploadResponse,
        )

    @overload
    def delete_many(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteManyResponse:
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
    def delete_many(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteManyResponse:
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
    def delete_many(
        self,
        *,
        body: str | SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteManyResponse:
        return cast(
            MemoryDeleteManyResponse,
            self._post(
                "/v1/memories/delete",
                body=maybe_transform(body, memory_delete_many_params.MemoryDeleteManyParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryDeleteManyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete_upload(
        self,
        *,
        s3_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteUploadResponse:
        """Delete a file from S3 that was uploaded via a presigned URL.

        Verifies the caller
        owns the file via S3 object metadata.

        Args:
          s3_key: S3 key of the file to delete (returned by POST /memories/upload)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/memories/upload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"s3_key": s3_key}, memory_delete_upload_params.MemoryDeleteUploadParams),
            ),
            cast_to=MemoryDeleteUploadResponse,
        )

    def search(
        self,
        *,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        effort: Optional[Literal["auto", "low", "medium", "high"]] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        nql: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        search_settings: Optional[memory_search_params.SearchSettings] | Omit = omit,
        snapshot: Optional[memory_search_params.Snapshot] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Perform a search query across your memories.

        **Standard mode** (collection_ids or readable-scope search): returns
        hierarchical MemoryRecall with semantics, episodes, procedures, and sources.

        **Snapshot mode** (snapshot field): returns graph-search results with {entities,
        relationships} from stateless in-memory traversal.

        Args:
          collection_ids: Optional list of collection UUIDs or names to scope the search.

          effort: Compute effort budget for memory search.

              Effort controls traversal compute (exploration budgets, depth, fanout), not the
              size of the returned MemoryRecall projection.

          filters: Optional filters to apply to the search.

          nql: Pre-written NQL script. Executes directly without planner compilation. Mutually
              exclusive with `query`.

          query: Natural-language search query. Mutually exclusive with `nql`.

          search_settings: Advanced search settings for fine-tuning search behavior.

              Note: Core parameters (query, collection_ids, filters) are now top-level API
              parameters. This class contains advanced tuning options plus internal fields
              used by the retrieval service.

              Memory search uses `effort` (auto/low/medium/high) to control compute.

          snapshot: Portable full snapshot owned by the client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            MemorySearchResponse,
            self._post(
                "/v1/memories/search",
                body=maybe_transform(
                    {
                        "collection_ids": collection_ids,
                        "effort": effort,
                        "filters": filters,
                        "nql": nql,
                        "query": query,
                        "search_settings": search_settings,
                        "snapshot": snapshot,
                    },
                    memory_search_params.MemorySearchParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemorySearchResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncMemoriesResource(AsyncAPIResource):
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
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        collection_id: Optional[str] | Omit = omit,
        content_parts: Optional[Iterable[memory_create_params.ContentPart]] | Omit = omit,
        contents: Optional[SequenceNotStr[str]] | Omit = omit,
        engram_type: Literal["document", "conversation"] | Omit = omit,
        ingestion_config: Optional[memory_create_params.IngestionConfig] | Omit = omit,
        ingestion_mode: Optional[Literal["hi-res", "ocr", "fast", "custom"]] | Omit = omit,
        messages: Optional[Iterable[memory_create_params.Message]] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        raw_text: Optional[str] | Omit = omit,
        snapshot: Optional[memory_create_params.Snapshot] | Omit = omit,
        speaker_id: Optional[str] | Omit = omit,
        speaker_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateResponse:
        """
        Create a new memory (conversation or document) using clean JSON body.

        - Use `collection_id` (UUID)
        - `engram_type` is optional and inferred from payload shape:
          - If `messages` present -> conversation
          - Otherwise -> document
        - For conversations: provide `messages` array
        - For documents: provide `raw_text` or `chunks`
        - Use `snapshot` for device-memory mode (mutually exclusive with collection_id)

        Args:
          chunks: Pre-chunked text for document type

          collection_id: Collection UUID (mutually exclusive with snapshot)

          content_parts: Multimodal content parts (text, images, audio, documents) for document type.

          contents: Batch content strings for snapshot mode

          engram_type: Type of memory to create

          ingestion_config: Public ingestion config accepted by memory-ingestion endpoints.

              This mirrors the supported request payload shape while staying independent from
              the runtime provider config, which also carries internal-only fields such as
              `app` and `extra_fields`.

          ingestion_mode: Ingestion mode for documents

          messages: Messages for conversation type

          metadata: Metadata for the memory

          name: Optional name for the memory

          raw_text: Raw text content for document type

          snapshot: Portable full snapshot owned by the client.

          speaker_id: UUID of the SourceRole entity creating this memory

          speaker_name: Display name of the speaker/agent creating this memory

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            MemoryCreateResponse,
            await self._post(
                "/v1/memories",
                body=await async_maybe_transform(
                    {
                        "chunks": chunks,
                        "collection_id": collection_id,
                        "content_parts": content_parts,
                        "contents": contents,
                        "engram_type": engram_type,
                        "ingestion_config": ingestion_config,
                        "ingestion_mode": ingestion_mode,
                        "messages": messages,
                        "metadata": metadata,
                        "name": name,
                        "raw_text": raw_text,
                        "snapshot": snapshot,
                        "speaker_id": speaker_id,
                        "speaker_name": speaker_name,
                    },
                    memory_create_params.MemoryCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> MemoryRetrieveResponse:
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
            cast_to=MemoryRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        collection_id: Optional[str] | Omit = omit,
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
    ) -> MemoryUpdateResponse:
        """
        Update memory-level properties including name, metadata, and collection
        associations.

        This endpoint allows updating properties of an entire memory (document or
        conversation) without modifying its content:

        - **name**: Updates the authoritative engram title
        - **metadata**: Can replace or merge with existing metadata
        - **collection_ids**: Updates authoritative engram collection associations

        Users can only update memories they own or have access to through collections.
        At least one collection association must be maintained.

        If collection_id is provided and the engram is shared across collections, a
        copy-on-write will be performed to create a collection-specific copy before
        modification.

        Args:
          id: The unique identifier of the memory

          collection_id: Collection context for copy-on-write. If provided and engram is shared, creates
              a copy before modification.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"collection_id": collection_id}, memory_update_params.MemoryUpdateParams
                ),
            ),
            cast_to=MemoryUpdateResponse,
        )

    async def list(
        self,
        *,
        chunks_limit: Optional[int] | Omit = omit,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
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
    ) -> MemoryListResponse:
        """
        Returns a paginated list of engrams the authenticated user has access to.

        Results can be filtered by providing specific engram IDs or collection IDs.
        Regular users will only see engrams they own or have access to through
        collections. Superusers can see all engrams.

        The engrams are returned in order of last modification, with most recent first.
        The response includes the engram's text field if available.

        Args:
          chunks_limit: Maximum chunks to inline per engram. Defaults to all chunks for backwards
              compatibility; pass 0 to skip chunk hydration.

          collection_ids: Optional list of collection IDs to filter engrams by. If provided, exactly one
              collection ID must be specified.

          ids: A list of engram IDs to retrieve. If not provided, all engrams will be returned.

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
                        "chunks_limit": chunks_limit,
                        "collection_ids": collection_ids,
                        "ids": ids,
                        "limit": limit,
                        "metadata_filters": metadata_filters,
                        "offset": offset,
                        "owner_only": owner_only,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            cast_to=MemoryListResponse,
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
    ) -> MemoryDeleteResponse:
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
            cast_to=MemoryDeleteResponse,
        )

    async def append(
        self,
        id: str,
        *,
        collection_id: str,
        chunks: Optional[SequenceNotStr[str]] | Omit = omit,
        ingestion_config: Optional[memory_append_params.IngestionConfig] | Omit = omit,
        ingestion_mode: Literal["hi-res", "ocr", "fast", "custom"] | Omit = omit,
        messages: Optional[Iterable[memory_append_params.Message]] | Omit = omit,
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

          chunks: Pre-processed text chunks to append for document memories.

          ingestion_config: Public ingestion config accepted by memory-ingestion endpoints.

              This mirrors the supported request payload shape while staying independent from
              the runtime provider config, which also carries internal-only fields such as
              `app` and `extra_fields`.

          ingestion_mode: Ingestion mode for document content.

          messages: Messages to append for conversation memories. Each message has content, role,
              and optional metadata.

          metadata: Additional metadata for the appended content.

          raw_text: Raw text content to append for document memories.

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

    async def create_upload(
        self,
        *,
        content_type: str,
        file_size: int,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateUploadResponse:
        """
        Get a presigned URL for uploading large files directly to S3.

        Use this for files larger than 5MB that cannot be sent inline as base64. After
        uploading, reference the file in memory creation using S3FileReference.

        Args: filename: Original filename (e.g., "image.jpg") content_type: MIME type
        (e.g., "image/jpeg", "application/pdf") file_size: Expected file size in bytes
        (max 100MB)

        Returns: dict with: - upload_url: Presigned URL for PUT request (expires in 1
        hour) - upload_headers: Headers that must be sent with the presigned PUT
        request - s3_key: The S3 key to reference in memory creation - bucket: S3 bucket
        name - expires_in: Seconds until URL expires - max_size: Maximum allowed file
        size

        Args:
          content_type: MIME type (e.g., 'image/jpeg', 'application/pdf')

          file_size: Expected file size in bytes (max 100MB)

          filename: Original filename (e.g., 'image.jpg')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/memories/upload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "content_type": content_type,
                        "file_size": file_size,
                        "filename": filename,
                    },
                    memory_create_upload_params.MemoryCreateUploadParams,
                ),
            ),
            cast_to=MemoryCreateUploadResponse,
        )

    @overload
    async def delete_many(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteManyResponse:
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
    async def delete_many(
        self,
        *,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteManyResponse:
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
    async def delete_many(
        self,
        *,
        body: str | SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteManyResponse:
        return cast(
            MemoryDeleteManyResponse,
            await self._post(
                "/v1/memories/delete",
                body=await async_maybe_transform(body, memory_delete_many_params.MemoryDeleteManyParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemoryDeleteManyResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete_upload(
        self,
        *,
        s3_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteUploadResponse:
        """Delete a file from S3 that was uploaded via a presigned URL.

        Verifies the caller
        owns the file via S3 object metadata.

        Args:
          s3_key: S3 key of the file to delete (returned by POST /memories/upload)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/memories/upload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"s3_key": s3_key}, memory_delete_upload_params.MemoryDeleteUploadParams
                ),
            ),
            cast_to=MemoryDeleteUploadResponse,
        )

    async def search(
        self,
        *,
        collection_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        effort: Optional[Literal["auto", "low", "medium", "high"]] | Omit = omit,
        filters: Optional[Dict[str, object]] | Omit = omit,
        nql: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        search_settings: Optional[memory_search_params.SearchSettings] | Omit = omit,
        snapshot: Optional[memory_search_params.Snapshot] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Perform a search query across your memories.

        **Standard mode** (collection_ids or readable-scope search): returns
        hierarchical MemoryRecall with semantics, episodes, procedures, and sources.

        **Snapshot mode** (snapshot field): returns graph-search results with {entities,
        relationships} from stateless in-memory traversal.

        Args:
          collection_ids: Optional list of collection UUIDs or names to scope the search.

          effort: Compute effort budget for memory search.

              Effort controls traversal compute (exploration budgets, depth, fanout), not the
              size of the returned MemoryRecall projection.

          filters: Optional filters to apply to the search.

          nql: Pre-written NQL script. Executes directly without planner compilation. Mutually
              exclusive with `query`.

          query: Natural-language search query. Mutually exclusive with `nql`.

          search_settings: Advanced search settings for fine-tuning search behavior.

              Note: Core parameters (query, collection_ids, filters) are now top-level API
              parameters. This class contains advanced tuning options plus internal fields
              used by the retrieval service.

              Memory search uses `effort` (auto/low/medium/high) to control compute.

          snapshot: Portable full snapshot owned by the client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            MemorySearchResponse,
            await self._post(
                "/v1/memories/search",
                body=await async_maybe_transform(
                    {
                        "collection_ids": collection_ids,
                        "effort": effort,
                        "filters": filters,
                        "nql": nql,
                        "query": query,
                        "search_settings": search_settings,
                        "snapshot": snapshot,
                    },
                    memory_search_params.MemorySearchParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, MemorySearchResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        self.create_upload = to_raw_response_wrapper(
            memories.create_upload,
        )
        self.delete_many = to_raw_response_wrapper(
            memories.delete_many,
        )
        self.delete_upload = to_raw_response_wrapper(
            memories.delete_upload,
        )
        self.search = to_raw_response_wrapper(
            memories.search,
        )


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
        self.create_upload = async_to_raw_response_wrapper(
            memories.create_upload,
        )
        self.delete_many = async_to_raw_response_wrapper(
            memories.delete_many,
        )
        self.delete_upload = async_to_raw_response_wrapper(
            memories.delete_upload,
        )
        self.search = async_to_raw_response_wrapper(
            memories.search,
        )


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
        self.create_upload = to_streamed_response_wrapper(
            memories.create_upload,
        )
        self.delete_many = to_streamed_response_wrapper(
            memories.delete_many,
        )
        self.delete_upload = to_streamed_response_wrapper(
            memories.delete_upload,
        )
        self.search = to_streamed_response_wrapper(
            memories.search,
        )


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
        self.create_upload = async_to_streamed_response_wrapper(
            memories.create_upload,
        )
        self.delete_many = async_to_streamed_response_wrapper(
            memories.delete_many,
        )
        self.delete_upload = async_to_streamed_response_wrapper(
            memories.delete_upload,
        )
        self.search = async_to_streamed_response_wrapper(
            memories.search,
        )
