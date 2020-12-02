import re

regex = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<c>\w): (?P<password>\w+)')

def verify(record):
    minimum, maximum, character, password = regex.fullmatch(record.strip()).groups()
    return(int(minimum) <= password.count(character) <= int(maximum))

if __name__ == '__main__':
    with open('input.txt') as f:
        records = f.readlines()
        print(len(list(filter(verify, records))))
