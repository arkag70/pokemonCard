#copyright lines

#imports
from toss import *
from dealing import *
from game import *
ch= 'y'

while ch.lower() == 'y':
    p1,p2 = toss()
    d1,d2 = randomizeCards()
    game(p1,p2,d1,d2)
    inp = input('About to Exit...play another round (y/n)? ')
    if inp.lower() == 'n':
        break
