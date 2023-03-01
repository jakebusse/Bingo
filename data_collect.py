#  @Author: Jake Busse
#  This file is used to run large simulations, specifically for my Bingo Labs project

import csv
import simulate as sim
import patterns

file_name = 'test.csv'
card_low = 1
card_high = 500
iterations = 1000
pattern = patterns.regular

with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(card_low, card_high+1):
        writer.writerow([sim.average_nums_called(i, pattern, iterations)])
        print(f'{round(((i/(card_high+1))*100), 2)}% complete')
print('CSV File Finished')