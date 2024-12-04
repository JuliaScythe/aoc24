import time
import grid
from rich.console import Console
console = None # filled in by runner

def solve_1(inp):
    inp_grid = grid.Grid(inp)
    count = 0
    
    def count_cell(cell):
        nonlocal count
        words = cell.get_cardinal_words(length=4)
        for word in words.values():
            if "".join(word) == "XMAS":
                count += 1
    
    inp_grid.for_each(count_cell)

    return count

def solve_2(inp):
    inp_grid = grid.Grid(inp)
    count = 0
    
    def count_cell(cell):
        nonlocal count
        words = cell.get_cardinal_words(length=2)
        words = {k: "".join(v) for k, v in words.items()}

        if words[grid.Direction.NORTHEAST] + words[grid.Direction.SOUTHWEST] in {"AMAS", "ASAM"} and  words[grid.Direction.NORTHWEST] + words[grid.Direction.SOUTHEAST] in {"AMAS", "ASAM"}:
            count += 1
            
    
    inp_grid.for_each(count_cell)

    return count

