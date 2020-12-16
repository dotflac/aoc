from itertools import combinations

PREAMBLE = 25

with open('input.txt') as f:
    data = list(map(int, f.read().strip().split('\n')))

for index, num in enumerate(data):
    if index < PREAMBLE:
        continue
    slice = data[(index - PREAMBLE):index]
    sums = list(map(sum, combinations(slice, 2)))
    if num not in sums:
        print(num)
        break