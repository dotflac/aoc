import re

regex = re.compile(r'(?P<first_pos>\d+)-(?P<second_pos>\d+) (?P<c>\w): (?P<password>\w+)')

def verify(record):
    first_pos, second_pos, character, password = regex.fullmatch(record.strip()).groups()
    first_pos, second_pos = int(first_pos) - 1, int(second_pos) - 1
    return (password[first_pos] == character) != (password[second_pos] == character)
    
if __name__ == '__main__':
    with open('input.txt') as f:
        records = f.readlines()
        print(len(list(filter(verify, records))))
