import re
from rich.console import Console
console = None # filled in by runner

def solve_1(inp):
    return sum(map(lambda x: int(x[0]) * int(x[1]), re.compile(r"mul\((\d{1,3}),(\d{1,3})\)").findall(" ".join(inp))))


def solve_2(inp):
    doing = True
    sum = 0
    matches = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t(\(\))").findall(" ".join(inp))
    for m in matches:
        if (m[0] == ''):
            doing = not m[2] == "()"
        elif (doing):
            sum += (int(m[0]) * int(m[1]))

    return sum

