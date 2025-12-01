import re
import math


def pt1_list(filename):
    with open(filename) as file:
        content = file.read()
        pattern = r"mul\(\d+,\d+\)"
        return re.findall(pattern, content)


def pt2_list(filename):
    mullist = []  # to store mul() matches
    do_block = True  # if inside a don't() block

    # pattern for mul({number, number})
    pattern = r"mul\(\d+,\d+\)"

    with open(filename) as file:
        content =file.read()
        # split the string into parts
        parts = re.split(r"(don't\(\)|do\(\))", content)

        for part in parts:
            if "don't()" in part:
                do_block=False
            elif "do()" in part:
                do_block=True
            elif do_block: #neither don't nor do are present, so it's mul
                # collect mul() values only when not inside a don't() block
                mullist.extend(re.findall(pattern, part))

        return mullist

def main():

    pt1_mullist = pt1_list("advent-of-code/data/day3.txt")
    pt2_mullist = pt2_list("advent-of-code/data/day3.txt")

    pt1 = sum(math.prod(map(int, item[4:-1].split(","))) for item in pt1_mullist)
    pt2 = sum(math.prod(map(int, item[4:-1].split(","))) for item in pt2_mullist)
    print(pt1)
    print(pt2)


main()
