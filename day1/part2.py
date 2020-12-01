# curl -o part1_input.txt --cookie "session=YOUR_SESSION" https://adventofcode.com/2020/day/1/input
import itertools

with open('part1_input.txt') as f:
    numbers = {int(i.strip()) for i in f.readlines()}

for x, y, z in itertools.permutations(numbers, 3):
    if x + y + z == 2020:
        print(f'{x} + {y} + {z} == 2020')
        print(f'{x} * {y} * {z} == {x * y * z}')
        break
