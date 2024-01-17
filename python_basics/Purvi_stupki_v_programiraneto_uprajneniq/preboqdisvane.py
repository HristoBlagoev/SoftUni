quantity_of_nylon = int(input())
quantity_of_paint = int(input())
quantity_of_thinner = int(input())
hours_work_of_handyman = int(input())

nylon_price = 1.5
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40

materials_price = nylon_price * (quantity_of_nylon +2) \
                  + paint_price * (quantity_of_paint * 1.1) \
                  + thinner_price * quantity_of_thinner \
                  + bags_price
workers_payment = materials_price * 0.3 * hours_work_of_handyman
total_payment = materials_price + workers_payment
print (total_payment)

