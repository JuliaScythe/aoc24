import time
from grid import Grid, Direction
from rich.console import Console
console = None # filled in by runner

def solve_1(inp):
    grid = Grid(inp, default='K')

    # Get the position of the starting '^'
    sX, sY = grid.find("^")
    grid.x, grid.y = sX, sY

    current_direction = Direction.NORTH

    # Start following the path!
    while grid.inbounds():
        # Mark the current cell as visited (with the direction)
        grid.tag(current_direction)
        grid.push()
        grid.move(*current_direction.value)
        if grid.at() == "#":
            current_direction = current_direction.rotate(90)
        grid.pop()
        grid.move(*current_direction.value)
    
    return len(grid.tags.keys())

def solve_2(inp):
    grid = Grid(inp, default='K')

    # Get the position of the starting '^'
    sX, sY = grid.find("^")
    grid.x, grid.y = sX, sY

    current_direction = Direction.NORTH
    
    # first of all, run part one again to get a list of candidate locations for the wall
    # since we can only add a single wall, it must be along this path
    while grid.inbounds():
        grid.tag(current_direction)
        grid.push()
        grid.move(*current_direction.value)
        if grid.at() == "#":
            current_direction = current_direction.rotate(90)
        grid.pop()
        grid.move(*current_direction.value)
    
    candidate_locations = grid.tags.keys()
    count = 0

    for loc in candidate_locations:
        if loc == (sX, sY):
            continue # no walling the starting location
        grid.tags = {}
        grid.x = sX
        grid.y = sY
        current_direction = Direction.NORTH
        while grid.inbounds():
            if hit_cycle(grid.tags, (grid.x, grid.y), current_direction):
                count += 1
                break
            grid.tag(current_direction)
            
            grid.push()
            grid.move(*current_direction.value)
            while grid.at() == "#" or (grid.x, grid.y) == loc:
                current_direction = current_direction.rotate(90)
                grid.pop()
                grid.push()
                grid.move(*current_direction.value)
            grid.pop()
            grid.move(*current_direction.value)
            
    return count
    
def hit_cycle(tags, loc, dir):
    if loc in tags:
        return dir in tags[loc]
    else:
        return False