import time
import importlib
from rich.console import Console

console = Console()

DAY = 6

def solve_1(inp):
    pass

def solve_2(inp):
    pass

def solve(day=DAY):
    console.log(f"juli's Advent Of Code - Day {str(day)}")
    
    console.log(f"Importing solver script...")
    solver = importlib.import_module("day"+str(day))
    solver.console = console

    with open("inputs/input" + str(day)) as f:
        i = f.readlines()

    with console.status("[blue]Solving part 1...", spinner="dots"):
        t_start = time.perf_counter()
        res = solver.solve_1(i)
        t_end = time.perf_counter()
    
    console.log("[green]Part 1 completed in ", (t_end - t_start), "seconds")
    console.log("[bold green] ", res)
    
    with console.status("[blue]Solving part 2...", spinner="dots"):
        t_start = time.perf_counter()
        res = solver.solve_2(i)
        t_end = time.perf_counter()

    console.log("[green]Part 2 completed in ", (t_end - t_start), "seconds")
    console.log("[bold green] ", res)


    
if __name__ == "__main__":
    solve(day=DAY)
    console.log("[purple]All done <3")