#!/usr/bin/env python3
import random

fortunes_generator = (row for row in open("fortunes"))
num_quotes = 2909
stop = random.randint(0, num_quotes)
quote_index = 0

quote = ""
quoteline = 0
for row in fortunes_generator:
    if row.find("%") != -1:
        quote_index += 1
    if quote_index == stop:
        if quoteline > 0:
            quote += row
        quoteline += 1
    if quote_index == stop + 1:
        print(quote)
        break
