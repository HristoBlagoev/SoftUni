from math import floor

qty_of_processors = int(input())
qty_workers = int(input())
working_days = int(input())

total_working_hours = qty_workers * working_days * 8
produced_processors = floor(total_working_hours / 3)

difference = abs(produced_processors - qty_of_processors)
price = difference * 110.10

if produced_processors >= qty_of_processors:
    print(f'Profit: -> {price:.2f} BGN')
if produced_processors < qty_of_processors:
    print(f'Losses: -> {price:.2f} BGN')