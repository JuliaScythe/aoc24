import time
from grid import Grid, Direction
from rich.console import Console
console = None # filled in by runner

def cardinal_explore(grid: Grid, initial: tuple[int, int], current: tuple[int, int]) -> None:
    curr_height = int(grid.get(*current))
    if curr_height == 9:
        grid.tag(initial, *current)
        return
    else:
        for dir in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]:
            next_current = (current[0]+dir.value[0], current[1]+dir.value[1])
            if int(grid.get(*next_current)) == curr_height + 1:
                cardinal_explore(grid, initial, next_current)


def solve_1(inp: list[str]) -> int:
    grid = Grid(inp, default="-1")

    score = 0
    for zX, zY in grid.find_all("0"):
        grid.tags = {}
        cardinal_explore(grid, (zX, zY), (zX, zY))
        score += len(grid.tags.keys())

    return score

def solve_2(inp: list[str]) -> int:
    grid = Grid(inp, default="-1")

    score = 0
    for zX, zY in grid.find_all("0"):
        grid.tags = {}
        cardinal_explore(grid, (zX, zY), (zX, zY))
        for v in grid.tags.values():
            score += len(v)

    return score
