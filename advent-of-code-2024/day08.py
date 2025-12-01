def arrayer(location=None):
    lines = []
    with open("inputfile.txt") as file:

        for line in file:
            line = line.strip()
            lines.append(line)

        array = []

        for line in lines:
            # iterate over the characters in the line
            inner = []
            for char in line:
                inner.append(char)
            array.append(inner)
        if location != None:
            array[location[0]][location[1]] = "#"
        return array


def hashtags(chars,stopper):  # dictionary , length of array
    count = 0

    list_of_attens = set()
    for letter in chars:
        
        for i in range(len(chars[letter])):
            if len(chars[letter]) != 1:
                list_of_attens.add(chars[letter][i])
            count = 0
            while count != len(chars[letter]):
                if i > 0:

                    distancex = chars[letter][i - count][0] - chars[letter][i][0]
                    distancey = chars[letter][i - count][1] - chars[letter][i][1]
                    multiplier = 1
                    
                    if distancex < 0:
                        while multiplier<stopper:

                                list_of_attens.add(
                                    (
                                        chars[letter][i][0] - (multiplier*distancex),
                                        chars[letter][i][1] - (multiplier*distancey),
                                    )
                                )
                            
                                list_of_attens.add(
                                    (
                                        chars[letter][i - count][0] + (multiplier*distancex),
                                        chars[letter][i - count][1] + (multiplier*distancey),
                                    )
                                )
                                multiplier +=1
                count += 1

    return list_of_attens

"""PART ONE"""
    #def hashtags(chars): #dictionary
    # count = 0

    # list_of_attens = set()
    # for letter in chars:

    #     for i in range(len(chars[letter])):
    #         count = 0
    #         while count != len(chars[letter]):
    #             if i > 0:

    #                 distancex = chars[letter][i - count][0] - chars[letter][i][0]
    #                 distancey = chars[letter][i - count][1] - chars[letter][i][1]

    #                 if distancex < 0:
    #                     if (
    #                         chars[letter][i][0] - distancex,
    #                         chars[letter][i][1] - distancey,
    #                     ) not in chars[letter]:
    #                         list_of_attens.add(
    #                             (
    #                                 chars[letter][i][0] - distancex,
    #                                 chars[letter][i][1] - distancey,
    #                             )
    #                         )
    #                     if (
    #                         chars[letter][i - count][0] + distancex,
    #                         chars[letter][i - count][1] + distancey,
    #                     ) not in chars[letter]:
    #                         list_of_attens.add(
    #                             (
    #                                 chars[letter][i - count][0] + distancex,
    #                                 chars[letter][i - count][1] + distancey,
    #                             )
    #                         )
    #             count += 1

    # return list_of_attens


def remover(hashes, a):
    hashtag_correct = list()
    for hashtag in hashes:
        if hashtag[0] >= 0 and hashtag[0] < len(a):
            if hashtag[1] >= 0 and hashtag[1] < len(a[0]):
                hashtag_correct.append(hashtag)

    print(hashtag_correct)
    return hashtag_correct


def main():
    a = arrayer()
    d = dict()
    for line in a:
        for char in line:
            if char != ".":
                if char in d:
                    d[char].append((a.index(line), line.index(char)))
                else:
                    d[char] = []
                    d[char].append((a.index(line), line.index(char)))
    if len(a) == len(a[0]):
        print("yes")
    hashes = hashtags(d,len(a))
    print(hashes)
    final = remover(hashes, a)
    print(len(final))


main()
