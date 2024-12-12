import time
from rich.console import Console
console = None # filled in by runner

def rec_pos(target, current, xs):
    if current > target:
        return False 
    if len(xs) == 0:
        return current == target
    else:
        return (rec_pos(target, current+xs[0], xs[1:]) or rec_pos(target, current*xs[0], xs[1:]))

def solve_1(inp):
    total = 0
    for line in inp:
        parts = line.split(":")
        target = int(parts[0])
        xs = list(map(int, parts[1].strip().split(" ")))
        if rec_pos(target, xs[0], xs[1:]):
            total += target

    return total 

def rec_pos_2(target, current, xs):
    if current > target:
        return False 
    if current == target and len(xs) == 0:
        return True
    if len(xs) == 0:
        return False
    else:
        return (rec_pos_2(target, current+xs[0], xs[1:]) or rec_pos_2(target, current*xs[0], xs[1:]) or rec_pos_2(target, int(str(current)+str(xs[0])), xs[1:]))

def solve_2(inp):
    total = 0
    for line in inp:
        parts = line.split(":")
        target = int(parts[0])
        xs = list(map(int, parts[1].strip().split(" ")))
        if rec_pos_2(target, xs[0], xs[1:]):
            total += target

    return total 

