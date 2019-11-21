#METHOD USED
#Dylan Cook
#CSCI 102 – Section E
#Week 12 - Part A

def PrintOutput(statement):
    d = statement
    print('OUTPUT', d)


def LoadFile(file):
    a = open(file, 'r')
    b = a.read()
    c = b.split('\n')
    PrintOutput(c) 


def UpdateString(word, letter, num):
    a = list(word)
    a[num] = letter
    new_word = ''.join(a)
    PrintOutput(new_word)


def FindWordCount(mylist, mystring):
    a = 0
    for i in mylist:
        a += i.count(mystring)
    PrintOutput(a)


def ScoreFinder(list1, list2, string):
    a = 0
    for i in list1:
        if i.lower() == string.lower():
            print(string, 'got a score of', list2[list1.index(i)])
            a += 1
    if a == 0:
        PrintOutput('player not found')


def Union(list1, list2):
    newlist = list1 + list2
    PrintOutput(newlist)


def Intersection(list1, list2):
    newlist= []
    for i in list1:
        for a in list2:
            if i.lower() == a.lower():
                newlist.append(i)
    PrintOutput(newlist)
















