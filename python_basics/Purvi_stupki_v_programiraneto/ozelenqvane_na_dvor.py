square_meters_for_greening = float(input())
price_for_greening_the_whole_yard = square_meters_for_greening * 7.61
discount_for_greening_the_whole_yard = price_for_greening_the_whole_yard * 0.18
final_price_for_greening_the_whole_yard = price_for_greening_the_whole_yard - discount_for_greening_the_whole_yard

print(f'The final price is: {final_price_for_greening_the_whole_yard} lv.')
print(f'The discount is: {discount_for_greening_the_whole_yard} lv.')
