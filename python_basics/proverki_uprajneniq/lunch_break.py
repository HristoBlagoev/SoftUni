from math import ceil

movie_name = input()
duration_episode = int(input())
duration_break = int(input())
difference = 0

lunch_time = duration_break / 8
free_time = duration_break / 4

left_time = duration_break - lunch_time - free_time

difference = abs(left_time - duration_episode)
difference = ceil(difference)
if duration_episode <= left_time:
    print(f'You have enough time to watch {movie_name} and left with {difference} minutes free time.')
else:
    print(f"You don't have enough time to watch {movie_name}, you need {difference} more minutes.")

