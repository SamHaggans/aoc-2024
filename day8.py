import sys

def pairwise(lst):
    for i, elem in enumerate(lst):
        for nxt in lst[i+1:]:
            yield (elem, nxt)

def part1(file: str):
    locations = set()
    nodes = dict()
    with open(file, "r") as f:
        lines = f.read().split("\n")
    # rows cols
    dimensions = (len(lines), len(lines[0]))
    in_bounds = lambda rowcol: 0 <= rowcol[0] < dimensions[0] and 0 <= rowcol[1] < dimensions[1]
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val == ".": continue
            if val not in nodes:
                nodes[val] = list()
            nodes[val].append((r, c))
    for typ, nodes in nodes.items():
        for a, b in pairwise(nodes):
            delta_row = b[0] - a[0]
            delta_col = b[1] - a[1]
            min_row = min(b[0] + delta_row, a[0] + delta_row, b[0] - delta_row, a[0] - delta_row)
            max_row = max(b[0] + delta_row, a[0] + delta_row, b[0] - delta_row, a[0] - delta_row)
            min_col = min(b[1] + delta_col, a[1] + delta_col, b[1] - delta_col, a[1] - delta_col)
            max_col = max(b[1] + delta_col, a[1] + delta_col, b[1] - delta_col, a[1] - delta_col)
            print(min_row, max_row, min_col, max_col)
            if delta_col >= 0 <= delta_row or delta_col < 0 > delta_row:
                print("Both negative")
                nodes = ((min_row, min_col), (max_row, max_col))
            else:
                print("Opposites")
                nodes = ((min_row, max_col), (max_row, min_col))
            for node in nodes:
                if in_bounds(node) and node not in locations:
                    locations.add(node)
    print(locations)
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if (r, c) in locations:
                print("#", end="")
            else:
                print(val, end="")
        print()
    print(len(locations))

    
    
    
def part2(file: str):
    locations = set()
    nodes = dict()
    with open(file, "r") as f:
        lines = f.read().split("\n")
    # rows cols
    dimensions = (len(lines), len(lines[0]))
    in_bounds = lambda rowcol: 0 <= rowcol[0] < dimensions[0] and 0 <= rowcol[1] < dimensions[1]
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val == ".": continue
            if val not in nodes:
                nodes[val] = list()
            nodes[val].append((r, c))
    for typ, nodes in nodes.items():
        for a, b in pairwise(nodes):
            delta_row = b[0] - a[0]
            delta_col = b[1] - a[1]
            # choose node arbitrarily because they will all happen
            count = -1
            diff = (count * delta_row, count * delta_col)
            new_check = a[0] + diff[0], a[1] + diff[1]
            while in_bounds(new_check):
                if new_check not in locations:
                    locations.add(new_check)
                count -= 1
                diff = (count * delta_row, count * delta_col)
                new_check = a[0] + diff[0], a[1] + diff[1]
            count = 0
            diff = (count * delta_row, count * delta_col)
            new_check = a[0] + diff[0], a[1] + diff[1]
            while in_bounds(new_check):
                if new_check not in locations:
                    locations.add(new_check)
                count += 1
                diff = (count * delta_row, count * delta_col)
                new_check = a[0] + diff[0], a[1] + diff[1]
    print(locations)
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if (r, c) in locations:
                print("#", end="")
            else:
                print(val, end="")
        print()
    print(len(locations))


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])