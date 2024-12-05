import time
from rich.console import Console
from functools import cmp_to_key
console = None # filled in by runner

def parse_rules(inp):
    pages_rules = {}
    section_break = 0
    for i,line in enumerate(inp):
        if line == "\n":
            section_break = i
            break
        # line = "XX|YY"
        left = int(line[0:2])
        right = int(line[3:5])
        if left not in pages_rules:
            pages_rules[left] = [right]
        else:
            pages_rules[left].append(right)
    return pages_rules, section_break

def solve_1(inp):
    pages_rules, section_break = parse_rules(inp)
    
    total = 0
    for line in inp[section_break+1:]:
        nline = list(map(int, line.strip().split(",")))
        if (is_line_good(nline, pages_rules)):
            total += nline[int((len(nline) - 1)/2)]
    
    return total
        

def is_line_good(nline, pages_rules):
    seen = []
    for i, entry in enumerate(nline):
        if entry not in pages_rules:
            seen.append(entry)
            continue # no rules relating to this page
        for t in seen:
            if t in pages_rules[entry]:
                # violation!
                return False
        seen.append(entry)
    return True

def solve_2(inp):
    pages_rules, section_break = parse_rules(inp)
    
    total = 0
    for line in inp[section_break+1:]:
        nline = list(map(int, line.strip().split(",")))
        if not is_line_good(nline, pages_rules):
            fixlist = reorder(nline, pages_rules)
            total += fixlist[int((len(fixlist) - 1)/2)]
    
    return total

def reorder(nline, pages_rules):
    def comparator(l, r):
        if l in pages_rules and r in pages_rules[l]:
            return -1
        elif r in pages_rules and l in pages_rules[r]:
            return 1
        else:
            return 0
    return sorted(nline, key=cmp_to_key(comparator))
