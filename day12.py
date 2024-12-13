import copy
import sys
from collections import deque
import itertools
import time
import dataclasses

@dataclasses.dataclass
class Edge:
    row: int
    col: int
    direction: int
    span: int = 1

def in_bounds(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols

def routing_neighbors(grid, point):
    neighbors = []
    possible_neighbor_diffs = ((1, 0), (-1, 0), (0, -1), (0, 1))
    for offset in possible_neighbor_diffs:
        (r, c) = (point[0] + offset[0], point[1] + offset[1])
        if in_bounds(grid, r, c) and grid[r][c] == grid[point[0]][point[1]]:
            neighbors.append((r, c))
    return neighbors



def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    grid = [[x for x in line] for line in lines]
    process_nodes = deque()
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            process_nodes.append((r, c))
    components = dict()
    component_index = 0

    while len(process_nodes) != 0:
        new_node = process_nodes.pop()
        point_queue = deque()
        point_queue.append(new_node)
        components[component_index] = set()

        visited = set()
        while len(point_queue) != 0:
            pt = point_queue.pop()
            visited.add(pt)
            if pt in process_nodes: process_nodes.remove(pt)
            components[component_index].add(pt)
            new_neighbors = routing_neighbors(grid, pt)
            for neighbor in new_neighbors:
                if neighbor not in visited:
                    point_queue.append(neighbor)
        component_index += 1

    total = 0
    for i, component in components.items():
        area = len(component)
        perimeter = 0
        for node in component:
            possible_neighbor_diffs = ((1, 0), (-1, 0), (0, -1), (0, 1))
            for n in possible_neighbor_diffs:
                if (node[0] + n[0], node[1] + n[1]) not in component:
                    perimeter += 1
        total += area*perimeter
    print(total)


def can_merge_edge(e1: Edge, e2: Edge, vertical=False):
    if e1.direction != e2.direction:
        return None
    if vertical:
        if e1.row >= e2.row:
            return None
        if e1.row + e1.span == e2.row and e1.col == e2.col:
            return Edge(e1.row, e1.col, span=e1.span + e2.span, direction=e1.direction)
        return None
    else:
        if e1.col >= e2.col:
            return None
        if e1.col + e1.span == e2.col and e1.row == e2.row:
            return Edge(e1.row, e1.col, span=e1.span + e2.span, direction=e1.direction)
        return None


def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    grid = [[x for x in line] for line in lines]
    process_nodes = deque()
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            process_nodes.append((r, c))
    components = dict()
    component_index = 0

    while len(process_nodes) != 0:
        new_node = process_nodes.pop()
        point_queue = deque()
        point_queue.append(new_node)
        components[component_index] = set()

        visited = set()
        while len(point_queue) != 0:
            pt = point_queue.pop()
            visited.add(pt)
            if pt in process_nodes: process_nodes.remove(pt)
            components[component_index].add(pt)
            new_neighbors = routing_neighbors(grid, pt)
            for neighbor in new_neighbors:
                if neighbor not in visited:
                    point_queue.append(neighbor)
        component_index += 1

    total = 0
    for i, component in components.items():
        print(f"Component {i}: {component}")
        area = len(component)
        perimeter = 0
        vertical_edges = []
        horizontal_edges = []
        edge_select = lambda k: horizontal_edges if k % 2 == 0 else vertical_edges
        for node in component:
            possible_neighbor_diffs = ((1, 0), (0, -1), (-1, 0), (0, 1))
            for nc, n in enumerate(possible_neighbor_diffs):
                neighbor = (node[0] + n[0], node[1] + n[1])
                direction = nc == 1 or nc == 2
                edge_append = Edge(max(node[0], neighbor[0]), max(node[1], neighbor[1]), direction=direction, span=1)
                if neighbor not in component:
                    edge_select(nc).append(edge_append)
        ctn = False
        did_merge = True
        
        print(f"Initial vertical: {vertical_edges}")
        while did_merge:
            did_merge = False
            new_edges = copy.deepcopy(vertical_edges)
            ctn = False
            for edge1 in vertical_edges:
                if ctn:
                    break
                for edge2 in vertical_edges:                
                    if ctn:
                        break
                    test_merge = can_merge_edge(edge1, edge2, vertical=True)
                    if test_merge is not None:
                        new_edges.remove(edge1)
                        new_edges.remove(edge2)
                        new_edges.append(test_merge)
                        ctn = True
                        did_merge = True
            vertical_edges = new_edges
        print(f"Final vertical: {vertical_edges}")
        ctn = False
        did_merge = True
        print(f"Initial horizontal: {horizontal_edges}")
        while did_merge:
            did_merge = False
            new_edges = copy.deepcopy(horizontal_edges)
            ctn = False
            for edge1 in horizontal_edges:
                if ctn:
                    break
                for edge2 in horizontal_edges:                
                    if ctn:
                        break
                    test_merge = can_merge_edge(edge1, edge2, vertical=False)
                    if test_merge is not None:
                        new_edges.remove(edge1)
                        new_edges.remove(edge2)
                        new_edges.append(test_merge)
                        ctn = True
                        did_merge = True
            horizontal_edges = new_edges
        print(f"Final horizontal: {horizontal_edges}")
        perimeter = len(horizontal_edges) + len(vertical_edges)
        total += area * perimeter
    print(total)






if __name__ == "__main__":
    #part1(sys.argv[1])
    part2(sys.argv[1])