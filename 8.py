from aoc_tools import is_inside_grid, manhattan_distance
from aoc_types import Position
from collections import defaultdict
from typing import Dict, List, Set, TypeAlias
from utils import timer
from itertools import combinations

sample_input = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
real_input = '''..f........................8......................
G............8..u.................................
........G...p.....................................
......d.....................n.....................
..................................................
.....................................K............
..................F...8.n...B.K...................
....b.........8..u................................
...............F.p.......B.............4.....5....
....f..d..U.........................c.............
...........U.....d.n.u.0................5.........
...Y.......f..........................5...........
..........................u.....d.....e.........4.
..F...p.............v........n....................
....s.............0...............................
...US.s....g.....D..........................4.....
......wG...............S..........................
.............................B.....e..............
.........w.........................A..............
.............9w.g..........................4......
U....9..g.....v.....P....D.....f.K................
.s.............0..9........pP..........5..........
..9s...................P..........................
.............b..................0.....A..2....e...
....................b.....V..v....................
.......7........B......................A..........
..................D6...V....q.....................
...v............D....PV...........................
.........Y...........g.......................e..y.
.......SW......V..7....................c..........
.......bY7.....................N........A.........
.....................q.N..........y...............
........................N.........c...............
..................................................
.........C..7..................q........2.........
............................N...q.................
...W......C3...Q................a1.........y......
.......W.......................3......2...........
........3...........6.............1...............
....3............C.1....................k.........
E..................................a.....c........
.............................................w....
..S.......................Q..........2......k.....
......................C....6.......Q......ak......
..................................................
.................E.............a1............y....
W..........E......................................
......E...........6...........Q...................
...........................k......................
..................................................'''

Frequency: TypeAlias = str
@timer
def part1(input: str):
    grid = input.split('\n')
    num_rows = len(grid)
    num_cols = len(grid[0])
    all_antennae: Dict[Frequency, List[Position]] = locate_antennae(grid)
    all_antinodes = set()

    for freq, antennae_on_freq in all_antennae.items():
        # Find the antinodes for just this frequency's antennae, discarding any
        # which are outside the grid boundaries
        antinode_locations = locate_antinodes(num_rows, num_cols, antennae_on_freq)
        for antinode in antinode_locations:
            all_antinodes.add(antinode)

    return len(all_antinodes)

def locate_antennae(grid) -> Dict[str,List[Position]]:
    antennae = defaultdict(list)
    for i_row, row in enumerate(grid):
        for i_col, cell in enumerate(row):
            if cell != '.':
                antennae[cell].append((i_row, i_col))
    return antennae

def locate_antinodes(num_rows: int, num_cols: int, antennae: List[Position]) -> Set[Position]:
    # Find the distance between each pair of antennae
    antinodes: Set[Position] = set()
    for pair in combinations(antennae, 2):
        distance = manhattan_distance(pair[0], pair[1])
        antinode_a = (pair[0][0] - distance[0], pair[0][1] - distance[1])
        if is_inside_grid(antinode_a, num_rows, num_cols):
            antinodes.add(antinode_a)

        antinode_b = (pair[1][0] + distance[0], pair[1][1] + distance[1])
        if is_inside_grid(antinode_b, num_rows, num_cols):
            antinodes.add(antinode_b)

    return antinodes

def locate_antinodes_part2(num_rows: int, num_cols: int, antennae: List[Position]) -> Set[Position]:
    # Find the distance between each pair of antennae
    antinodes: Set[Position] = set()
    for pair in combinations(antennae, 2):
        distance = manhattan_distance(pair[0], pair[1])
        a = pair[0]
        b = pair[1]
        # simultaneously go from a towards b and b towards a
        while True:
            a_inside = is_inside_grid(a, num_rows, num_cols)
            b_inside = is_inside_grid(b, num_rows, num_cols)
            
            if a_inside:
                antinodes.add(a)
            if b_inside:
                antinodes.add(b)

            if not a_inside and not b_inside:
                break
            
            a = (a[0] - distance[0], a[1] - distance[1])
            b = (b[0] + distance[0], b[1] + distance[1])

    return antinodes

@timer
def part2(input: str) -> int:
    grid = input.split('\n')
    num_rows = len(grid)
    num_cols = len(grid[0])
    all_antennae: Dict[Frequency, List[Position]] = locate_antennae(grid)
    all_antinodes = set()

    for freq, antennae_on_freq in all_antennae.items():
        # Find the antinodes for just this frequency's antennae, discarding any
        # which are outside the grid boundaries
        antinode_locations = locate_antinodes_part2(num_rows, num_cols, antennae_on_freq)
        for antinode in antinode_locations:
            all_antinodes.add(antinode)

    return len(all_antinodes)

assert part1(sample_input) == 14
assert part1(real_input) == 295

assert part2(sample_input) == 34
assert part2(real_input) == 1034
