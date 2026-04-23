# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MemoryDeleteUploadParams"]


class MemoryDeleteUploadParams(TypedDict, total=False):
    s3_key: Required[str]
    """S3 key of the file to delete (returned by POST /memories/upload)"""
