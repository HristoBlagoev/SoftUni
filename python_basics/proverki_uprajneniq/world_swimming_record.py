record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1_meter = float(input())
difference = 0

time_needed = distance_in_meters * time_in_seconds_for_1_meter
delay_distance = distance_in_meters // 15
delay_time = delay_distance * 12.5
resistance = (distance_in_meters / 15) * 12.5

total_time_needed = time_needed + delay_time

difference = abs(record_in_seconds - total_time_needed)

if total_time_needed < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time_needed:.2f} seconds.')
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")