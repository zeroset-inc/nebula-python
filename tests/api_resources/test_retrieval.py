# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nebula import Nebula, AsyncNebula
from tests.utils import assert_matches_type
from nebula.types import (
    RetrievalSearchResponse,
    RetrievalEngageAgentResponse,
    RetrievalGenerateEmbeddingsResponse,
    RetrievalGenerateCompletionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrieval:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_engage_agent(self, client: Nebula) -> None:
        retrieval = client.retrieval.engage_agent()
        assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_engage_agent_with_all_params(self, client: Nebula) -> None:
        retrieval = client.retrieval.engage_agent(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_title_if_available=True,
            max_tool_context_length=0,
            message={
                "role": "user",
                "content": "This is a test message.",
                "function_call": {"foo": "bar"},
                "image_data": {"foo": "string"},
                "image_url": "image_url",
                "metadata": {"foo": "bar"},
                "name": "name",
                "structured_content": [{"foo": "bar"}],
                "tool_call_id": "tool_call_id",
                "tool_calls": [{"foo": "bar"}],
            },
            messages=[
                {
                    "role": "user",
                    "content": "This is a test message.",
                    "function_call": {"foo": "bar"},
                    "image_data": {"foo": "string"},
                    "image_url": "image_url",
                    "metadata": {"foo": "bar"},
                    "name": "name",
                    "structured_content": [{"foo": "bar"}],
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [{"foo": "bar"}],
                }
            ],
            mode="rag",
            needs_initial_conversation_name=True,
            rag_generation_config={
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
            rag_tools=["web_search"],
            research_generation_config={
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
            research_tools=["rag"],
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
            task_prompt="task_prompt",
            use_system_context=True,
        )
        assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_engage_agent(self, client: Nebula) -> None:
        response = client.retrieval.with_raw_response.engage_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_engage_agent(self, client: Nebula) -> None:
        with client.retrieval.with_streaming_response.engage_agent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_rag_query(self, client: Nebula) -> None:
        retrieval = client.retrieval.execute_rag_query(
            query="query",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_rag_query_with_all_params(self, client: Nebula) -> None:
        retrieval = client.retrieval.execute_rag_query(
            query="query",
            include_title_if_available=True,
            include_web_search=True,
            rag_generation_config={
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
            task_prompt="task_prompt",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_rag_query(self, client: Nebula) -> None:
        response = client.retrieval.with_raw_response.execute_rag_query(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_rag_query(self, client: Nebula) -> None:
        with client.retrieval.with_streaming_response.execute_rag_query(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_completions(self, client: Nebula) -> None:
        retrieval = client.retrieval.generate_completions(
            messages=[{"role": "user"}],
        )
        assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_completions_with_all_params(self, client: Nebula) -> None:
        retrieval = client.retrieval.generate_completions(
            messages=[
                {
                    "role": "user",
                    "content": "This is a test message.",
                    "function_call": {"foo": "bar"},
                    "image_data": {"foo": "string"},
                    "image_url": "image_url",
                    "metadata": {"foo": "bar"},
                    "name": "name",
                    "structured_content": [{"foo": "bar"}],
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [{"foo": "bar"}],
                }
            ],
            response_model={},
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
        )
        assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_completions(self, client: Nebula) -> None:
        response = client.retrieval.with_raw_response.generate_completions(
            messages=[{"role": "user"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_completions(self, client: Nebula) -> None:
        with client.retrieval.with_streaming_response.generate_completions(
            messages=[{"role": "user"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_embeddings(self, client: Nebula) -> None:
        retrieval = client.retrieval.generate_embeddings(
            body="body",
        )
        assert_matches_type(RetrievalGenerateEmbeddingsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_embeddings(self, client: Nebula) -> None:
        response = client.retrieval.with_raw_response.generate_embeddings(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalGenerateEmbeddingsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_embeddings(self, client: Nebula) -> None:
        with client.retrieval.with_streaming_response.generate_embeddings(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalGenerateEmbeddingsResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Nebula) -> None:
        retrieval = client.retrieval.search(
            query="query",
        )
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Nebula) -> None:
        retrieval = client.retrieval.search(
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
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Nebula) -> None:
        response = client.retrieval.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Nebula) -> None:
        with client.retrieval.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetrieval:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_engage_agent(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.engage_agent()
        assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_engage_agent_with_all_params(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.engage_agent(
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_title_if_available=True,
            max_tool_context_length=0,
            message={
                "role": "user",
                "content": "This is a test message.",
                "function_call": {"foo": "bar"},
                "image_data": {"foo": "string"},
                "image_url": "image_url",
                "metadata": {"foo": "bar"},
                "name": "name",
                "structured_content": [{"foo": "bar"}],
                "tool_call_id": "tool_call_id",
                "tool_calls": [{"foo": "bar"}],
            },
            messages=[
                {
                    "role": "user",
                    "content": "This is a test message.",
                    "function_call": {"foo": "bar"},
                    "image_data": {"foo": "string"},
                    "image_url": "image_url",
                    "metadata": {"foo": "bar"},
                    "name": "name",
                    "structured_content": [{"foo": "bar"}],
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [{"foo": "bar"}],
                }
            ],
            mode="rag",
            needs_initial_conversation_name=True,
            rag_generation_config={
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
            rag_tools=["web_search"],
            research_generation_config={
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
            research_tools=["rag"],
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
            task_prompt="task_prompt",
            use_system_context=True,
        )
        assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_engage_agent(self, async_client: AsyncNebula) -> None:
        response = await async_client.retrieval.with_raw_response.engage_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_engage_agent(self, async_client: AsyncNebula) -> None:
        async with async_client.retrieval.with_streaming_response.engage_agent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalEngageAgentResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_rag_query(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.execute_rag_query(
            query="query",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_rag_query_with_all_params(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.execute_rag_query(
            query="query",
            include_title_if_available=True,
            include_web_search=True,
            rag_generation_config={
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
            task_prompt="task_prompt",
        )
        assert_matches_type(object, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_rag_query(self, async_client: AsyncNebula) -> None:
        response = await async_client.retrieval.with_raw_response.execute_rag_query(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(object, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_rag_query(self, async_client: AsyncNebula) -> None:
        async with async_client.retrieval.with_streaming_response.execute_rag_query(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(object, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_completions(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.generate_completions(
            messages=[{"role": "user"}],
        )
        assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_completions_with_all_params(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.generate_completions(
            messages=[
                {
                    "role": "user",
                    "content": "This is a test message.",
                    "function_call": {"foo": "bar"},
                    "image_data": {"foo": "string"},
                    "image_url": "image_url",
                    "metadata": {"foo": "bar"},
                    "name": "name",
                    "structured_content": [{"foo": "bar"}],
                    "tool_call_id": "tool_call_id",
                    "tool_calls": [{"foo": "bar"}],
                }
            ],
            response_model={},
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
        )
        assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_completions(self, async_client: AsyncNebula) -> None:
        response = await async_client.retrieval.with_raw_response.generate_completions(
            messages=[{"role": "user"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_completions(self, async_client: AsyncNebula) -> None:
        async with async_client.retrieval.with_streaming_response.generate_completions(
            messages=[{"role": "user"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalGenerateCompletionsResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_embeddings(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.generate_embeddings(
            body="body",
        )
        assert_matches_type(RetrievalGenerateEmbeddingsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_embeddings(self, async_client: AsyncNebula) -> None:
        response = await async_client.retrieval.with_raw_response.generate_embeddings(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalGenerateEmbeddingsResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_embeddings(self, async_client: AsyncNebula) -> None:
        async with async_client.retrieval.with_streaming_response.generate_embeddings(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalGenerateEmbeddingsResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.search(
            query="query",
        )
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncNebula) -> None:
        retrieval = await async_client.retrieval.search(
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
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncNebula) -> None:
        response = await async_client.retrieval.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncNebula) -> None:
        async with async_client.retrieval.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True
