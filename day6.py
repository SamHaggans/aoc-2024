import sys

POSITIONS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

def progress_direction(direction):
    if direction == (1, 0):
        return (0, -1)
    elif direction == (-1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (1, 0)
    else:
        return(-1, 0)


def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    grid = [[char for char in line] for line in lines]
    position = None
    direction = (0, 0)
    for r, row in enumerate(grid):
        for c, character in enumerate(row):
            if character in POSITIONS.keys():
                position = (r, c)
                direction = POSITIONS[character]
                break
    if position is None:
        print("Error: No direction found")
    print(f"Starting {position} direction {direction}")
    print(len(grid))
    print(len(grid[0]))
    within_row = lambda row: 0 <= row < len(grid)
    within_col = lambda col: 0 <= col < len(grid[0])

    while within_row(position[0]) and within_col(position[1]):
        grid[position[0]][position[1]] = "X"
        newpos = [position[0] + direction[0], position[1] + direction[1]]
        while within_row(newpos[0]) and within_col(newpos[1]) and grid[newpos[0]][newpos[1]] == "#":
            direction = progress_direction(direction)
            newpos = [position[0] + direction[0], position[1] + direction[1]]
        position = newpos
        print(f"STEP: {position}")
    
    count = 0
    for r, row in enumerate(grid):
        for c, character in enumerate(row):
            if character == "X":
                count += 1
    
    print(count)
    print(len(grid))
    print(len(grid[0]))

def next_turn_leads_to_loop(grid, directions, position, direction):
    base_position = position
    # Consider going forward until the next turn
    # does our final next step after the next turn
    # take us somewhere we've been?
    within_row = lambda row: 0 <= row < len(grid)
    within_col = lambda col: 0 <= col < len(grid[0])
    has_turned = False
    turn_pos = None
    loopcount = 0
    while within_row(position[0]) and within_col(position[1]) and loopcount < 100000:
        newpos = [position[0] + direction[0], position[1] + direction[1]]
        stuckcount = 0
        while within_row(newpos[0]) and within_col(newpos[1]) and grid[newpos[0]][newpos[1]] == "#":
            direction = progress_direction(direction)
            newpos = [position[0] + direction[0], position[1] + direction[1]]

            if not has_turned:
                turn_pos = position
                has_turned = True
        position = newpos
        loopcount += 1
    return loopcount >= 100000

    
    
    
def part2(file: str):
    directions = dict()
    with open(file, "r") as f:
        lines = f.read().split("\n")
    grid = [[char for char in line] for line in lines]
    position = None
    direction = (0, 0)
    for r, row in enumerate(grid):
        for c, character in enumerate(row):
            if character in POSITIONS.keys():
                position = (r, c)
                direction = POSITIONS[character]
                break
    if position is None:
        print("Error: No direction found")
    starting = tuple(position)
    print(f"Starting {position} direction {direction}")
    print(len(grid))
    print(len(grid[0]))
    within_row = lambda row: 0 <= row < len(grid)
    within_col = lambda col: 0 <= col < len(grid[0])
    loop_count = 0

    while within_row(position[0]) and within_col(position[1]):
        if (position[0], position[1]) not in directions:
            directions[(position[0], position[1])] = list()
            directions[(position[0], position[1])].append(tuple(direction))
        else:
            directions[(position[0], position[1])].append(tuple(direction))
        grid[position[0]][position[1]] = "X"
        # for row in grid:
        #     print("".join(row))
        newpos = [position[0] + direction[0], position[1] + direction[1]]
        while within_row(newpos[0]) and within_col(newpos[1]) and grid[newpos[0]][newpos[1]] == "#":
            direction = progress_direction(direction)
            newpos = [position[0] + direction[0], position[1] + direction[1]]
        # found new position
        # consider turning right right now
        # print(f"Pretending to put barrier at {newpos}")
        try:
            if grid[newpos[0]][newpos[1]] == "X":
                raise ValueError()
            prev = grid[newpos[0]][newpos[1]]
            grid[newpos[0]][newpos[1]] = "#"
            temp_direction = progress_direction(direction)
            temp_newpos = [position[0] + temp_direction[0], position[1] + temp_direction[1]]
            run_count = 0
            while grid[temp_newpos[0]][temp_newpos[1]] == "#" and run_count < 10:
                temp_direction = progress_direction(temp_direction)
                temp_newpos = [position[0] + temp_direction[0], position[1] + temp_direction[1]]
                run_count += 1
            if  next_turn_leads_to_loop(grid, directions, position, temp_direction) and starting != tuple(newpos):
                loop_count += 1
            
            grid[newpos[0]][newpos[1]] = prev
        except:
            pass

        position = newpos
        # print(f"STEP: {position}")
    print(loop_count)


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])