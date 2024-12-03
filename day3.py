import sys
import re

def mul(a, b):
    return a*b

def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    total = "".join(lines)
    reg = r"mul\(\d+,\d+\)"
    matches = re.findall(reg, total)
    print(sum(eval(m) for m in matches))
    

def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    total = "".join(lines)
    reg = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(reg, total)
    s = 0
    run = True
    for match in matches:
        if match == "do()":
            run = True
        elif match == "don't()":
            run = False
        elif run:
            s += eval(match)
    print(s)


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])