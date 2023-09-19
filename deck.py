#!python3
import random


ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['C','D','H','S']

clubs = [(i + "C") for i in ranks]
diamonds = [(i + "D") for i in ranks]
hearts = [(i + "H") for i in ranks]
spades = [(i + "S") for i in ranks]
all = [clubs, diamonds, hearts, spades]
all = [i for i in (clubs + diamonds + hearts + spades)]
def gethand():
    global all
    hand = []
    for i in range(5):
        hand1 = all[random.randint(0, len(all)-1)]
        all.pop(all.index(hand1))
        hand.append(hand1)
    return(hand)
print(gethand())
print(gethand())
    


