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
            valid_count += 1
        # reset passport
        passport = ''

print(valid_count)