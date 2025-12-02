import opener

FILENAME="data/daytwo"


def ptone(lines):
    total = 0
    for line in lines:
        line = line.split("-")
        st = int(line[0])
        end = int(line[1])
        for i in range(st,end+1):
            s = str(i)
            if  s[:len(s)//2] ==  s[len(s)//2:]:
                    total += i
    return total

def pttwo(lines):
    total = 0
    for line in lines:
        line = line.split("-")
        st,end = int(line[0]), int(line[1])
        for i in range(st,end+1):
            s = str(i)
            for j in range(2,len(s)+1):
                pattern = s[:len(s)//j]
                lengthof = int(len(s)/len(pattern))

                if s == pattern*lengthof:
                    total += i
                    break
    return total
def main():
    lines = opener.opener(FILENAME,",")

    print(ptone(lines))
    print(pttwo(lines))

main()