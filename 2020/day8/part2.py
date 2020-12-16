import re

def run_program(program):
    accumulator = 0
    instruction_pointer = 0
    executed_instructions = []
    while instruction_pointer < len(program):
        if instruction_pointer in executed_instructions:
            raise Exception(f'infinite loop\n'
                            f'{instruction_pointer} : {program[instruction_pointer]}\n'
                            f'accumulator: {accumulator}\n')
        executed_instructions.append(instruction_pointer)
        ins, v = program[instruction_pointer].split()
        if ins == 'jmp':
            instruction_pointer += int(v)
            continue
        if ins == 'acc':
            accumulator += int(v)
        instruction_pointer += 1
    return accumulator

if __name__ == '__main__':
    with open('input.txt') as f:
        program = f.readlines()

    for index, instruction in enumerate(program):
        instruction, c = re.subn('nop', 'jmp', instruction)
        if not c:
            instruction, c = re.subn('jmp', 'nop', instruction)
        if c:
            patched_program = program[:index] + \
                              [instruction] + \
                              program[index + 1:]
            try:
                print(run_program(patched_program))
                break
            except Exception as e:
                continue
