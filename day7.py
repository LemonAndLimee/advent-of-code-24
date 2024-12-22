from utils import *

def get_inputs_as_list_of_tuples(input_lines:list) -> list:
    result = []
    for line in input_lines:
        items = str.split(line)
        value = int(items[0][:-1])
        
        operands = []
        for i in range(1, len(items)):
            operands.append(int(items[i]))
        
        list_item = (value, operands)
        result.append(list_item)
    return result

class Operation:
    def __init__(self):
        pass
    
    def execute(num1:int, num2:int) -> int:
        raise Exception("Not implemented: base class.")
    
    def inverse(num1, num2):
        raise Exception("Not implemented: base class.")

class Add(Operation):
    def __init__(self):
        super().__init__()
    
    def execute(self, num1, num2) -> int:
        return num1 + num2
    
    def inverse(self, num1, num2) -> int:
        return num1 - num2

class DivisionCausesNonInt(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Multiply(Operation):
    def __init__(self):
        super().__init__()
    
    def execute(self, num1, num2):
        return num1 * num2
    
    def inverse(self, num1, num2) -> int:
        if num1 % num2 == 0:
            return num1 / num2
        else:
            raise DivisionCausesNonInt

class InverseConcatenateNotPossible(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Concatenate(Operation):
    def __init__(self):
        super().__init__()
    
    def execute(self, num1, num2) -> int:
        joined_str = str(num1) + str(num2)
        return int(joined_str)

    def inverse(self, num1, num2) -> int:
        '''Removes num2 from the end of the string version of num1'''
        num1_str = str(num1)
        num2_str = str(num2)
        if num1_str[-len(num2_str):] != num2_str:
            raise InverseConcatenateNotPossible(f"{num2} is not on the end of {num1}")
        elif len(num1_str) == len(num2_str):
            raise InverseConcatenateNotPossible("Arguments are of same string length.")
        else:
            result_str = num1_str[:-len(num2_str)]
            return int(result_str)

def can_operands_match_value(desired_value:int, operands:list, allowed_operations:list) -> bool:
    if len(operands) == 1:
        return operands[0] == desired_value
    
    last_operand = operands[-1]
    for operation in allowed_operations:
        try:
            new_desired_value = operation.inverse(num1=desired_value, num2=last_operand)
        except DivisionCausesNonInt:
            continue
        except InverseConcatenateNotPossible:
            continue
        if can_operands_match_value(desired_value=new_desired_value, operands=operands[:-1]):
            return True
    
    return False

def is_equation_achievable(equation:list, allowed_operations:list) -> bool:
    value = equation[0]
    operands = equation[1]
    return can_operands_match_value(value, operands, allowed_operations)

def get_total_of_achievable_equations(equations:list, allowed_operations:list) -> int:
    total = 0
    for equation in equations:
        if is_equation_achievable(equation, allowed_operations):
            print(f"achievable equation {equation}")
            total += equation[0]
    return total

def part1():
    lines = read_file_to_list_of_lines(get_input_filepath(day=7))
    equations = get_inputs_as_list_of_tuples(lines)
    allowed_operations = (Add(), Multiply())
    print(get_total_of_achievable_equations(equations, allowed_operations))

def part2():
    lines = read_file_to_list_of_lines(get_input_filepath(day=7))
    equations = get_inputs_as_list_of_tuples(lines)
    allowed_operations = (Add(), Multiply(), Concatenate())
    print(get_total_of_achievable_equations(equations, allowed_operations))