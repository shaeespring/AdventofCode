def create_lists(filename):
    with open(filename) as file:
        list1 = list()
        list2 = list()
        for line in file:
            line = line.strip().split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))
        return list1, list2


def main():
    list1, list2 = create_lists("inputfile.txt")
    pt2 = sum(list2.count(list1[i])*list1[i] for i in range(len(list1)))
    list1.sort()
    list2.sort()
    #list1 and list2 are always going to be the same length, so the min part is a little unnecessary...
    pt1 = sum(abs(list1[i]-list2[i]) for i in range(min(len(list1),len(list2))))
    print(pt1)
    print(pt2)

main()
