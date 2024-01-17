kg_pratka = float(input())
type = input()
distance = int(input())

if type == 'standard':
    if kg_pratka < 1:
        price_km = 0.03
    elif 1 <= kg_pratka < 10:
        price_km = 0.05
    elif 10 <= kg_pratka < 40:
        price_km = 0.10
    elif 40 <= kg_pratka < 90:
        price_km = 0.15
    elif 90 <= kg_pratka < 150:
        price_km = 0.20

elif type == 'express':
    if kg_pratka < 1:
        price_km = 0.03 + 0.03 * 0.80 * kg_pratka
    elif 1 <= kg_pratka < 10:
        price_km = 0.05 + 0.05 * 0.40 * kg_pratka
    elif 10 <= kg_pratka < 40:
        price_km = 0.10 + 0.10 * 0.05 * kg_pratka
    elif 40 <= kg_pratka < 90:
        price_km = 0.15 + 0.15 * 0.02 * kg_pratka
    elif 90 <= kg_pratka < 150:
        price_km = 0.20 + 0.20 * 0.01 * kg_pratka

price = price_km * distance

print(f"The delivery of your shipment with weight of {kg_pratka:.3f} kg. would cost {price:.2f} lv.")