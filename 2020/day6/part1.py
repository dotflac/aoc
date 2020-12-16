with open('input.txt') as f:
    # had to add an extra newline to count the final
    # group?? not happy about this :/
    data = f.readlines() + ['\n']

answers = set()
total = 0
for line in data:
    if line.strip():
        for c in line.strip():
            answers.add(c)
    else:
        print(answers)
        total += len(answers) # process group
        answers = set()
print(total)