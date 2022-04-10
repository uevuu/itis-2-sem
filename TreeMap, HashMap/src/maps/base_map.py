"""Abstract class for Map"""

from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class BaseMap(ABC):
    """Abstract class for Map"""

    @abstractmethod
    def __setitem__(self, key: str, value: int) -> None:
        ...

    @abstractmethod
    def __getitem__(self, key: str) -> int:
        ...

    @abstractmethod
    def __delitem__(self, key: str) -> None:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __iter__(self) -> Iterable[Tuple[str, int]]:
        ...

    def write(self, path: str) -> None:
        """write Map in file"""
        with open(path, "w+", encoding="utf-8") as file:
            for key, data in self:
                file.write(f"{key}\t{data}\n")

    @classmethod
    def read(cls, path: str) -> 'BaseMap':
        """read file in Map"""
        my_obj = cls()
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                key, value = line.split('\t')[0]
                my_obj[key] = int(value)

        return my_obj
