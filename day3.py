import re

INPUT_FILE = "day3_input.txt"           

input_string = ""

def get_uncorrupted_muls(input_str:str) -> list:
    matches = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", input_str)
    return matches

def get_uncorrupted_muls_and_toggles(input_str:str) -> list:
    regex_pattern = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)"
    matches = re.findall(regex_pattern, input_str)
    return matches

def perform_multiplication(mul_str:str) -> int:
    numbers_str = mul_str[4:-1]
    numbers_list = numbers_str.split(",")
    
    result = int(numbers_list[0]) * int(numbers_list[1])
    return result

def get_mult_total(mul_strings:list) -> int:
    total = 0
    for string in mul_strings:
        mul = perform_multiplication(string)
        total += mul
    return total

def get_mult_total_with_toggles(strings:list) -> int:
    total = 0
    mult_enabled = True
    for string in strings:
        if string == "do()":
            mult_enabled = True
        elif string == "don't()":
            mult_enabled = False
        else:
            if mult_enabled:
                total += perform_multiplication(string)
    
    return total

with open(INPUT_FILE, 'r') as input_file:
    for line in input_file:
        line_items = line.split()
        for item in line_items:
            input_string = input_string + item

def part1():
    mul_strings = get_uncorrupted_muls(input_string)
    total = get_mult_total(mul_strings)
    print(total)
    
def part2():
    strings = get_uncorrupted_muls_and_toggles(input_string)
    total = get_mult_total_with_toggles(strings)
    print(total)

part2()