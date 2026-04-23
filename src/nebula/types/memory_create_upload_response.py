# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MemoryCreateUploadResponse", "Results"]


class Results(BaseModel):
    bucket: str

    download_url: str

    expires_in: int

    max_size: int

    s3_key: str

    upload_headers: Dict[str, str]

    upload_url: str


class MemoryCreateUploadResponse(BaseModel):
    results: Results
