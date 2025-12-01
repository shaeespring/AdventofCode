from arrayer import arrayer
from opener import opener


def findall(x,y,a,section=set()):
    
    char = a[x][y]
    section.add((x,y)
    )
    print(x,y)
    print(char)
    if a[x+1][y] == char:
        if x<len(a)-2:
            
            
            pos = (x+1,y)
            if pos not in section:
                
                findall(x+1,y,a,section)
    if a[x][y+1] == char:
        
        if y<len(a)-2:
            print("here")
            pos = (x,y+1)
            if pos not in section:
                
                findall(x,y+1,a,section)
    
    return section , x , y
        
    


    
def area_build(a,x=0,y=0):
    completed_pos = set()
    pos = (x, y)
    if pos not in completed_pos:
        section ,dont,use= findall(x,y,a)
        for pose in section:
            completed_pos.add(pose)
    print(completed_pos)
    if x<len(a)-1:
        area_build(a,x+1,y)
    if y<len(a)-1:
        area_build(a,x,y+1)



def main():
    a = opener("day12_little.txt")
    area = area_build(a)


main()
