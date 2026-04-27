# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MemoryCreateUploadParams"]


class MemoryCreateUploadParams(TypedDict, total=False):
    content_type: Required[str]
    """MIME type (e.g., 'image/jpeg', 'application/pdf')"""

    file_size: Required[int]
    """Expected file size in bytes (max 100MB)"""

    filename: Required[str]
    """Original filename (e.g., 'image.jpg')"""
