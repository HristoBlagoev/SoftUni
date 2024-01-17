price_per_kilo_mackerel = float(input())
price_per_kilo_sprinkle = float(input())
price_per_kilo_bonito = price_per_kilo_mackerel + price_per_kilo_mackerel * 0.60
price_per_kilo_safrid = price_per_kilo_sprinkle + price_per_kilo_sprinkle * 0.80
price_per_kilo_mussels = 7.50

kg_bonito = float(input())
kg_safrif = float(input())
kg_mussles = int(input())

price_for_bonito = price_per_kilo_bonito * kg_bonito
price_for_safrid = price_per_kilo_safrid * kg_safrif
price_for_mussles = price_per_kilo_mussels * kg_mussles
total_price = price_for_mussles + price_for_safrid + price_for_bonito

print(' %.2f ' % total_price)





