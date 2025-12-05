# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CollectionGetDocumentsWithMemoriesParams"]


class CollectionGetDocumentsWithMemoriesParams(TypedDict, total=False):
    include_embeddings: bool
    """Whether to include embedding vectors in the response"""

    limit: int
    """Number of documents to return (1-100)"""

    offset: int
    """Number of documents to skip for pagination"""
