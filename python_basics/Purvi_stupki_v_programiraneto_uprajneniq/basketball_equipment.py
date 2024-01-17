annual_fee_for_basketball = int(input())

price_snickers = annual_fee_for_basketball * 0.60
price_outfit = price_snickers * 0.80
price_ball = price_outfit / 4
price_accessories = price_ball / 5

total_price = annual_fee_for_basketball + price_snickers + price_outfit + price_ball + price_accessories

print(total_price)