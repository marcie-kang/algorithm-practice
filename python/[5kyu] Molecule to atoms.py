"""
For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
"""

def check_digit(formula, index):
    num = 1

    if index + 1 < len(formula) and formula[index + 1].isdigit():
        num = 0

        while index + 1 < len(formula) and formula[index + 1].isdigit():
            num = num * 10 + int(formula[index + 1])
            index += 1

    return num, index

def parse_element(formula, index):
    molecule = formula[index]

    if index + 1 < len(formula) and formula[index + 1].islower():
        molecule += formula[index + 1]
        index += 1

    return molecule, index

def parse_molecule(formula):
    stack = [{}]
    index = 0

    while index < len(formula):
        current = formula[index]

        if current.isupper():
            molecule, index = parse_element(formula, index)
            num, index = check_digit(formula, index)
            stack[-1][molecule] = stack[-1].get(molecule, 0) + num
        elif current in "([{":
            stack.append({})
        elif current in ")]}":
            top = stack.pop()
            num, index = check_digit(formula, index)

            for key, value in top.items():
                stack[-1][key] = stack[-1].get(key, 0) + value * num

        index += 1

    return stack[0]
