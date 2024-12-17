from enum import Enum
from typing import Tuple, TypeAlias


class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'
    
    @classmethod
    def values(cls) -> set:
        return {d.value for d in cls}

Position: TypeAlias = Tuple[int, int]
ManhattanDistance: TypeAlias = Tuple[int, int]