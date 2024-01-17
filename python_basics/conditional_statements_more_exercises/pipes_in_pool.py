volume_of_pool = int(input())
debit_of_first_pipe_per_hour = int(input())
debit_of_second_pipe_per_hour = int(input())
hours_of_break = float(input())

debit_of_first_pipe = debit_of_first_pipe_per_hour * hours_of_break
debit_of_second_pipe = debit_of_second_pipe_per_hour * hours_of_break
total_debit_of_the_pipes = debit_of_first_pipe + debit_of_second_pipe
difference = abs(volume_of_pool - total_debit_of_the_pipes)

total_percentage_of_the_pipes = total_debit_of_the_pipes / volume_of_pool * 100
percentage_of_first_pipe = debit_of_first_pipe / total_debit_of_the_pipes * 100
percentage_of_second_pipe = debit_of_second_pipe / total_debit_of_the_pipes * 100

if total_debit_of_the_pipes > volume_of_pool:
    print(f'For {hours_of_break} hours the pool overflows with {difference} liters.')
else:
    print(f"The pool is {total_percentage_of_the_pipes}% full. Pipe 1: {percentage_of_first_pipe:.2f}%. Pipe 2: {percentage_of_second_pipe:.2f}%.")