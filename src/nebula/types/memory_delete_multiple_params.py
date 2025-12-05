# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["MemoryDeleteMultipleParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    body: Required[str]


class Variant1(TypedDict, total=False):
    body: Required[SequenceNotStr[str]]


MemoryDeleteMultipleParams: TypeAlias = Union[Variant0, Variant1]
