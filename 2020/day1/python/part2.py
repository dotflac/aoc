import itertools

with open('../input.txt') as f:
    numbers = [int(i) for i in f.readlines()]

for x, y, z in itertools.combinations(numbers, 3):
    if x + y + z == 2020:
        print(f'{x} + {y} + {z} == 2020')
        print(f'{x} * {y} * {z} == {x * y * z}')
        break
