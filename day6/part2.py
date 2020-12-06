# spaghetti i'm NOT HAPPY I'M NOT HAPPY WITH THIS

with open('input.txt') as f:
    # had to add an extra newline to count the final
    # group?? not happy about this :/
    data = f.readlines() + ['\n']

current_group = []
total = 0

for line in data:
    if line.strip():
        current_group.append(line.strip())
    else:
        unique_letters = {letter for answerset in current_group for letter in answerset}
        in_all = ''
        for l in unique_letters:
            for r in current_group:
                if l not in r:
                    break
            else:
                in_all += l
        total += len(in_all)
        current_group = []

print(total)


