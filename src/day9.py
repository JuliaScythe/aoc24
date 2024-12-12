import time
from enum import Enum
import itertools
from rich.console import Console
from rich.progress import track
console = None # filled in by runner


def expand_map(inp):
    result = []
    n = 0

    if len(inp) % 2 == 1:
        inp += '0' # ensure even number of inputs

    for x1, x2 in itertools.batched(inp, n=2):
        file_list = [n for _ in range(int(x1))]
        empty_list = [-1 for _ in range(int(x2))]
        result = result + file_list + empty_list
        n += 1
    return result

def solve_1(inp):
    dmap = expand_map(inp[0].strip())

    while -1 in dmap:
        blkid = dmap[-1]
        dmap[dmap.index(-1)] = blkid
        del dmap[-1]

    return sum(map(lambda x: x[0]*x[1], enumerate(dmap)))


_no_status_2 = True
def solve_2(inp):
    dmap = expand_map(inp[0].strip())
    max_id = max(dmap)

    for id in track(range(max_id, 0, -1), description="Solving part 2..."):
        size = dmap.count(id)
        fstart = dmap.index(id)

        # look for big enough gaps, left to right
        # this could be done faster using the original map but i don't care
        i = 0
        run = 0
        run_start = 0
        found = False
        while i < len(dmap):
            if dmap[i] != -1:
                run = 0
                run_start = i
                i += 1
                continue
            run += 1
            i += 1
            if run == size:
                found = True
                break
        

        if not found or fstart < run_start:
            continue

        for i in range(size):
            dmap[run_start + i + 1] = id
            dmap[fstart + i] = -1


    return sum(map(lambda x: x[0]*x[1], enumerate(map(lambda x: x if x != -1 else 0, dmap))))
        

def pp(dmap):
    for x in dmap:
        if x == -1:
            print(".", end='')
        else:
            print(int(x), end='')
    print("")