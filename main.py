#copyright lines

#imports
from toss import *
from dealing import *
from game import *

p1,p2 = toss()
d1,d2 = randomizeCards()
game(p1,p2,d1,d2)
