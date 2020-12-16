import re

EXPECTED_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
}

with open('input.txt') as f:
    data = f.readlines()

passport = ''
valid_count = 0

for line in data:
    if line.strip():
        # construct multiline passport
        passport += line
    else:
        # process passport
        passport = dict(kv.split(':') for kv in passport.split())
        if all(field in passport for field in EXPECTED_FIELDS):
            if all((
                (passport['byr'].isnumeric() and
                1920 <= int(passport['byr']) <= 2002),
                (passport['iyr'].isnumeric() and
                2010 <= int(passport['iyr']) <= 2020),
                (passport['eyr'].isnumeric() and
                2020 <= int(passport['eyr']) <= 2030),
                any((
                    (
                        passport['hgt'][:3].isnumeric() and
                        150 <= int(passport['hgt'][:3]) <= 193 and
                        passport['hgt'][3:] == 'cm'
                    ),
                    (
                        passport['hgt'][:2].isnumeric() and
                        59 <= int(passport['hgt'][:2]) <= 76 and
                        passport['hgt'][2:] == 'in'
                    )
                )),
                re.fullmatch(r'#[a-f0-9]{6}', passport['hcl'], re.I),
                passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
                passport['pid'].isnumeric() and len(passport['pid']) == 9
            )):
                valid_count += 1
        # reset passport
        passport = ''

print(valid_count)