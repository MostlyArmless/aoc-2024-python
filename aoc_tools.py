from aoc_types import Position

def is_outside_grid(position: Position, num_rows: int, num_cols: int) -> bool:
    return not is_inside_grid(position, num_rows, num_cols)

def is_inside_grid(position: Position, num_rows: int, num_cols: int) -> bool:
    return 0 <= position[0] < num_rows and 0 <= position[1] < num_cols