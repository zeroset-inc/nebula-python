# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Message"]


class Message(BaseModel):
    role: Union[Literal["system", "user", "assistant", "function", "tool"], str]

    content: Optional[object] = None

    function_call: Optional[Dict[str, object]] = None

    image_data: Optional[Dict[str, str]] = None

    image_url: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    name: Optional[str] = None

    structured_content: Optional[List[Dict[str, object]]] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[Dict[str, object]]] = None
