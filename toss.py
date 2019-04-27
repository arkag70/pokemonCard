import random
import numpy as np

def toss():

    p1 = input('Player 1 choose a name: ')
    p2 = input('Player 2 choose a name: ')
    n = int(input(f'{p1} choose a number: '))%2
    r = np.random.randint(100)%2
    print('')
    if n == r:
        #print(f'{p1} start')
        return p1,p2
    else:
        #print(f'{p2} start')
        return p2,p1
