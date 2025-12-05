# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .generation_config_param import GenerationConfigParam

__all__ = ["IngestionConfigParam", "App", "ChunkEnrichmentSettings"]


class App(TypedDict, total=False):
    allowed_webhook_ips: SequenceNotStr[str]

    app_base_url: Optional[str]

    audio_lm: Optional[str]

    default_max_chunks_per_user: Optional[int]

    default_max_collections_per_user: Optional[int]

    default_max_documents_per_user: Optional[int]

    default_max_upload_size: int

    extra_fields: Dict[str, object]

    fast_llm: Optional[str]

    max_upload_size_by_type: Dict[str, int]

    planning_llm: Optional[str]

    project_name: Optional[str]

    quality_llm: Optional[str]

    reasoning_llm: Optional[str]

    require_service_api_key: bool

    service_api_key: Optional[str]

    stripe_secret_key: Optional[str]

    stripe_webhook_secret: Optional[str]

    user_tools_path: Optional[str]

    vlm: Optional[str]

    webhook_hmac_secret: Optional[str]

    webhook_hmac_secret_previous: Optional[str]

    webhook_ip_validation_enabled: bool

    webhook_rate_limit_max_requests: int

    webhook_rate_limit_window_seconds: int

    webhook_signature_validation_enabled: bool


class ChunkEnrichmentSettings(TypedDict, total=False):
    chunk_enrichment_prompt: Optional[str]
    """The prompt to use for chunk enrichment"""

    enable_chunk_enrichment: bool
    """Whether to enable chunk enrichment or not"""

    generation_config: Optional[GenerationConfigParam]
    """The generation config to use for chunk enrichment"""

    n_chunks: int
    """The number of preceding and succeeding chunks to include. Defaults to 2."""


class IngestionConfigParam(TypedDict, total=False):
    app: Optional[App]

    audio_transcription_model: Optional[str]

    automatic_extraction: bool

    chunk_enrichment_settings: ChunkEnrichmentSettings
    """Settings for chunk enrichment."""

    chunk_overlap: int

    chunk_size: int

    chunking_strategy: Union[str, Literal["recursive", "character", "basic", "by_title"]]

    chunks_for_document_summary: int

    document_summary_max_length: int

    document_summary_model: Optional[str]

    document_summary_system_prompt: str

    document_summary_task_prompt: str

    excluded_parsers: SequenceNotStr[str]

    extra_fields: Dict[str, object]

    extra_parsers: Dict[str, object]

    max_concurrent_vlm_tasks: int

    parser_overrides: Dict[str, str]

    provider: str

    skip_document_summary: bool

    vlm: Optional[str]

    vlm_batch_size: int

    vlm_max_tokens_to_sample: int

    vlm_ocr_one_page_per_chunk: bool
