import time, itertools
from rich.console import Console

console = None  # filled in by runner


def prx(x):  # for easy debugging
    console.log(list(x))
    return x


def prxx(x):
    console.log(list([list(y) for y in x]))
    return x


def solve_1(inp):

    return len(                                                                         # count the reports that are still alive
        list(
            filter(
                lambda l: all(map(lambda x: 1 <= abs(x) <= 3, l))
                and (all(map(lambda x: x > 0, l)) or all(map(lambda x: x < 0, l))),     # remove each report that doesn't satisfy the predicate
                map(
                    lambda l: list(map(lambda x: x[0] - x[1], l)),                      # create a list of differences in each element
                    map(
                        lambda l: zip(*l),                                              # create a list of pairs from both lists    
                        list(
                            map(
                                lambda l: (       
                                    list(l[0]),                                                                           
                                    list(itertools.islice(l[1], 1, None)),              # advance the second list by one element
                                ),
                                map(
                                    lambda x: itertools.tee(x),                         # duplicate each list
                                    map(
                                        lambda l: map(lambda x: int(x), l),             # convert the input to integers
                                        map(lambda x: x.split(), inp),                  # split up the input into a list of lists
                                    ),
                                ),
                            )
                        ),
                    ),
                ),
            ),
        )
    )


def solve_2(inp):
    reports = list(
            map(
                lambda l: list(map(lambda x: int(x), l)),
                map(lambda x: x.split(), inp),
            ),
    )

    reports_expanded = []
    for l in reports:
        report_expanded = [l]
        for i, _ in enumerate(l):
            new_list = l.copy()
            del new_list[i]
            report_expanded.append(new_list)
        reports_expanded.append(report_expanded)

    def is_good(l):
        (i, j) = itertools.tee(l)
        next(j)
        diffs = list(map(lambda x: x[0] - x[1], zip(i,j)))
        return all(map(lambda x: 1 <= abs(x) <= 3, diffs)) and (all(map(lambda x: x > 0, diffs)) or all(map(lambda x: x < 0, diffs)))

    return len(list(filter(lambda l: any(map(is_good, l)), reports_expanded)))