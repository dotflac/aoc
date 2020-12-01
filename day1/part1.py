# curl -o part1_input.txt --cookie "session=YOUR_SESSION" https://adventofcode.com/2020/day/1/input
import itertools

with open('part1_input.txt') as f:
    numbers = [int(i.strip()) for i in f.readlines()]

for x, y in itertools.combinations(numbers, 2):
    if x + y == 2020:
        print(f'{x} + {y} == 2020')
        print(f'{x} * {y} == {x * y}')
        break
