# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["WebPageSearchResult"]


class WebPageSearchResult(BaseModel):
    id: str

    position: int

    date: Optional[str] = None

    link: Optional[str] = None

    sitelinks: Optional[List[Dict[str, object]]] = None

    snippet: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None
