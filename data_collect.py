#  @Author: Jake Busse
#  This file is used to run large simulations, specifically for my Bingo Labs project

import csv
import simulate as sim
import patterns
import gspread

def csv_run(file_name, card_low, card_high, iterations, pattern):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(card_low, card_high+1):
            writer.writerow([sim.average_nums_called(i, pattern, iterations)])
            print(f'{round(((i/(card_high+1))*100), 2)}% complete')
    print('CSV File Finished')


def google_sheets_run(spreadsheet_name, worksheet_name, starting_row, column, card_low, card_high, iterations, pattern):
    gc = gspread.oauth()
    spreadsheet = gc.open(spreadsheet_name)
    worksheet = spreadsheet.worksheet(worksheet_name)
    for i in range(card_low, card_high+1):
        worksheet.update_cell(starting_row+i, column, sim.average_nums_called(i, pattern, iterations))
        print(f'{round(((i/(card_high+1))*100), 2)}% complete')
    print('Updated Google Sheets')


google_sheets_run('Bingo Data', 'gspread', 2, 1, 1, 100, 10, patterns.regular)

