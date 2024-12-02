import sys

def part1(file: str):
    first = []
    second = []
    with open(file, "r") as f:
        lines = f.read().split("\n")
    
    for line in lines:
        for i, num in enumerate(line.split("   ")):
            num = int(num.strip())
            (first, second)[i].append(num)

    first = sorted(first)
    second = sorted(second)

    result = sum(abs(f - s) for f, s in zip(first, second))
    print(result)

def part2(file: str):
    first = []
    second = []
    with open(file, "r") as f:
        lines = f.read().split("\n")
    
    for line in lines:
        for i, num in enumerate(line.split("   ")):
            num = int(num.strip())
            (first, second)[i].append(num)

    # Process right list
    counts = {}
    for elem in second:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1

    similarity = 0
    for elem in first:
        similarity += elem * counts.get(elem, 0)

    print(similarity)


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])