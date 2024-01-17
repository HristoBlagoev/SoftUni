days_off = int(input())

days_off_play = days_off * 127
working_days_play = (365 - days_off) * 63

total_play_time_in_min = days_off_play + working_days_play
difference = abs(30000 - total_play_time_in_min)
play_time_in_hours = difference // 60
play_time_in_minutes = difference % 60
if total_play_time_in_min > 30000:
    print('Tom will run away')
    print(f'{play_time_in_hours} hours and {play_time_in_minutes} minutes more for play')
elif total_play_time_in_min < 30000:
    print('Tom sleeps well')
    print(f'{play_time_in_hours} hours and {play_time_in_minutes} minutes less for play')
