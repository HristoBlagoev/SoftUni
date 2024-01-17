budget = float(input())
number_video_card = int(input())
number_processor = int(input())
number_ram_memory= int(input())
difference = 0

price_video_card = number_video_card * 250.00
price_per_processor = price_video_card * 0.35
price_processor = number_processor * price_per_processor
price_per_ram_memory = price_video_card * 0.10
price_ram_memory = number_ram_memory * price_per_ram_memory
total_price = price_video_card \
              + price_processor \
              + price_ram_memory

if number_video_card > number_processor:
    total_price *= 0.85

difference = abs(total_price - budget)

if total_price <= budget:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
