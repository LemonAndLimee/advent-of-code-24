from utils import *

BUTTON_A_COST = 3
BUTTON_B_COST = 1

PART2 = True

class Configuration():
    def __init__(self) -> None:
        self.button_a = None
        self.button_b = None
        self.prize = None
    
    def __str__(self) -> str:
        return f"A: {self.button_a}, B: {self.button_b}, Prize: {self.prize}"

def get_input() -> list[Configuration]:
    filepath = get_input_filepath(day=13)
    configs = []
    with open(filepath, 'r') as input_file:
        current_config = Configuration()
        for line in input_file:
            if line == "\n":
                configs.append(current_config)
                current_config = Configuration()
            else:
                line_parts = line.split()
                x_part = line_parts[-2][2:-1]
                y_part = line_parts[-1][2:]
                tuple = (int(x_part), int(y_part))
                if "A" in line:
                    current_config.button_a = tuple
                elif "B" in line:
                    current_config.button_b = tuple
                elif "Prize" in line:
                    add = 0
                    if PART2:
                        add = 10000000000000
                    current_config.prize = (add + tuple[0], add + tuple[1])
        configs.append(current_config)
    return configs

def get_equations(config:Configuration) -> tuple[list[int]]:
    # equation: _a + _b = _
    equation1 = [config.button_a[0], config.button_b[0], config.prize[0]]
    equation2 = [config.button_a[1], config.button_b[1], config.prize[1]]
    return (equation1, equation2)

def multiply_equation(equation:list[int], multiplier:int):
    for i in range(len(equation)):
        equation[i] = equation[i] * multiplier

def minus_equations_with_same_b_coefficient(equation1:list[int], equation2:list[int]) -> tuple:
    # returns _a = _
    a_coeff = equation1[0] - equation2[0]
    prize = equation1[-1] - equation2[-1]
    return (a_coeff, prize)

def get_tokens_spent_on_config(config:Configuration) -> int:
    equation1, equation2 = get_equations(config)

    # multiply both so their B term has the same coefficient
    equation1_b_coeff = equation1[1]
    multiply_equation(equation1, equation2[1])
    multiply_equation(equation2, equation1_b_coeff)

    a_coefficient, prize = minus_equations_with_same_b_coefficient(equation1, equation2)
    if prize % a_coefficient == 0:
        a = prize / a_coefficient
        a_term = a * equation1[0]
        equation1_result = equation1[-1] - a_term
        if equation1_result % equation1[1] == 0:
            b = equation1_result / equation1[1]
            return int((a * BUTTON_A_COST) + (b * BUTTON_B_COST))
    
    # Equations have no answer, return 0
    return 0

def get_tokens_spent(configs:list[Configuration]) -> int:
    total = 0
    for config in configs:
        total += get_tokens_spent_on_config(config)
    return total

configs = get_input()
tokens = get_tokens_spent(configs)
print(tokens)