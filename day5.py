from utils import *

def get_input(filepath:str) -> tuple:
    rules = []
    updates = []

    is_on_first_section = True
    delim = "|"

    with open(filepath, 'r') as input_file:
        for line in input_file:
            if line == "\n":
                is_on_first_section = False
                delim = ","
                continue

            numbers = line.split(delim)
            nums_list = []
            for num in numbers:
                if num != "\n":
                    nums_list.append(int(num))
            
            if is_on_first_section:
                rules.append(nums_list)
            else:
                updates.append(nums_list)
    
    return (rules, updates)

rules, updates = get_input(get_input_filepath(day=5))

def get_all_lhs_items_by_rhs(rhs:int) -> list:
    '''Get list of LHS numbers that have a given RHS number.'''
    left_items = []
    for rule in rules:
        if rule[1] == rhs:
            left_items.append(rule[0])
    return left_items

def is_update_correct(update:list) -> bool:
    if len(update) <= 1:
        return True

    first = update[0]
    # if any rules have the first number on the RHS, the LHS number is not allowed in the
    # rest of this list
    not_allowed_numbers = get_all_lhs_items_by_rhs(first)
    rest_of_update = update[1:]

    if has_any_items_in_common(rest_of_update, not_allowed_numbers):
        return False
    else:
        return is_update_correct(rest_of_update)

def part1():
    middle_page_total = 0
    for update in updates:
        if is_update_correct(update):
            middle_page_total += get_middle_element(update)
    
    print(middle_page_total)

def get_incorrect_updates() -> list:
    incorrects = []
    for update in updates:
        if not is_update_correct(update):
            incorrects.append(update)
    return incorrects

def is_after(num1:int, num2:int) -> bool:
    ''' Returns true if num1 must come after num2.'''
    for rule in rules:
        if num1 in rule and num2 in rule:
            if rule[0] == num1:
                return False
            else:
                return True
    raise Exception("Could not find rule.")

def bubble_sort_with_custom_rules(list:list) -> list:
    result = list.copy()
    for pass_num in range(len(list)):
        empty_pass = True
        for index in range((len(list)-1) - pass_num):
            if is_after(result[index], result[index+1]):
                temp = result[index]
                result[index] = result[index+1]
                result[index+1] = temp
                empty_pass = False
        if empty_pass:
            break

    return result

def part2():
    middle_page_total = 0
    incorrect_updates = get_incorrect_updates()
    for update in incorrect_updates:
        corrected_update = bubble_sort_with_custom_rules(update)
        middle_page_total += get_middle_element(corrected_update)
    print(middle_page_total)

part2()