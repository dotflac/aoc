with open('input.txt') as f:
    adapters = sorted([int(i) for i in f.readlines()])

MAX_DIFF = 3

def solve(chain):
    if len(chain) == 1:
        return chain
    
    head = chain[0]
    tail = chain[1:]
    
    i = 0
    while True:
        if tail[i] - head > MAX_DIFF:
            return None
        if (valid_chain := solve(tail)):
            return [head] + valid_chain
        i += 1

valid_chain = solve(adapters)
valid_chain = [0] + valid_chain + [max(valid_chain) + 3]

count_1j = count_3j = 0

for i in range(len(valid_chain) - 1):
    if valid_chain[i + 1] - valid_chain[i] == 1:
        count_1j += 1
    elif valid_chain[i + 1] - valid_chain[i] == 3: 
        count_3j += 1

print(count_1j, count_3j)
print(count_1j * count_3j)