# @Author Jake Busse
"""
This file 'card.py' is used to create randomized BINGO cards, display them in the console in a 'human-friendly'
way, daub numbers once they are called (see 'game.py'), and check cards for wins.
"""

import random


def create_card():
    """
    Returns a list of 5 lists, each list will contain 5 random numbers associated with the letter.
    """
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    i = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    n = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    g = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    o = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
    nums = [b, i, n, g, o]
    card = [[], [], [], [], []]
    for letter in range(5):
        for pos in range(5):
            rand_index = random.randint(0, len(nums[letter])-1)
            num = nums[letter][random.randint(0, rand_index)]
            nums[letter].remove(num)
            card[letter].append(num)
    card[2][2] = -1
    return card


def display_card(card):
    """
    Prints card to console
    :param card:
    """
    print('B  I  N  G  O')
    for i in range(5):
        for letter in card:
            if 0 < letter[i] < 10:
                print(letter[i], end='  ')
            else:
                print(letter[i], end=' ')
        print()
    print('---------')


def daub_number(card, num):
    """
    Takes card and number to daub, searches card for number and changes it to '-1' if it is present to signify a
    daubed number.
    :param card:
    :param num:
    """
    letter = None
    index = None
    if num <= 15 and num in card[0]:
        letter = 0
        index = card[0].index(num)
    elif num <= 30 and num in card[1]:
        letter = 1
        index = card[1].index(num)
    elif num <= 45 and num in card[2]:
        letter = 2
        index = card[2].index(num)
    elif num <= 60 and num in card[3]:
        letter = 3
        index = card[3].index(num)
    elif num <= 75 and num in card[4]:
        letter = 4
        index = card[4].index(num)
    if letter and index:
        card[letter][index] = -1


def check_card(card, pattern):
    """
    Takes card and list signifying a pattern of a valid BINGO. This function finds the indexes of daubed numbers on
    the valid bingo and searches each 'winning' spot on the player card. If the player card matches the winning card,
    True is returned. If the winning card does not match, False is returned.
    :param card:
    :param pattern:
    :return:
    """
    pattern_indexes = [[], [], [], [], []]
    pattern_count = 0
    for letter in range(len(pattern)):
        for pos in range(len(pattern[letter])):
            if pattern[letter][pos] == -1:
                pattern_indexes[letter].append(pos)
                pattern_count += 1
    card_count = 0
    for letter in range(len(pattern_indexes)):
        for pos in range(len(pattern_indexes[letter])):
            if card[letter][pattern_indexes[letter][pos]] == -1:
                card_count += 1
    if pattern_count == card_count:
        return True
    else:
        return False


def check_multiple_patterns(card, patterns):
    """
    Takes in card and a list of patterns and uses check_card to check each pattern and returns True if at least ONE
    of the patterns is met, otherwise returns False
    :param card:
    :param patterns:
    :return:
    """
    for pattern in patterns:
        result = check_card(card, pattern)
        if result:
            return True
    return False
