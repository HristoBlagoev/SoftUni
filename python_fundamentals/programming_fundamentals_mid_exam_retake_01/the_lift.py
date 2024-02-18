number_of_people = int(input())
state_of_elevators = [int(number) for number in input().split()]
max_people_in_elevator = 4

for current_elevator in range(len(state_of_elevators)):
    can_load = min(max_people_in_elevator - state_of_elevators[current_elevator], number_of_people)
    state_of_elevators[current_elevator] += can_load
    number_of_people -= can_load

if number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
elif len([elevator for elevator in state_of_elevators if elevator < 4]) > 0:
    print('The lift has empty spots!')

print(*state_of_elevators, sep=" ")
