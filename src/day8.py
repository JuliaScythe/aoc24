import time, itertools
from grid import Grid
from rich.console import Console
console = None # filled in by runner

def parse_signals(grid):
    
    freqs = {}
    def add_signals(signal):
        freq = signal.at()
        if freq == ".":
            return
        sigX = signal.x
        sigY = signal.y
        if freq in freqs:
            freqs[freq].append((sigX, sigY))
        else:
            freqs[freq] = [(sigX, sigY)]
    
    grid.for_each(add_signals)
    return freqs

def solve_1(inp):
    grid = Grid(inp)
    freqs = parse_signals(grid)

    for freq, transmitters in freqs.items():
        for (startX, startY), (endX, endY) in itertools.permutations(transmitters, 2):
            grid.x = startX
            grid.y = startY
            # Compute the vector to end, double it, check if we're in the grid, then tag
            dX = endX - startX
            dY = endY - startY
            vec = (2*dX, 2*dY)
            grid.move(*vec)
            if grid.inbounds():
                grid.tag(freq)

    return len(grid.tags)

def solve_2(inp):
    grid = Grid(inp)
    freqs = parse_signals(grid)

    for freq, transmitters in freqs.items():
        for (startX, startY), (endX, endY) in itertools.permutations(transmitters, 2):
            grid.x = startX
            grid.y = startY

            dX = endX - startX
            dY = endY - startY

            vec = (dX, dY)
            
            while grid.inbounds():
                grid.tag(freq)
                grid.move(*vec)


    return len(grid.tags)
