#METHOD USED
#Dylan Cook
#CSCI 102 – Section E
#Week 12 - Part A

def PrintOutput(statement):
    d = statement
    print(d)


def LoadFile(file):
    a = open(file, 'r')
    b = a.read()
    c = b.split('\n')
    print(c) 


def UpdateString(word, letter, num):
    a = list(word)
    a[num] = letter
    new_word = ''.join(a)
    print(new_word)
