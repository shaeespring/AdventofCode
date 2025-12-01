from opener import opener
import functools

def rules(rock):

    if int(rock) == 0:
        return str(1)
    elif len(rock) % 2 == 0:
        split = int(len(rock) / 2)
        rock1 =rock[:split] 
        rock2 = rock[split:] 
        try:
            if rock2.index("0") == 0 and len(rock2)>1:
                for char in rock2:
                    if char != "0":
                        rock2 = rock2[rock2.index(char):]
                        return rock1 + " " + rock2
                    
                return rock1 + " " + "0"
            return rock1 + " " + rock2
        except ValueError:
            return rock1 + " " + rock2
    else:
        return str(int(rock) *2024)


def recursion(rocks,num=0,final=[]):
    if num == 75:
        rocks = rocks.strip().split()
        for ro in rocks:
            final.append(ro)
        return rocks
    rocks = rocks.strip().split()

    for rock in rocks:
        r = recursion(rules(rock),num+1,final)
        
    return final
        
    




def main():
    after_rules = list()
    line = opener("day11.txt")
    line = line.strip().split(" ") 
    for rock in line:
        r=recursion(rock,0,[])
        for ro in r:
            after_rules.append(ro)
        
    print(len(after_rules))
main()
