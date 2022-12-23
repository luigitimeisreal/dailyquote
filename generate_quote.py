import random
import datetime

from quotes import quotes

'''
def generate_quote():
    last_day = None  # Variable global
    index_quote = -1  # Variable global

    if last_day != datetime.datetime.now().day:
        last_index = index_quote
        while index_quote == last_index:
            index_quote = random.randint(0, len(quotes) - 1)
        last_day = datetime.datetime.now().day

    return(quotes[index_quote])
'''

def generate_quote():
    # Read the last index
    with open('index.txt') as index_file:
        index_lines = index_file.readlines()
    # Read the last day
    with open('last_day.txt') as last_day_file:
        last_day_lines = last_day_file.readlines()
    # Obtain the variables
    index = int(index_lines[0])
    last_day = int(last_day_lines[0])
    today = datetime.datetime.now().day
    # Change the variables if a day has passed
    if today != last_day:
        if index < len(quotes) - 1:
            index += 1
        else:
            index = 0
        last_day = today
        with open('index.txt', 'w') as index_file:
            index_file.write(str(index))
        with open('last_day.txt', 'w') as last_day_file:
            last_day_file.write(str(last_day))
    
    return quotes[index]

generate_quote()
