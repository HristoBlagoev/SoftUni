from math import pi

figure = (input())
area = 0

if figure == 'square':
    a = float(input())
    area = a * a
if figure == 'rectangle':
        a = float(input())
        b = float(input())
        area = a * b
if figure == 'circle':
    r = float(input())
    area = pi * r ** 2
if figure == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b * 0.5

print(f'{area:.3f}')
