# @Author: Jake Busse
#  This file 'simulate.py' simulates different variations of BINGO games and returns data used for statistical analysis
#  (see individual functions)
from card import *
from game import *
from patterns import *


def average_nums_called(num_cards, pattern, iterations):
    """
    This function calculates the average number of balls called before a valid bingo occurs over a provided number of
    iterations, for a specified number of cards, and for a specified pattern.
    :param cards:
    :param pattern:
    :param iterations:
    :return:
    """
    all_nums_called = []
    for i in range(iterations):
        cards = []
        calls = []
        nums_called = 0
        win = False
        for j in range(num_cards):
            cards.append(create_card())
        while not win:
            calls = call_number(calls)
            call = calls[-1]
            nums_called += 1
            for card in cards:
                daub_number(card, call)
            for card in cards:
                if check_card(card, pattern):
                    win = True
        all_nums_called.append(nums_called)
    avg_nums_called = sum(all_nums_called)/len(all_nums_called)
    return avg_nums_called
