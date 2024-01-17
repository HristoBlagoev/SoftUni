'''
a = 1
while a < 11:
    print(a)
    a += 2
-----------------
'''
''''
number_of_interactions = 5

while number_of_interactions > 0:
    print('Hello SoftUni')
    number_of_interactions -= 1
--------------
'''
'''
a = 5
while a <= 10:
    print('a = ' + str(a))
    a +=1
---------------
'''
'''
line = input()

while line != 'Stop':
    print(line)

    line = input()
--------------------
'''

while True:
    line = input()

    if line == 'Stop':
        break

    print(line)