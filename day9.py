import sys



def parse_to_line(line):
    mode = 0
    # 0 = block mode
    # 1 = empty mode
    count = 0
    results = []
    for char in line:
        if mode == 0:
            for _ in range(int(char)):
                results.append(str(count))
            count += 1
        else:
            
            for _ in range(int(char)):
                results.append(".")
        mode += 1
        mode %= 2
    return results

def move_up(parsed_line):

    front_ptr = 0
    back_ptr = len(parsed_line) - 1
    while not parsed_line[front_ptr] == ".":
        front_ptr += 1
    while parsed_line[back_ptr] == ".":
        back_ptr -= 1
    
    while back_ptr > front_ptr:
        parsed_line[front_ptr] = parsed_line[back_ptr]
        parsed_line[back_ptr] = "."
        while not parsed_line[front_ptr] == ".":
            front_ptr += 1
        while parsed_line[back_ptr] == ".":
            back_ptr -= 1
    return parsed_line

def parse_to_line_p2(line):
    mode = 0
    # 0 = block mode
    # 1 = empty mode
    count = 0
    results = []
    for char in line:
        if mode == 0:
            results.append([str(count), int(char), False])
            count += 1
        else:
            results.append([".", int(char)])
        mode += 1
        mode %= 2
    return results

def move_up_p2(parsed_line):

    back_ptr = len(parsed_line) - 1

    def get_matching_spot(block_length, block_index):
        i = 0
        while i < block_index:
            if parsed_line[i][0] == "." and parsed_line[i][1] >= block_length:
                return i
            i += 1
        return None
            
    
    while back_ptr >= 0:
        potential_block = parsed_line[back_ptr]
        if potential_block[0] != "." and not potential_block[2]:
            check_spot = get_matching_spot(potential_block[1], back_ptr)
            if not check_spot:
                back_ptr -= 1
                continue
            else:
                remaining_length = parsed_line[check_spot][1] - potential_block[1]
                parsed_line.insert(back_ptr + 1, [".", potential_block[1]])
                del parsed_line[back_ptr]
                parsed_line[check_spot][1] = remaining_length
                parsed_line.insert(check_spot, [potential_block[0], potential_block[1], True])
        back_ptr -= 1

    return parsed_line

def checksum(line):
    sm = 0
    count = 0
    for char in line:
        if char == ".":
            continue
        else:
            sm += int(char) * count
            count += 1
    return sm

def checksum_p2(line):
    sm = 0
    count = 0
    for char in line:
        if char[0] == ".":
            count += char[1]
            continue
        else:
            length = char[1]
            for i in range(length):
                sm += int(char[0]) * count
                count += 1
                print(f"Adding {int(char[0]) * count} ({int(char[0])} * {count})")
        
    return sm

def print_p2(line):
    for elem in line:
        print(elem[0] * elem[1], end="")
    print()

def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    line = lines[0]
    parsed = parse_to_line(line)
    print(parsed)
    result = move_up(parsed)
    print(result)
    chk = checksum(result)
    print(chk)

def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    line = lines[0]
    parsed = parse_to_line_p2(line)
    print(parsed)
    result = move_up_p2(parsed)
    print(result)
    print_p2(result)
    chk = checksum_p2(result)
    print(chk)




if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])