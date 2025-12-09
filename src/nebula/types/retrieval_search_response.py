# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .chunk_search_result import ChunkSearchResult
from .web_page_search_result import WebPageSearchResult
from .memories.engram_response import EngramResponse

__all__ = [
    "RetrievalSearchResponse",
    "Results",
    "ResultsGraphSearchResult",
    "ResultsGraphSearchResultContent",
    "ResultsGraphSearchResultContentGraphEntityResult",
    "ResultsGraphSearchResultContentGraphRelationshipResult",
    "ResultsGraphSearchResultContentGraphCommunityResult",
    "ResultsGraphSearchResultContentGraphSpeakerResult",
    "ResultsWebSearchResult",
    "ResultsWebSearchResultPeopleAlsoAsk",
    "ResultsWebSearchResultRelatedSearch",
]


class ResultsGraphSearchResultContentGraphEntityResult(BaseModel):
    description: str

    name: str

    id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None


class ResultsGraphSearchResultContentGraphRelationshipResult(BaseModel):
    object: str

    predicate: str

    subject: str

    id: Optional[str] = None

    description: Optional[str] = None

    metadata: Optional[Dict[str, builtins.object]] = None

    object_id: Optional[str] = None

    score: Optional[float] = None

    subject_id: Optional[str] = None


class ResultsGraphSearchResultContentGraphCommunityResult(BaseModel):
    name: str

    summary: str

    id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None


class ResultsGraphSearchResultContentGraphSpeakerResult(BaseModel):
    name: str

    id: Optional[str] = None

    authority_score: Optional[float] = None

    description: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None


ResultsGraphSearchResultContent: TypeAlias = Union[
    ResultsGraphSearchResultContentGraphEntityResult,
    ResultsGraphSearchResultContentGraphRelationshipResult,
    ResultsGraphSearchResultContentGraphCommunityResult,
    ResultsGraphSearchResultContentGraphSpeakerResult,
]


class ResultsGraphSearchResult(BaseModel):
    id: str

    content: ResultsGraphSearchResultContent

    chunk_ids: Optional[List[str]] = None

    display_name: Optional[str] = None

    engram_id: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    owner_id: Optional[str] = None

    result_type: Optional[Literal["entity", "relationship", "community", "speaker"]] = None

    score: Optional[float] = None

    source_role: Optional[str] = None

    timestamp: Optional[datetime] = None


class ResultsWebSearchResultPeopleAlsoAsk(BaseModel):
    id: str

    link: str

    question: str

    snippet: str

    title: str

    type: Optional[str] = None


class ResultsWebSearchResultRelatedSearch(BaseModel):
    id: str

    query: str

    type: Optional[str] = None


class ResultsWebSearchResult(BaseModel):
    organic_results: Optional[List[WebPageSearchResult]] = None

    people_also_ask: Optional[List[ResultsWebSearchResultPeopleAlsoAsk]] = None

    related_searches: Optional[List[ResultsWebSearchResultRelatedSearch]] = None


class Results(BaseModel):
    """Result of an aggregate search operation."""

    chunk_search_results: Optional[List[ChunkSearchResult]] = None

    document_search_results: Optional[List[EngramResponse]] = None

    generic_tool_result: Optional[object] = None

    graph_search_results: Optional[List[ResultsGraphSearchResult]] = None

    web_page_search_results: Optional[List[WebPageSearchResult]] = None

    web_search_results: Optional[List[ResultsWebSearchResult]] = None


class RetrievalSearchResponse(BaseModel):
    results: Results
    """Result of an aggregate search operation."""
