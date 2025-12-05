# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, TypedDict

from .search_mode import SearchMode
from .message_param import MessageParam
from .search_settings_param import SearchSettingsParam
from .generation_config_param import GenerationConfigParam

__all__ = ["RetrievalEngageAgentParams"]


class RetrievalEngageAgentParams(TypedDict, total=False):
    conversation_id: Optional[str]
    """ID of the conversation"""

    include_title_if_available: bool
    """Pass engram titles from search results into the LLM context window."""

    max_tool_context_length: Optional[int]
    """Maximum length of returned tool context"""

    message: Optional[MessageParam]
    """Current message to process"""

    messages: Optional[Iterable[MessageParam]]
    """List of messages (deprecated, use message instead)"""

    mode: Optional[Literal["rag", "research"]]
    """
    Mode to use for generation: 'rag' for standard retrieval or 'research' for deep
    analysis with reasoning capabilities
    """

    needs_initial_conversation_name: Optional[bool]
    """
    If true, the system will automatically assign a conversation name if not already
    specified previously.
    """

    rag_generation_config: GenerationConfigParam
    """Configuration for RAG generation in 'rag' mode"""

    rag_tools: Optional[
        List[
            Literal["web_search", "web_scrape", "search_file_descriptions", "search_file_knowledge", "get_file_content"]
        ]
    ]
    """List of tools to enable for RAG mode.

    Available tools: search_file_knowledge, get_file_content, web_search,
    web_scrape, search_file_descriptions
    """

    research_generation_config: Optional[GenerationConfigParam]
    """Configuration for generation in 'research' mode.

    If not provided but mode='research', rag_generation_config will be used with
    appropriate model overrides.
    """

    research_tools: Optional[List[Literal["rag", "reasoning", "critique", "python_executor"]]]
    """List of tools to enable for Research mode.

    Available tools: rag, reasoning, critique, python_executor
    """

    search_mode: SearchMode
    """
    Graph search algorithm: 'fast' (simple BFS) or 'super' (SuperBFS with
    contextualization, default).
    """

    search_settings: Optional[SearchSettingsParam]
    """
    Simplified search settings with automatic hybrid search and type-specific
    limits.
    """

    task_prompt: Optional[str]
    """Optional custom prompt to override default"""

    use_system_context: Optional[bool]
    """Use extended prompt for generation"""
