def simple_assembler(program):
    registers = {}
    pc = 0
    splited_program = []

    for part in program:
        splited_program += [part.split(" ")]

    while pc < len(program):
        command = splited_program[pc][0]
        x = splited_program[pc][1]

        if command == "mov":
            registers[x] = int(splited_program[pc][2])
        elif command == "inc":
            registers[x] += 1
        elif command == "dec":
            registers[x] -= 1
        elif command == "jnz" and registers[x] != 0:
            pc -= int(splited_program[pc][2])
            continue

        pc += 1

    return registers

print(simple_assembler(["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"]))