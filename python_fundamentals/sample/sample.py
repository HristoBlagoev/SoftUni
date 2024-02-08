employees = input().split()
happiness_factor = int(input())

employee = list(map(lambda x: int(x) * happiness_factor, employees))

filtrated = list(filter(lambda x: x >= (sum(employee)) / (len(employees)), employees))

if len(filtrated) >= len(employees) / 2:
    print(f"Score: {len(filtrated)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtrated)}/{len(employees)}. Employees are not happy!")