# soru: introduction to programming > part 7 > lesson 6 - more python features'da

def run(program):
    # print("program:",program) #program: ['MOV A 1', 'MOV B 2', 'PRINT A', 'PRINT B', 'ADD A B', 'PRINT A', 'END']
    labels = {} #satır numaralarını tutmak icin
    variables = {}
    printed_list = []

    for index, command in enumerate(program):
        if ":" in command:
            name = command[:-1:]
            labels[name] = index #jump'ta kullanmak uzere indeksini alıyoruz
            # print(labels)

    i = 0
    while i < len(program):
        command = program[i]
        # print("command:", command) #command: MOV A 1
        command_list = command.split()
        # print("Command List:", command_list) #Command List: ['MOV', 'A', '1']
        command_name = command_list[0]
        if command_name == "MOV": #assign etmek icin
            if command_list[2] in variables:
                variables[command_list[1]] = variables[command_list[2]]
            else:
                variables[command_list[1]] = int(command_list[2])
        elif command_name == "PRINT":
            if command_list[1] in variables:
                printed_list.append(variables[command_list[1]])
            else: 
                try:
                    printed_list.append(int(command_list[1]))
                except ValueError:
                    printed_list.append(0) #ne sozlukte tanımlanmıs degisken ne sayı ise default 0 olur
        elif command_name == "ADD":
            if command_list[1] in variables:
                if command_list[2] in variables:
                    variables[command_list[1]] += variables[command_list[2]]
                else:
                    variables[command_list[1]] += int(command_list[2])
            else:
                variables[command_list[1]] = 0
                if command_list[2] in variables:
                    variables[command_list[1]] += variables[command_list[2]]
                else:
                    variables[command_list[1]] += int(command_list[2])
        elif command_name == "SUB":
            if command_list[2] in variables:
                variables[command_list[1]] -= variables[command_list[2]]
            else:
                variables[command_list[1]] -= int(command_list[2])
        elif command_name == "MUL":
            if command_list[2] in variables:
                variables[command_list[1]] *= variables[command_list[2]]
            else:
                variables[command_list[1]] *= int(command_list[2])
        elif command_name == "JUMP":
            target_name = command_list[1]
            i = labels[target_name] # *sihir burada, indeksi basa alıyoruz (for loop bunu yapamazdı)*
            continue #sayacı artırma!
        elif command_name == "IF":
            left_var = command_list[1]
            right_var = command_list[3]
            operator = command_list[2]
            if right_var in variables:
                if (operator == ">=" and variables[left_var] >= variables[right_var] or
                    operator == ">" and variables[left_var] > variables[right_var] or
                    operator == "<=" and variables[left_var] <= variables[right_var] or
                    operator == "<" and variables[left_var] < variables[right_var] or
                    operator == "!=" and variables[left_var] != variables[right_var] or
                    operator == "==" and variables[left_var] == variables[right_var]):
                    target_name = command_list[-1]
                    i = labels[target_name] #endless looptan cıkıyoruz
                    continue #sayacı artırma!
            else:
                if (operator == ">=" and variables[left_var] >= int(right_var) or
                    operator == ">" and variables[left_var] > int(right_var) or
                    operator == "<=" and variables[left_var] <= int(right_var) or
                    operator == "<" and variables[left_var] < int(right_var) or
                    operator == "!=" and variables[left_var] != int(right_var) or
                    operator == "==" and variables[left_var] == int(right_var)):
                    target_name = command_list[-1]
                    i = labels[target_name] #endless looptan cıkıyoruz
                    continue #sayacı artırma!
        elif command_name == "END":
            break
        i += 1
    return printed_list

def starter():
    # program1 = []
    # program1.append("MOV A 1")
    # program1.append("MOV B 2")
    # program1.append("PRINT A")
    # program1.append("PRINT B")
    # program1.append("ADD A B")
    # program1.append("PRINT A")
    # program1.append("END")
    # result = run(program1)
    # print(result)

    # program3 = []
    # program3.append("PRINT C")
    # print(run(program3))

    # program4 = ['MOV A 10', 'PRINT A', 'MOV B A', 'SUB B 8', 'PRINT B', 'SUB A B', 'PRINT A']
    # print(run(program4))

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    # program5 = ['MOV A 10', 'start:', 'PRINT A', 'SUB A 1', 'IF A > 0 JUMP start', 'END']
    # print(run(program5))

    # program6 = ['MOV A 1', 'MOV B 999', 'start:', 'ADD A 1', 'SUB B 1', 'ADD C 1', 'IF A == B JUMP end', 'JUMP start', 'end:', 'PRINT C']
    # print(run(program6))

    # program7 = ['MOV N 100', 'PRINT 2']
    # print(run(program7))

if __name__ == "__main__":
    starter()


# alt2: mooc.fi:
def value(x, data):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return data[characters.index(x)]
    else:
        return int(x)

def condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<":
        return a < b
    if condition == "<=":
        return a <= b
    if condition == ">":
        return a > b
    if condition == ">=":
        return a >= b

def run(program):
    length = len(program)
    row = 0
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    result = []
    while True:
        if row == length:
            break
        parts = program[row].split(" ")
        if parts[0] == "PRINT":
            result.append(value(parts[1], data))
        if parts[0] == "MOV":
            data[characters.index(parts[1])] = value(parts[2], data)
        if parts[0] == "ADD":
            data[characters.index(parts[1])] += value(parts[2], data)
        if parts[0] == "SUB":
            data[characters.index(parts[1])] -= value(parts[2], data)
        if parts[0] == "MUL":
            data[characters.index(parts[1])] *= value(parts[2], data)
        if parts[0] == "JUMP":
            row = program.index(parts[1]+":")
            continue
        if parts[0] == "IF":
            if condition(value(parts[1], data), parts[2], value(parts[3], data)):
                row = program.index(parts[5]+":")
                continue
        if parts[0] == "END":
            break
        row += 1
    return result
