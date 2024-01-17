kg_parcel = float(input())
type_of_delivery = input()
distance = int(input())
final_price_standard = 0
final_price_express = 0
price_express = 0
price_standard = 0
if type_of_delivery == 'standard':
    if kg_parcel < 1:
        price_standard = 0.03
    elif 1 <= kg_parcel < 10:
        price_standard = 0.05
    elif 10 <= kg_parcel < 40:
        price_standard = 0.10
    elif 40 <= kg_parcel < 90:
        price_standard = 0.15
    elif 90 <= kg_parcel < 150:
        price_standard = 0.20
    final_price_standard = price_standard * distance

elif type_of_delivery == 'express':
    if kg_parcel < 1:
        price_express = 0.03 + 0.03 * 0.80 * kg_parcel
    elif 1 <= kg_parcel < 10:
        price_express = 0.05 + 0.05 * 0.40 * kg_parcel
    elif 10 <= kg_parcel < 40:
        price_express = 0.10 + 0.10 * 0.05 * kg_parcel
    elif 40 <= kg_parcel < 90:
        price_express = 0.15 + 0.15 * 0.02 * kg_parcel
    elif 90 <= kg_parcel < 150:
        price_express = 0.20 + 0.20 * 0.01 * kg_parcel
    final_price_express = price_express * distance


if type_of_delivery == 'standard':
    print(f'The delivery of your shipment with weight of {kg_parcel:.3f} kg. would cost {final_price_standard:.2f} lv.')
elif type_of_delivery == 'express':
    print(f'The delivery of your shipment with weight of {kg_parcel:.3f} kg. would cost {final_price_express:.2f} lv.')