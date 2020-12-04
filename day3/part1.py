LINE_LEN = 31
import math

all_counts = []

pos = 0
tree_count = 0
with open('input.txt') as f:
    for line in f:
        if line[pos] == '#':
            tree_count += 1
        pos = (pos + 3) % LINE_LEN
print('right 3 down 1', tree_count)
all_counts.append(tree_count)

pos = 0
tree_count = 0
with open('input.txt') as f:
    for line in f:
        if line[pos] == '#':
            tree_count += 1
        pos = (pos + 1) % LINE_LEN
print('right 1 down 1', tree_count)
all_counts.append(tree_count)

pos = 0
tree_count = 0
with open('input.txt') as f:
    for line in f:
        if line[pos] == '#':
            tree_count += 1
        pos = (pos + 5) % LINE_LEN
print('right 5 down 1', tree_count)
all_counts.append(tree_count)

pos = 0
tree_count = 0
with open('input.txt') as f:
    for line in f:
        if line[pos] == '#':
            tree_count += 1
        pos = (pos + 7) % LINE_LEN
print('right 7 down 1', tree_count)
all_counts.append(tree_count)

pos = 0
tree_count = 0
skip_next = False
with open('input.txt') as f:
    for line in f:
        if skip_next == True:
            print('skipping, pos', pos)
            skip_next = not skip_next
            continue
        if line[pos] == '#':
            tree_count += 1
        print(line[pos])
        pos = (pos + 1) % LINE_LEN
        skip_next = not skip_next
print('right 1 down 2', tree_count)
all_counts.append(tree_count)

print(math.prod(all_counts))