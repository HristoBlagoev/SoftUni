price_per_kg_vegetables = float(input())
price_per_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

price_vegetables = price_per_kg_vegetables * total_kg_vegetables
price_fruits = price_per_kg_fruits * total_kg_fruits
total = price_vegetables + price_fruits
total_in_euro = total / 1.94

print(' \n %.2f ' % total_in_euro)
