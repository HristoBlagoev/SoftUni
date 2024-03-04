shopping_list = {
    "foods": {"nuts": "almonds"},
    "drinks": {"soft": "lemonade", "wine": "merlot"}
}

for key, value in shopping_list.items():
    for current_key, current_value in value.items():
        print(f'{current_value} bought')
        shopping_list[key][current_key] = 'bought'
