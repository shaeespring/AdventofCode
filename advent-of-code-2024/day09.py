from opener import opener
import re


def expander(line):
    expanded = []
    files = []
    freespace = []
    count = 0
    new=[]
    for i in range(len(line)):
        if i % 2 == 0:
            files.append(line[i])
        else:
            freespace.append(line[i])

    for i in range(len(freespace)):
        num_of_dots = int(freespace[i])
        nums = int(files[i])
        numcomb = list()
        for num in range(nums):
            numcomb.append(str(count))
        expanded.append(numcomb)
        new.append(numcomb)
        
        expanded.append(num_of_dots)
        count += 1
    if len(files) > len(freespace):
        last = int(files[-1])
        numcomb = list()
        for num in range(last):

            numcomb.append( str(count))
        expanded.append(numcomb)
        new.append(numcomb)

    return expanded, new


    



def compactor(expanded,new):
    
    new.reverse()
    print(new)
    count = 0 
    stopper = len(expanded)
    for num in range(len(new)):
        
            length = len(new[num])
            
            index = next((i for i, x in enumerate(expanded) if isinstance(x,int) and x>=length),None)
            if index != None and index<expanded.index(new[num]):
                ind = expanded.index(new[num])
                expanded[index] -= length
                expanded.insert(index,new[num])
                
                expanded.pop(ind+1)
                expanded.insert(ind+1,length)
                
                
            
            
    else:


        return expanded

def done(compacted):
    final = list()
    
    for num in compacted:
        
        if type(num) == list:
            for val in num:
                final.append(val)
            
        
        else:
            for ber in range(num):
                final.append( ".")
        
        
    return final
    


def checksum(compacted):
    summation = 0
    count = 0
    for i in range(len(compacted)):
        if compacted[i] != ".":
                summation += i * int(compacted[i])
                count += 1
    return summation


def main():

    line = opener("day9.txt")
    print(len(line), ":LINE")

    expanded, new = expander(str(line))
    print((expanded), ":EXPAND")

    compacted = compactor(expanded,new)
    print("here")
    print(compacted)
    print(len(compacted), ":COMPACT")
    stringer = done(compacted)
    print(stringer)
    summ = checksum(stringer)
    print(summ)


main()
