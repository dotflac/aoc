with open('test_input.txt') as f:
    instructions = f.read().rstrip().split('\n')

facing = 'E'
displacement = [0,0]

def parse_instruction(ins):
    letter = ins[0]
    number = int(ins[1:])
    print(letter, number)


for ins in instructions:
    parse_instruction(ins)