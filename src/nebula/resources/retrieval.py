# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    SearchMode,
    retrieval_search_params,
    retrieval_engage_agent_params,
    retrieval_execute_rag_query_params,
    retrieval_generate_embeddings_params,
    retrieval_generate_completions_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_mode import SearchMode
from ..types.message_param import MessageParam
from ..types.search_settings_param import SearchSettingsParam
from ..types.generation_config_param import GenerationConfigParam
from ..types.retrieval_search_response import RetrievalSearchResponse
from ..types.retrieval_engage_agent_response import RetrievalEngageAgentResponse
from ..types.retrieval_generate_embeddings_response import RetrievalGenerateEmbeddingsResponse
from ..types.retrieval_generate_completions_response import RetrievalGenerateCompletionsResponse

__all__ = ["RetrievalResource", "AsyncRetrievalResource"]


class RetrievalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return RetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return RetrievalResourceWithStreamingResponse(self)

    def engage_agent(
        self,
        *,
        conversation_id: Optional[str] | Omit = omit,
        include_title_if_available: bool | Omit = omit,
        max_tool_context_length: Optional[int] | Omit = omit,
        message: Optional[MessageParam] | Omit = omit,
        messages: Optional[Iterable[MessageParam]] | Omit = omit,
        mode: Optional[Literal["rag", "research"]] | Omit = omit,
        needs_initial_conversation_name: Optional[bool] | Omit = omit,
        rag_generation_config: GenerationConfigParam | Omit = omit,
        rag_tools: Optional[
            List[
                Literal[
                    "web_search", "web_scrape", "search_file_descriptions", "search_file_knowledge", "get_file_content"
                ]
            ]
        ]
        | Omit = omit,
        research_generation_config: Optional[GenerationConfigParam] | Omit = omit,
        research_tools: Optional[List[Literal["rag", "reasoning", "critique", "python_executor"]]] | Omit = omit,
        search_mode: SearchMode | Omit = omit,
        search_settings: Optional[SearchSettingsParam] | Omit = omit,
        task_prompt: Optional[str] | Omit = omit,
        use_system_context: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalEngageAgentResponse:
        """
        Engage with an intelligent agent for information retrieval, analysis, and
        research.

        This endpoint offers two operating modes:

        - **RAG mode**: Standard retrieval-augmented generation for answering questions
          based on knowledge base
        - **Research mode**: Advanced capabilities for deep analysis, reasoning, and
          computation

        ### RAG Mode (Default)

        The RAG mode provides fast, knowledge-based responses using:

        - Semantic and hybrid search capabilities
        - Engram-level and chunk-level content retrieval
        - Optional web search integration
        - Source citation and evidence-based responses

        ### Research Mode

        The Research mode builds on RAG capabilities and adds:

        - A dedicated reasoning system for complex problem-solving
        - Critique capabilities to identify potential biases or logical fallacies
        - Python execution for computational analysis
        - Multi-step reasoning for deeper exploration of topics

        ### Available Tools

        **RAG Tools:**

        - `search_file_knowledge`: Semantic/hybrid search on your ingested engrams
        - `search_file_descriptions`: Search over file-level metadata
        - `content`: Fetch entire engrams or chunk structures
        - `web_search`: Query external search APIs for up-to-date information
        - `web_scrape`: Scrape and extract content from specific web pages

        **Research Tools:**

        - `rag`: Leverage the underlying RAG agent for information retrieval
        - `reasoning`: Call a dedicated model for complex analytical thinking
        - `critique`: Analyze conversation history to identify flaws and biases
        - `python_executor`: Execute Python code for complex calculations and analysis

        ### Streaming Output

        When streaming is enabled, the agent produces different event types:

        - `thinking`: Shows the model's step-by-step reasoning (when
          extended_thinking=true)
        - `tool_call`: Shows when the agent invokes a tool
        - `tool_result`: Shows the result of a tool call
        - `citation`: Indicates when a citation is added to the response
        - `message`: Streams partial tokens of the response
        - `final_answer`: Contains the complete generated answer and structured
          citations

        ### Conversations

        Maintain context across multiple turns by including `conversation_id` in each
        request. After your first call, store the returned `conversation_id` and include
        it in subsequent calls. If no conversation name has already been set for the
        conversation, the system will automatically assign one.

        Args:
          conversation_id: ID of the conversation

          include_title_if_available: Pass engram titles from search results into the LLM context window.

          max_tool_context_length: Maximum length of returned tool context

          message: Current message to process

          messages: List of messages (deprecated, use message instead)

          mode: Mode to use for generation: 'rag' for standard retrieval or 'research' for deep
              analysis with reasoning capabilities

          needs_initial_conversation_name: If true, the system will automatically assign a conversation name if not already
              specified previously.

          rag_generation_config: Configuration for RAG generation in 'rag' mode

          rag_tools: List of tools to enable for RAG mode. Available tools: search_file_knowledge,
              get_file_content, web_search, web_scrape, search_file_descriptions

          research_generation_config: Configuration for generation in 'research' mode. If not provided but
              mode='research', rag_generation_config will be used with appropriate model
              overrides.

          research_tools: List of tools to enable for Research mode. Available tools: rag, reasoning,
              critique, python_executor

          search_mode: Graph search algorithm: 'fast' (simple BFS) or 'super' (SuperBFS with
              contextualization, default).

          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          task_prompt: Optional custom prompt to override default

          use_system_context: Use extended prompt for generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/retrieval/agent",
            body=maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "include_title_if_available": include_title_if_available,
                    "max_tool_context_length": max_tool_context_length,
                    "message": message,
                    "messages": messages,
                    "mode": mode,
                    "needs_initial_conversation_name": needs_initial_conversation_name,
                    "rag_generation_config": rag_generation_config,
                    "rag_tools": rag_tools,
                    "research_generation_config": research_generation_config,
                    "research_tools": research_tools,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                    "task_prompt": task_prompt,
                    "use_system_context": use_system_context,
                },
                retrieval_engage_agent_params.RetrievalEngageAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalEngageAgentResponse,
        )

    def execute_rag_query(
        self,
        *,
        query: str,
        include_title_if_available: bool | Omit = omit,
        include_web_search: bool | Omit = omit,
        rag_generation_config: GenerationConfigParam | Omit = omit,
        search_mode: SearchMode | Omit = omit,
        search_settings: Optional[SearchSettingsParam] | Omit = omit,
        task_prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Execute a RAG (Retrieval-Augmented Generation) query.

        This endpoint combines search results with language model generation to produce
        accurate, contextually-relevant responses based on your engram corpus.

        **Features:**

        - Combines vector search, optional knowledge graph integration, and LLM
          generation
        - Automatically cites sources with unique citation identifiers
        - Supports both streaming and non-streaming responses
        - Compatible with various LLM providers (OpenAI, Anthropic, etc.)
        - Web search integration for up-to-date information

        **Search Configuration:** All search parameters from the search endpoint apply
        here, including filters, hybrid search, and graph-enhanced search.

        **Generation Configuration:** Fine-tune the language model's behavior with
        `rag_generation_config`:

        ```json
        {
          "model": "openai/gpt-4.1-mini", // Model to use
          "temperature": 0.7, // Control randomness (0-1)
          "max_tokens": 1500, // Maximum output length
          "stream": true // Enable token streaming
        }
        ```

        **Model Support:**

        - OpenAI models (default)
        - Anthropic Claude models (requires ANTHROPIC_API_KEY)
        - Local models via Ollama
        - Any provider supported by LiteLLM

        **Streaming Responses:** When `stream: true` is set, the endpoint returns
        Server-Sent Events with the following types:

        - `search_results`: Initial search results from your engrams
        - `message`: Partial tokens as they're generated
        - `citation`: Citation metadata when sources are referenced
        - `final_answer`: Complete answer with structured citations

        **Example Response:**

        ```json
        {
        "generated_answer": "DeepSeek-R1 is a model that demonstrates impressive performance...[1]",
        "search_results": { ... },
        "citations": [
            {
                "id": "cit.123456",
                "object": "citation",
                "payload": { ... }
            }
        ]
        }
        ```

        Args:
          include_title_if_available: Include engram titles in responses when available

          include_web_search: Include web search results provided to the LLM.

          rag_generation_config: Configuration for RAG generation

          search_mode:
              Graph search algorithm selection:

              `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
              with set transformers (max_depth=3, contextualized scoring, default)

              All modes now use depth=3 for optimal speed + relevance balance. All search
              settings can be controlled via `search_settings` regardless of mode.

          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          task_prompt: Optional custom prompt to override default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/retrieval/rag",
            body=maybe_transform(
                {
                    "query": query,
                    "include_title_if_available": include_title_if_available,
                    "include_web_search": include_web_search,
                    "rag_generation_config": rag_generation_config,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                    "task_prompt": task_prompt,
                },
                retrieval_execute_rag_query_params.RetrievalExecuteRagQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def generate_completions(
        self,
        *,
        messages: Iterable[MessageParam],
        response_model: object | Omit = omit,
        generation_config: GenerationConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalGenerateCompletionsResponse:
        """
        Generate completions for a list of messages.

        This endpoint uses the language model to generate completions for the provided
        messages. The generation process can be customized using the generation_config
        parameter.

        The messages list should contain alternating user and assistant messages, with
        an optional system message at the start. Each message should have a 'role' and
        'content'.

        Args:
          messages: List of messages to generate completion for

          generation_config: Configuration for text generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/retrieval/completion",
            body=maybe_transform(
                {
                    "messages": messages,
                    "generation_config": generation_config,
                },
                retrieval_generate_completions_params.RetrievalGenerateCompletionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"response_model": response_model},
                    retrieval_generate_completions_params.RetrievalGenerateCompletionsParams,
                ),
            ),
            cast_to=RetrievalGenerateCompletionsResponse,
        )

    def generate_embeddings(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalGenerateEmbeddingsResponse:
        """
        Generate embeddings for the provided text using the specified model.

        This endpoint uses the language model to generate embeddings for the provided
        text. The model parameter specifies the model to use for generating embeddings.

        Args:
          body: Text to generate embeddings for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/retrieval/embedding",
            body=maybe_transform(body, retrieval_generate_embeddings_params.RetrievalGenerateEmbeddingsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalGenerateEmbeddingsResponse,
        )

    def search(
        self,
        *,
        query: str,
        search_mode: SearchMode | Omit = omit,
        search_settings: Optional[SearchSettingsParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalSearchResponse:
        """
        Perform a search query against vector and/or graph-based databases.

        **Search Modes:**

        - `basic`: Smaller type limits for faster searches.
        - `advanced`: Larger type limits for comprehensive results.
        - `custom`: Complete control over search settings. Always uses hybrid search.

        **Hybrid Search (Always Enabled):** All searches use hybrid mode combining
        semantic and full-text search. Control the balance with weights:

        ```json
        {
          "semantic_weight": 5.0, // Weight for semantic search (default: 5.0)
          "fulltext_weight": 1.0 // Weight for full-text search (default: 1.0)
        }
        ```

        Set `semantic_weight: 0` for pure full-text search, or `fulltext_weight: 0` for
        pure semantic search.

        **Filters:** Apply filters directly inside `search_settings.filters`. For
        example:

        ```json
        {
          "filters": { "engram_id": { "$eq": "e43864f5-a36f-548e-aacd-6f8d48b30c7f" } }
        }
        ```

        Supported operators: `$eq`, `$neq`, `$gt`, `$gte`, `$lt`, `$lte`, `$like`,
        `$ilike`, `$in`, `$nin`.

        **Result Limits:** Control the total number of results returned:

        ```json
        {
          "limit": 20
        }
        ```

        **Graph-Enhanced Search:** Knowledge graph integration is enabled automatically
        and managed internally for optimal performance.

        **Advanced Filtering:** Use complex filters to narrow down results by metadata
        fields or engram properties:

        ```json
        {
          "filters": {
            "$and": [
              { "engram_type": { "$eq": "pdf" } },
              { "metadata.year": { "$gt": 2020 } }
            ]
          }
        }
        ```

        **Results:** The response includes vector search results and optional graph
        search results. Each result contains the matched text, engram ID, and relevance
        score.

        Args:
          query: Search query to find relevant engrams

          search_mode:
              Graph search algorithm selection:

              `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
              with set transformers (max_depth=3, contextualized scoring, default)

              All modes now use depth=3 for optimal speed + relevance balance. All search
              settings can be controlled via `search_settings` regardless of mode.

          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/retrieval/search",
            body=maybe_transform(
                {
                    "query": query,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                },
                retrieval_search_params.RetrievalSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalSearchResponse,
        )


class AsyncRetrievalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/nebula-agi/nebula-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/nebula-agi/nebula-python#with_streaming_response
        """
        return AsyncRetrievalResourceWithStreamingResponse(self)

    async def engage_agent(
        self,
        *,
        conversation_id: Optional[str] | Omit = omit,
        include_title_if_available: bool | Omit = omit,
        max_tool_context_length: Optional[int] | Omit = omit,
        message: Optional[MessageParam] | Omit = omit,
        messages: Optional[Iterable[MessageParam]] | Omit = omit,
        mode: Optional[Literal["rag", "research"]] | Omit = omit,
        needs_initial_conversation_name: Optional[bool] | Omit = omit,
        rag_generation_config: GenerationConfigParam | Omit = omit,
        rag_tools: Optional[
            List[
                Literal[
                    "web_search", "web_scrape", "search_file_descriptions", "search_file_knowledge", "get_file_content"
                ]
            ]
        ]
        | Omit = omit,
        research_generation_config: Optional[GenerationConfigParam] | Omit = omit,
        research_tools: Optional[List[Literal["rag", "reasoning", "critique", "python_executor"]]] | Omit = omit,
        search_mode: SearchMode | Omit = omit,
        search_settings: Optional[SearchSettingsParam] | Omit = omit,
        task_prompt: Optional[str] | Omit = omit,
        use_system_context: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalEngageAgentResponse:
        """
        Engage with an intelligent agent for information retrieval, analysis, and
        research.

        This endpoint offers two operating modes:

        - **RAG mode**: Standard retrieval-augmented generation for answering questions
          based on knowledge base
        - **Research mode**: Advanced capabilities for deep analysis, reasoning, and
          computation

        ### RAG Mode (Default)

        The RAG mode provides fast, knowledge-based responses using:

        - Semantic and hybrid search capabilities
        - Engram-level and chunk-level content retrieval
        - Optional web search integration
        - Source citation and evidence-based responses

        ### Research Mode

        The Research mode builds on RAG capabilities and adds:

        - A dedicated reasoning system for complex problem-solving
        - Critique capabilities to identify potential biases or logical fallacies
        - Python execution for computational analysis
        - Multi-step reasoning for deeper exploration of topics

        ### Available Tools

        **RAG Tools:**

        - `search_file_knowledge`: Semantic/hybrid search on your ingested engrams
        - `search_file_descriptions`: Search over file-level metadata
        - `content`: Fetch entire engrams or chunk structures
        - `web_search`: Query external search APIs for up-to-date information
        - `web_scrape`: Scrape and extract content from specific web pages

        **Research Tools:**

        - `rag`: Leverage the underlying RAG agent for information retrieval
        - `reasoning`: Call a dedicated model for complex analytical thinking
        - `critique`: Analyze conversation history to identify flaws and biases
        - `python_executor`: Execute Python code for complex calculations and analysis

        ### Streaming Output

        When streaming is enabled, the agent produces different event types:

        - `thinking`: Shows the model's step-by-step reasoning (when
          extended_thinking=true)
        - `tool_call`: Shows when the agent invokes a tool
        - `tool_result`: Shows the result of a tool call
        - `citation`: Indicates when a citation is added to the response
        - `message`: Streams partial tokens of the response
        - `final_answer`: Contains the complete generated answer and structured
          citations

        ### Conversations

        Maintain context across multiple turns by including `conversation_id` in each
        request. After your first call, store the returned `conversation_id` and include
        it in subsequent calls. If no conversation name has already been set for the
        conversation, the system will automatically assign one.

        Args:
          conversation_id: ID of the conversation

          include_title_if_available: Pass engram titles from search results into the LLM context window.

          max_tool_context_length: Maximum length of returned tool context

          message: Current message to process

          messages: List of messages (deprecated, use message instead)

          mode: Mode to use for generation: 'rag' for standard retrieval or 'research' for deep
              analysis with reasoning capabilities

          needs_initial_conversation_name: If true, the system will automatically assign a conversation name if not already
              specified previously.

          rag_generation_config: Configuration for RAG generation in 'rag' mode

          rag_tools: List of tools to enable for RAG mode. Available tools: search_file_knowledge,
              get_file_content, web_search, web_scrape, search_file_descriptions

          research_generation_config: Configuration for generation in 'research' mode. If not provided but
              mode='research', rag_generation_config will be used with appropriate model
              overrides.

          research_tools: List of tools to enable for Research mode. Available tools: rag, reasoning,
              critique, python_executor

          search_mode: Graph search algorithm: 'fast' (simple BFS) or 'super' (SuperBFS with
              contextualization, default).

          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          task_prompt: Optional custom prompt to override default

          use_system_context: Use extended prompt for generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/retrieval/agent",
            body=await async_maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "include_title_if_available": include_title_if_available,
                    "max_tool_context_length": max_tool_context_length,
                    "message": message,
                    "messages": messages,
                    "mode": mode,
                    "needs_initial_conversation_name": needs_initial_conversation_name,
                    "rag_generation_config": rag_generation_config,
                    "rag_tools": rag_tools,
                    "research_generation_config": research_generation_config,
                    "research_tools": research_tools,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                    "task_prompt": task_prompt,
                    "use_system_context": use_system_context,
                },
                retrieval_engage_agent_params.RetrievalEngageAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalEngageAgentResponse,
        )

    async def execute_rag_query(
        self,
        *,
        query: str,
        include_title_if_available: bool | Omit = omit,
        include_web_search: bool | Omit = omit,
        rag_generation_config: GenerationConfigParam | Omit = omit,
        search_mode: SearchMode | Omit = omit,
        search_settings: Optional[SearchSettingsParam] | Omit = omit,
        task_prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Execute a RAG (Retrieval-Augmented Generation) query.

        This endpoint combines search results with language model generation to produce
        accurate, contextually-relevant responses based on your engram corpus.

        **Features:**

        - Combines vector search, optional knowledge graph integration, and LLM
          generation
        - Automatically cites sources with unique citation identifiers
        - Supports both streaming and non-streaming responses
        - Compatible with various LLM providers (OpenAI, Anthropic, etc.)
        - Web search integration for up-to-date information

        **Search Configuration:** All search parameters from the search endpoint apply
        here, including filters, hybrid search, and graph-enhanced search.

        **Generation Configuration:** Fine-tune the language model's behavior with
        `rag_generation_config`:

        ```json
        {
          "model": "openai/gpt-4.1-mini", // Model to use
          "temperature": 0.7, // Control randomness (0-1)
          "max_tokens": 1500, // Maximum output length
          "stream": true // Enable token streaming
        }
        ```

        **Model Support:**

        - OpenAI models (default)
        - Anthropic Claude models (requires ANTHROPIC_API_KEY)
        - Local models via Ollama
        - Any provider supported by LiteLLM

        **Streaming Responses:** When `stream: true` is set, the endpoint returns
        Server-Sent Events with the following types:

        - `search_results`: Initial search results from your engrams
        - `message`: Partial tokens as they're generated
        - `citation`: Citation metadata when sources are referenced
        - `final_answer`: Complete answer with structured citations

        **Example Response:**

        ```json
        {
        "generated_answer": "DeepSeek-R1 is a model that demonstrates impressive performance...[1]",
        "search_results": { ... },
        "citations": [
            {
                "id": "cit.123456",
                "object": "citation",
                "payload": { ... }
            }
        ]
        }
        ```

        Args:
          include_title_if_available: Include engram titles in responses when available

          include_web_search: Include web search results provided to the LLM.

          rag_generation_config: Configuration for RAG generation

          search_mode:
              Graph search algorithm selection:

              `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
              with set transformers (max_depth=3, contextualized scoring, default)

              All modes now use depth=3 for optimal speed + relevance balance. All search
              settings can be controlled via `search_settings` regardless of mode.

          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          task_prompt: Optional custom prompt to override default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/retrieval/rag",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "include_title_if_available": include_title_if_available,
                    "include_web_search": include_web_search,
                    "rag_generation_config": rag_generation_config,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                    "task_prompt": task_prompt,
                },
                retrieval_execute_rag_query_params.RetrievalExecuteRagQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def generate_completions(
        self,
        *,
        messages: Iterable[MessageParam],
        response_model: object | Omit = omit,
        generation_config: GenerationConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalGenerateCompletionsResponse:
        """
        Generate completions for a list of messages.

        This endpoint uses the language model to generate completions for the provided
        messages. The generation process can be customized using the generation_config
        parameter.

        The messages list should contain alternating user and assistant messages, with
        an optional system message at the start. Each message should have a 'role' and
        'content'.

        Args:
          messages: List of messages to generate completion for

          generation_config: Configuration for text generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/retrieval/completion",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "generation_config": generation_config,
                },
                retrieval_generate_completions_params.RetrievalGenerateCompletionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"response_model": response_model},
                    retrieval_generate_completions_params.RetrievalGenerateCompletionsParams,
                ),
            ),
            cast_to=RetrievalGenerateCompletionsResponse,
        )

    async def generate_embeddings(
        self,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalGenerateEmbeddingsResponse:
        """
        Generate embeddings for the provided text using the specified model.

        This endpoint uses the language model to generate embeddings for the provided
        text. The model parameter specifies the model to use for generating embeddings.

        Args:
          body: Text to generate embeddings for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/retrieval/embedding",
            body=await async_maybe_transform(
                body, retrieval_generate_embeddings_params.RetrievalGenerateEmbeddingsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalGenerateEmbeddingsResponse,
        )

    async def search(
        self,
        *,
        query: str,
        search_mode: SearchMode | Omit = omit,
        search_settings: Optional[SearchSettingsParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalSearchResponse:
        """
        Perform a search query against vector and/or graph-based databases.

        **Search Modes:**

        - `basic`: Smaller type limits for faster searches.
        - `advanced`: Larger type limits for comprehensive results.
        - `custom`: Complete control over search settings. Always uses hybrid search.

        **Hybrid Search (Always Enabled):** All searches use hybrid mode combining
        semantic and full-text search. Control the balance with weights:

        ```json
        {
          "semantic_weight": 5.0, // Weight for semantic search (default: 5.0)
          "fulltext_weight": 1.0 // Weight for full-text search (default: 1.0)
        }
        ```

        Set `semantic_weight: 0` for pure full-text search, or `fulltext_weight: 0` for
        pure semantic search.

        **Filters:** Apply filters directly inside `search_settings.filters`. For
        example:

        ```json
        {
          "filters": { "engram_id": { "$eq": "e43864f5-a36f-548e-aacd-6f8d48b30c7f" } }
        }
        ```

        Supported operators: `$eq`, `$neq`, `$gt`, `$gte`, `$lt`, `$lte`, `$like`,
        `$ilike`, `$in`, `$nin`.

        **Result Limits:** Control the total number of results returned:

        ```json
        {
          "limit": 20
        }
        ```

        **Graph-Enhanced Search:** Knowledge graph integration is enabled automatically
        and managed internally for optimal performance.

        **Advanced Filtering:** Use complex filters to narrow down results by metadata
        fields or engram properties:

        ```json
        {
          "filters": {
            "$and": [
              { "engram_type": { "$eq": "pdf" } },
              { "metadata.year": { "$gt": 2020 } }
            ]
          }
        }
        ```

        **Results:** The response includes vector search results and optional graph
        search results. Each result contains the matched text, engram ID, and relevance
        score.

        Args:
          query: Search query to find relevant engrams

          search_mode:
              Graph search algorithm selection:

              `fast`: Fast BFS graph traversal (max_depth=3, simple scoring) `super`: SuperBFS
              with set transformers (max_depth=3, contextualized scoring, default)

              All modes now use depth=3 for optimal speed + relevance balance. All search
              settings can be controlled via `search_settings` regardless of mode.

          search_settings: Simplified search settings with automatic hybrid search and type-specific
              limits.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/retrieval/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "search_mode": search_mode,
                    "search_settings": search_settings,
                },
                retrieval_search_params.RetrievalSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrievalSearchResponse,
        )


class RetrievalResourceWithRawResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.engage_agent = to_raw_response_wrapper(
            retrieval.engage_agent,
        )
        self.execute_rag_query = to_raw_response_wrapper(
            retrieval.execute_rag_query,
        )
        self.generate_completions = to_raw_response_wrapper(
            retrieval.generate_completions,
        )
        self.generate_embeddings = to_raw_response_wrapper(
            retrieval.generate_embeddings,
        )
        self.search = to_raw_response_wrapper(
            retrieval.search,
        )


class AsyncRetrievalResourceWithRawResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.engage_agent = async_to_raw_response_wrapper(
            retrieval.engage_agent,
        )
        self.execute_rag_query = async_to_raw_response_wrapper(
            retrieval.execute_rag_query,
        )
        self.generate_completions = async_to_raw_response_wrapper(
            retrieval.generate_completions,
        )
        self.generate_embeddings = async_to_raw_response_wrapper(
            retrieval.generate_embeddings,
        )
        self.search = async_to_raw_response_wrapper(
            retrieval.search,
        )


class RetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.engage_agent = to_streamed_response_wrapper(
            retrieval.engage_agent,
        )
        self.execute_rag_query = to_streamed_response_wrapper(
            retrieval.execute_rag_query,
        )
        self.generate_completions = to_streamed_response_wrapper(
            retrieval.generate_completions,
        )
        self.generate_embeddings = to_streamed_response_wrapper(
            retrieval.generate_embeddings,
        )
        self.search = to_streamed_response_wrapper(
            retrieval.search,
        )


class AsyncRetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.engage_agent = async_to_streamed_response_wrapper(
            retrieval.engage_agent,
        )
        self.execute_rag_query = async_to_streamed_response_wrapper(
            retrieval.execute_rag_query,
        )
        self.generate_completions = async_to_streamed_response_wrapper(
            retrieval.generate_completions,
        )
        self.generate_embeddings = async_to_streamed_response_wrapper(
            retrieval.generate_embeddings,
        )
        self.search = async_to_streamed_response_wrapper(
            retrieval.search,
        )
