import random
import numpy as np
from os import system
#dup2
def toss():
    p1 = ''
    p2 = ''
    while p1 == '' or p2 == '':
        system('cls')
        p1 = input('Player 1 choose a name: ')
        p2 = input('Player 2 choose a name: ')
    n = int(input(f'{p1} choose a number: '))%2
    r = np.random.randint(100)%2
    print('')
    if n == r:
        print(f'{p1} wins the toss')
        return p1,p2
    else:
        print(f'{p2} wins the toss')
        return p2,p1
#vfork




#mount_ifs
