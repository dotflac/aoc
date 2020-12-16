import itertools

with open('../input.txt') as f:
    numbers = [int(i) for i in f.readlines()]

for x, y in itertools.combinations(numbers, 2):
    if x + y == 2020:
        print(f'{x} + {y} == 2020')
        print(f'{x} * {y} == {x * y}')
        break