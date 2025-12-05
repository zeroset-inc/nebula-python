# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RetrievalGenerateEmbeddingsParams"]


class RetrievalGenerateEmbeddingsParams(TypedDict, total=False):
    body: Required[str]
    """Text to generate embeddings for"""
