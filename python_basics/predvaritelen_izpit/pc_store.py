price_per_processor_in_usd = float(input())
price_per_video_card_in_usd = float(input())
price_per_ram_memory_in_usd = int(input())
qty_of_ram_memory = float(input())
discount_in_percent = float(input())

price_processor_in_bgn = price_per_processor_in_usd * 1.57
price_video_card_in_bgn = price_per_video_card_in_usd * 1.57
price_ram_memory_in_bgn = price_per_ram_memory_in_usd * qty_of_ram_memory * 1.57

final_price_processor = price_processor_in_bgn - price_processor_in_bgn * discount_in_percent
final_price_video_card = price_video_card_in_bgn - price_video_card_in_bgn * discount_in_percent
total_price = final_price_video_card + final_price_processor + price_ram_memory_in_bgn

print(f"Money needed - {total_price:.2f} leva.")