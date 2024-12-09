import sys

operators = ["*", "+", "* 10 +"]

def translate_operators(binary_value, values):
    result = values[0]
    assert len(binary_value) == len(values) - 1
    for char, val in zip(binary_value, values[1:]):
        binar = int(char)
        operators[2] = f"* {10 ** len(str(val)) } +"
        result = eval("".join([str(result), operators[binar], str(val)]))
    return result

def decimal_to_ternary(n):
  """Converts a decimal number to ternary."""

  if n == 0:
    return "0"

  result = ""
  while n > 0:
    n, remainder = divmod(n, 3)
    result = str(remainder) + result

  return result

def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    goods = 0
    for line in lines:
        ans = int(line.split(":")[0])
        vals = line.split(":")[1]
        values = [int(val.strip()) for val in vals.split()]
        bits = len(values) - 1
        max_val = 2 ** bits
        for i in range(max_val):
            bin_string = str(format(i, '030b'))[-bits:]
            if ans == translate_operators(bin_string, values):
                goods += ans
                print(f"{line} is good: {i}")
                break
        print(goods)
                

def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    goods = 0
    for line in lines:
        ans = int(line.split(":")[0])
        vals = line.split(":")[1]
        values = [int(val.strip()) for val in vals.split()]
        bits = len(values) - 1
        max_val = 3 ** bits
        for i in range(max_val):
            bin_string = decimal_to_ternary(i).zfill(bits + 10)[-bits:]
            if ans == translate_operators(bin_string, values):
                goods += ans
                print(f"{line} is good: {i}")
                break
    print(goods)


if __name__ == "__main__":
    part1(sys.argv[1])
    print("PART2")
    part2(sys.argv[1])