import random
import datetime

from quotes import quotes

last_day = None

if last_day != datetime.datetime.now().day:
    index_quote = random.randint(0, len(quotes) - 1)
    last_day = datetime.datetime.now().day

print(quotes[index_quote])
