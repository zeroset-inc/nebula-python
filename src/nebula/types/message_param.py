# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageParam"]


class MessageParam(TypedDict, total=False):
    role: Required[Union[Literal["system", "user", "assistant", "function", "tool"], str]]

    content: object

    function_call: Optional[Dict[str, object]]

    image_data: Optional[Dict[str, str]]

    image_url: Optional[str]

    metadata: Optional[Dict[str, object]]

    name: Optional[str]

    structured_content: Optional[Iterable[Dict[str, object]]]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[Dict[str, object]]]
