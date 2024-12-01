import time
from rich.console import Console
console = Console()

def solve_1(inp):
    # input will come as a list of lines "x   y"
    return sum(map(lambda x: abs(x[0] - x[1]),zip(*map(lambda x: sorted(list(x)), zip(*map(lambda line: map(lambda y: int(y), line.split()),inp))))))

def solve_2(inp):
    # I think a oneliner is going to be more annoying this time :(
    ziplist = list(zip(*map(lambda line: map(lambda y: int(y), line.split()),inp)))
    list1 = ziplist[0]
    list2 = ziplist[1]
    return sum(map(lambda x: x*list2.count(x), list1))
