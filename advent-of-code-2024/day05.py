from collections import defaultdict


def opener(filename):
    rules = defaultdict(list)
    lines = []
    with open(filename) as file:
        for line in file:
            if "|" in line:
                rule = line.strip().split("|")
                rules[rule[0]].append(rule[1])
            elif line != "\n":
                lines.append(line.strip().split(","))
    return rules, lines


def sort_for_pt_2(rules, line):
    for key in range(0, len(line)):
        for value in range(key + 1, len(line)):
            if line[value] not in rules[line[key]]:
                line[key], line[value] = line[value], line[key]
                sort_for_pt_2(rules, line)

    return int(line[len(line) // 2])


def main():
    rules, lines = opener("inputfile.txt")
    pt1 = 0
    pt2 = 0
    for line in lines:
        correct_order = True
        for i, key in enumerate(line):
            for value in range(i + 1, len(line)):
                if line[value] not in rules[key]:
                    correct_order = False
            if not correct_order:
                pt2 += sort_for_pt_2(rules, line)
                break
        if correct_order:
            pt1 += int(line[len(line) // 2])
    print(pt1)
    print(pt2)


main()
