# @Author Jake Busse

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
    prints card to console
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
    for letter in card:
        if num in letter:
            letter[letter.index(num)] = -1

def check_card(card, pattern):
    

card = create_card()
display_card(card)
for i in range(75):
    daub_number(card, i)
display_card(card)