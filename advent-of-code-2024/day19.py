def opener():
    sum = 0
    with open("day19_little.txt") as file:
        
        for line in file:
            if "," in line:
                rules = line.strip().split(",")

            longest = rules[0]
            for rule in rules:
                if len(rule) > len(longest):
                    longest = rule

                    
            print(rules)
            print(longest)
            line = line.strip()
            if line_check(line,rules,len(longest)):
                sum += 1
        print(sum)

def line_check(line,rules,longest,i=0):
    print("here")
    if i == len(line)-1:
        return True
    if line[i] in rules:
        line_check(line, rules, i+1)
    while longest != 0:
        longest-=1
        if line[i:longest] in rules:

            line_check(line,rules,longest-1,i+longest)
        
    
            

    

opener()
            

        

