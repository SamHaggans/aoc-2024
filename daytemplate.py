import sys


def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])