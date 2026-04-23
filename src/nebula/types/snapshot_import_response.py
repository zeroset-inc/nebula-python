# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SnapshotImportResponse", "Results"]


class Results(BaseModel):
    """Ephemeral collection handle returned after importing a snapshot."""

    ephemeral_collection_id: str


class SnapshotImportResponse(BaseModel):
    results: Results
    """Ephemeral collection handle returned after importing a snapshot."""
