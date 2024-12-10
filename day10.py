import sys
from collections import deque
import itertools

def in_bounds(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols

def routing_neighbors(grid, point):
    offsets = (0, 1, -1)
    neighbors = []
    possible_neighbor_diffs = ((1, 0), (-1, 0), (0, -1), (0, 1))
    for offset in possible_neighbor_diffs:
        (r, c) = (point[0] + offset[0], point[1] + offset[1])
        if in_bounds(grid, r, c) and grid[r][c] == grid[point[0]][point[1]] + 1:
            neighbors.append((r, c))
    return neighbors



def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    grid = [[(lambda v: int(v) if v != "." else v)(x) for x in line] for line in lines]

    starting_points = []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 0:
                starting_points.append((r, c))

    total_count = 0
    for point in starting_points:
        point_queue = deque()
        point_queue.append(point)
        routecount = 0
        visited = set()
        while len(point_queue) != 0:
            pt = point_queue.pop()
            visited.add(pt)
            if grid[pt[0]][pt[1]] == 9:
                routecount += 1
            else:
                new_neighbors = routing_neighbors(grid, pt)
                for neighbor in new_neighbors:
                    if neighbor not in visited:
                        point_queue.append(neighbor)
        total_count += routecount
    print(total_count)




def part2(file: str):
    # Identical to p1 except don't check if a place is visited
    # funnily enough this is the way I (incorrectly) did part 1 at first :)
    with open(file, "r") as f:
        lines = f.read().split("\n")
    grid = [[(lambda v: int(v) if v != "." else v)(x) for x in line] for line in lines]

    starting_points = []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 0:
                starting_points.append((r, c))

    total_count = 0
    for point in starting_points:
        point_queue = deque()
        point_queue.append(point)
        routecount = 0
        visited = set()
        while len(point_queue) != 0:
            pt = point_queue.pop()
            visited.add(pt)
            if grid[pt[0]][pt[1]] == 9:
                routecount += 1
            else:
                new_neighbors = routing_neighbors(grid, pt)
                for neighbor in new_neighbors:
                    point_queue.append(neighbor)
        total_count += routecount
    print(total_count)


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])