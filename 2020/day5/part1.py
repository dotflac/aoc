def decode_boarding_pass(s):
    row, col = s[:7], s[7:]
    row = row.replace('B','1').replace('F','0')
    col = col.replace('R','1').replace('L','0')
    row = int(row, base=2)
    col = int(col, base=2)
    return row, col, (row * 8 + col)

if __name__ == '__main__':
    ids = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            *_, id_num = decode_boarding_pass(line)
            ids.append(id_num)
    print(max(ids))
