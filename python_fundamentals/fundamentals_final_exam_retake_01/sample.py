import re

food_information = input()
pattern = r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, food_information)
total_calories = sum([int(match[3]) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")