city = input()
volume_of_sales = float(input())
commission = 0
is_input_valid = True

if city == 'Sofia':
    if 0 <= volume_of_sales <= 500:
        commission = volume_of_sales * 0.05
    elif 500 < volume_of_sales <= 1000:
        commission = volume_of_sales * 0.07
    elif 1000 < volume_of_sales <= 10000:
        commission = volume_of_sales * 0.08
    elif volume_of_sales > 10000:
        commission = volume_of_sales * 0.12
    else:
        is_input_valid = False
elif city == "Varna":
    if 0 <= volume_of_sales <= 500:
        commission = volume_of_sales * 0.045
    elif 500 < volume_of_sales <= 1000:
        commission = volume_of_sales * 0.075
    elif 1000 < volume_of_sales <= 10000:
        commission = volume_of_sales * 0.10
    elif volume_of_sales > 10000:
        commission = volume_of_sales * 0.13
    else:
        is_input_valid = False
elif city == "Plovdiv":
    if 0 <= volume_of_sales <= 500:
        commission = volume_of_sales * 0.055
    elif 500 < volume_of_sales <= 1000:
        commission = volume_of_sales * 0.08
    elif 1000 < volume_of_sales <= 10000:
        commission = volume_of_sales * 0.12
    elif volume_of_sales > 10000:
        commission = volume_of_sales * 0.145
    else:
        is_input_valid = False
else:
    is_input_valid = False

if not is_input_valid:
    print('error')
else:
    print(f'{commission:.2f}')