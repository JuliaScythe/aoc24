import time
from rich.console import Console

console = None  # filled in by runner


def solve_1(inp):
    # input will come as a list of lines "x   y"
    return sum(                                                                     # sum all the differences up
        map(
            lambda x: abs(x[0] - x[1]),                                             # find the difference between each pair
            zip(                                                                    # convert back into lists of pairs
                *map(
                    lambda x: sorted(list(x)),                                      # sort both lists
                    zip(                                                            # transpose that into two lists of integers
                        *map(
                            lambda line: map(lambda y: int(y), line.split()),       # split into a list of pairs of integers
                            inp)                                                    # the input
                    ),  
                )
            ),
        )
    )


def solve_2(inp):
    # I think a oneliner is going to be more annoying this time :(
    ziplist = list(zip(*map(lambda line: map(lambda y: int(y), line.split()), inp)))
    list1 = ziplist[0]
    list2 = ziplist[1]
    return sum(map(lambda x: x * list2.count(x), list1))
