price_maiden_party = float(input())
qty_love_letters = int(input())
qty_wax_roses = int(input())
qty_key_chains = int(input())
qty_cartoons = int(input())
qty_good_luck_surprise = int(input())

total_qty = qty_love_letters + qty_wax_roses + qty_key_chains + qty_cartoons + qty_good_luck_surprise

price_love_letters = qty_love_letters * 0.60
price_wax_roses = qty_wax_roses * 7.20
price_key_chains = qty_key_chains * 3.60
price_cartoons = qty_cartoons * 18.20
price_good_luck_surprise = qty_good_luck_surprise * 22.00
total_price = price_love_letters + price_wax_roses + price_key_chains + price_cartoons + price_good_luck_surprise

if total_qty >= 25:
    total_price *= 0.65

final_price_after_taxes = total_price * 0.90
difference = abs(final_price_after_taxes - price_maiden_party)

if final_price_after_taxes >= price_maiden_party:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
