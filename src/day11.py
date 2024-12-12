import time
import functools
import sys
from rich.console import Console
console = None # filled in by runner

maxn =0

sys.setrecursionlimit(4096)

@functools.cache
def recursive_count(x, n):
    if n == 0:
        return 1
    if x == 0:
        return recursive_count(1, n - 1)
    if len(str(x)) % 2 == 0:
        xs = str(x)
        left = int(xs[:len(xs)//2])
        right = int(xs[len(xs)//2:])
        return recursive_count(left, n - 1) + recursive_count(right, n - 1)
    else:
        return recursive_count(x * 2024, n - 1)

def solve_1(inp):
    nums = map(int, inp[0].strip().split(" "))
    return sum(map(lambda x: recursive_count(x, 25), nums))

def solve_2(inp):
    nums = map(int, inp[0].strip().split(" "))
    return sum(map(lambda x: recursive_count(x, 75), nums))
