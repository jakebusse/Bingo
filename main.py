# @Author Jake Busse
"""
This file 'main.py' is a free file to test and play around with other functions and files. Nothing important here.
"""

from card import *
from game import *
from patterns import *

def card_test():
    card = create_card()
    display_card(card)
    pattern = [[-1, 0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, -1]]
    for i in range(1, 76, 2):
        daub_number(card, i)
    display_card(card)
    print(check_card(card, pattern))


def game_test():
    print(call_number())


cards = []
for i in range(2):
    cards.append(create_card())
game = slow_play(cards, regular)
print(f"Card  {cards.index(game['winning_card'])} won in {game['nums_called']} calls.")