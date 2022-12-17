import random
import datetime

from quotes import quotes


def generate_quote():
    last_day = None  # Variable global
    index_quote = -1  # Variable global

    if last_day != datetime.datetime.now().day:
        last_index = index_quote
        while index_quote == last_index:
            index_quote = random.randint(0, len(quotes) - 1)
        last_day = datetime.datetime.now().day

    return(quotes[index_quote])
