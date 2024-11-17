"""
Deeplake core types and functions
"""

from __future__ import annotations

import typing

__all__ = ["Dict", "IndexMapping64", "MemoryBuffer"]

class Dict:
    def __getstate__(self: dict) -> dict:
        ...
    def __setstate__(self: dict, arg0: dict) -> None:
        ...
    def __eq__(self: dict, other: dict | dict) -> bool:
        ...
    def __getitem__(self: dict, key: str) -> typing.Any:
        ...
    def __len__(self: dict) -> int:
        ...
    def __ne__(self: dict, other: dict | dict) -> bool:
        ...
    def items(self: dict) -> list:
        ...
    def keys(self: dict) -> list[str]:
        ...
    def to_dict(self: dict) -> dict:
        ...


class IndexMapping64:
    def __getitem__(self, index: int) -> int: ...


    def __getstate__(self) -> tuple:
        ...

    def __iter__(self) -> typing.Iterator[int]:
        ...

    def __len__(self) -> int:
        ...

    def __setstate__(self, arg0: tuple) -> None:
        ...


class MemoryBuffer:
    def __buffer__(self, flags):
        """
        Return a buffer object that exposes the underlying memory of the object.
        """
        ...

    def __release_buffer__(self, buffer):
        """
        Release the buffer object that exposes the underlying memory of the object.
        """
        ...