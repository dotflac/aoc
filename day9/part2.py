from itertools import combinations
import sys

PREAMBLE = 25

with open('input.txt') as f:
    data = list(map(int, f.read().strip().split('\n')))

for index, num in enumerate(data):
    if index < PREAMBLE:
        continue
    window = data[(index - PREAMBLE):index]
    sums = list(map(sum, combinations(window, 2)))
    if num not in sums:
        invalid_num = num
        break

for index in range(len(data)):
    sum_ = 0
    range_ = 2
    while sum_ < invalid_num:
        window = data[index:index + range_]
        sum_ = sum(window)
        if sum_ == invalid_num:
            print(min(window) + max(window))
            sys.exit()
        range_ += 1