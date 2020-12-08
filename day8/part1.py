if __name__ == '__main__':
    accumulator = 0
    instruction_pointer = 0
    executed_instructions = []
    with open('input.txt') as f:
        program = [line.strip() for line in f.readlines()]
    while True:
        if instruction_pointer in executed_instructions:
            print(accumulator)
            break
        executed_instructions.append(instruction_pointer)
        ins, v = program[instruction_pointer].split()
        if ins == 'nop':
            instruction_pointer += 1
        elif ins == 'acc':
            accumulator += int(v)
            instruction_pointer += 1
        elif ins == 'jmp':
            instruction_pointer += int(v)
