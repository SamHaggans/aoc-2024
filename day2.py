import sys

def part1(file: str):
    
    with open(file, "r") as f:
        lines = f.read().split("\n")
    success = 0
    for line in lines:
        status = 0 # 0 = unknown, 1 = increasing, 2 = decreasing
        values = [int(x) for x in line.split(" ")]
        start = values[0]
        ok = True
        for nxt in values[1:]:
            if status:
                if nxt - start > 0 and status == 2:
                    ok = False
                    break
                if nxt - start < 0 and status == 1:
                    ok = False
                    break
            else:
                if nxt - start > 0:
                    status = 1
                else:
                    status = 2
            diff = abs(nxt - start)
            if diff > 3 or diff < 1:
                ok = False
                break
            start = nxt
        if ok:
            success += 1
    print(success)

def check_line(values):
    print(f"Checking {values}")
    status = 0 # 0 = unknown, 1 = increasing, 2 = decreasing
    start = values[0]
    ok = True
    for nxt in values[1:]:
        if status:
            if nxt - start > 0 and status == 2:
                ok = False
                break
            if nxt - start < 0 and status == 1:
                ok = False
                break
        else:
            if nxt - start > 0:
                status = 1
            else:
                status = 2
        diff = abs(nxt - start)
        if diff > 3 or diff < 1:
            ok = False
            break
        start = nxt
    return ok

def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    success = 0
    for line in lines:
        values = [int(x) for x in line.split(" ")]
        if any(check_line(values[:x] + values[x+1:]) for x in range(0, len(values))) or check_line(values):
            success += 1
    print(success)


if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])