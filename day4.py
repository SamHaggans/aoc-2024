import sys

DESIRED_P1 = "XMAS"

def in_bounds(arr, x, y):
    x_good = 0 <= x < len(arr[0])
    y_good = 0 <= y < len(arr)
    return x_good and y_good

def check_range(chars, x, y, delta_x, delta_y, DESIRED):
    index = 0
    while index < len(DESIRED):
        if not in_bounds(chars, x, y):
            return False
        if chars[y][x] != DESIRED[index]:
            return False
        x += delta_x
        y += delta_y
        index += 1
    return True

def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    chars = [[char for char in line] for line in lines]
    count = 0
    for y, line in enumerate(chars):
        for x, char in enumerate(line):
            for delx, dely in ((0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)):
                if check_range(chars, x, y, delx, dely, DESIRED_P1):
                    count +=1 

                

    print(count)

DESIRED_P2 = "MAS"

def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    chars = [[char for char in line] for line in lines]
    cross_counts = [[0 for char in line] for line in chars]
    count = 0
    for y, line in enumerate(chars):
        for x, char in enumerate(line):
            for delx, dely in ((1, 1), (-1, -1), (-1, 1), (1, -1)):
                if check_range(chars, x, y, delx, dely, DESIRED_P2):
                    cross_counts[y+dely][x+delx] += 1


    for row in cross_counts:
        for val in row:
            if val == 2:
                count += 1
    print(count)


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])