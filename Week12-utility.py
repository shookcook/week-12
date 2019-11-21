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
