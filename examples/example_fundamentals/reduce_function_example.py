from functools import reduce
list = [1, 3, 5, 6, 2]
sum = reduce(lambda a, b: a + b, list) # 17
max = reduce(lambda a, b: a if a > b else b, list)