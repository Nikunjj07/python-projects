lst1=["","","O"]
from random import shuffle
def shuffledlst(My_List):
    shuffle(My_List)
    return My_List
shuffledlst(lst1)

def userguess():
    guess =''
    guess = input('Enter a guess: 0, 1, 2: ')
    return int(guess)

def checkans(l,g):
    if l[g] == "O" :
        print('Correct Answer!')
    else:
        print('Wrong Guess!')
checkans(lst1,userguess())

print(lst1)