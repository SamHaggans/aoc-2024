import random
import sys
from dataclasses import dataclass
import graphlib

def topological_sort(dag):
    ts = graphlib.TopologicalSorter()
    for node, dependencies in dag.items():
        ts.add(node, *dependencies)
    return list(ts.static_order())

def part1(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")

    rules: dict[int, set] = dict()
    getting_rules = True
    mids = []
    for line in lines:
        if getting_rules:
            if len(line) < 2:
                getting_rules = False
                continue
            first, second = [int(x) for x in line.split("|")]
            if first not in rules:
                rules[first] = set()
            rules[first].add(second)
        else:
            brk = False
            seen = set()
            nums = [int(x) for x in line.split(",")]
            for num in nums:
                if num in rules and any(see in rules[num] for see in seen):
                    brk = True
                seen.add(num)
            if brk:
                continue
            mids.append(nums[len(nums)//2])
    
    print(sum(mids))
    
def check_nums(nums, rules):
    brk = True
    seen = set()
    for num in nums:
        if num in rules and any(see in rules[num] for see in seen):
            brk = False
        seen.add(num)
    return brk

def part2(file: str):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    rules: dict[int, set] = dict()
    getting_rules = True
    mids = []
    bad_lines = []
    for line in lines:
        if getting_rules:
            if len(line) < 2:
                getting_rules = False
                continue
            first, second = [int(x) for x in line.split("|")]
            if first not in rules:
                rules[first] = set()
            rules[first].add(second)
        else:
            brk = False
            seen = set()
            nums = [int(x) for x in line.split(",")]
            for num in nums:
                if num in rules and any(see in rules[num] for see in seen):
                    brk = True
                seen.add(num)
            if brk:
                bad_lines.append(nums)
    
    for nums in bad_lines:
        rules_copy = {k: v for k, v in rules.items() if k in nums}
        for k, v in rules_copy.items():
            rules_copy[k] = [x for x in v if x in nums]
        # Topological sort has the rules in the opposite graph direction
        # but apparently reversing it just works
        nums = list(reversed(topological_sort(rules_copy)))
        print(f"{nums} in corrected order")
        assert check_nums(nums, rules)
        mids.append(nums[len(nums)//2])

    
    print(sum(mids))

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])