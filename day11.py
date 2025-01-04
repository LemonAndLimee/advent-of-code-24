from utils import *

PREVIOUS_CALCULATIONS = {}
'''
Stores previous calculation results in a dict, with key value form
(stone, blinks): number of stones
'''

def strip_leading_zeros(stone:str) -> str:
    stone_int = int(stone)
    return str(stone_int)

def strip_stones_leading_zeros(stones:list[str]) -> list[str]:
    result = []
    for stone in stones:
        result.append(strip_leading_zeros(stone))
    return result

def transform_stone(stone:str) -> list[str]:
    '''Returns 1 or more transformed stones, in a list.'''
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        new_stones = split_string_in_half(stone)
        new_stones_with_no_leading_zeros = strip_stones_leading_zeros(new_stones)
        return new_stones_with_no_leading_zeros
    else:
        new_stone = multiply_string_number(stone, 2024)
        return [new_stone]

def get_stones_after_blink(stones:list[str]) -> list[str]:
    result = []
    for stone in stones:
        new_stones = transform_stone(stone)
        for new_stone in new_stones:
            result.append(new_stone)
    return result

def get_num_stones_after_blinks(stones:list[str], blinks:int, debug_mode:bool=False) -> int:
    # Breadth first - used for part 1
    current_stones = stones.copy()
    for i in range(blinks):
        current_stones = get_stones_after_blink(current_stones)
        if debug_mode == True:
            print(f"Blink {i}, {len(current_stones)} stones")
    return len(current_stones)

def get_num_stones_generated_by_single_stone(stone:str, blinks:int) -> int:
    key = (stone, blinks)
    if key in PREVIOUS_CALCULATIONS:
        return PREVIOUS_CALCULATIONS[key]

    result = 0
    new_stones = transform_stone(stone)

    if blinks == 1:
        result = len(new_stones)
    else:
        for new_stone in new_stones:
            new_stone_num = get_num_stones_generated_by_single_stone(new_stone, blinks-1)
            result += new_stone_num
    
    PREVIOUS_CALCULATIONS[key] = result
    return result

def get_num_stones_after_blinks_depth_first(stones:list[str], blinks:int) -> int:
    total = 0
    for stone in stones:
        num_stones = get_num_stones_generated_by_single_stone(stone, blinks)
        total += num_stones
    return total

def part1():
    input = read_single_line_file_to_list_of_words(filepath=get_input_filepath(day=11))
    num_stones = get_num_stones_after_blinks(stones=input, blinks=25)
    print(num_stones)

def part2():
    input = read_single_line_file_to_list_of_words(filepath=get_input_filepath(day=11))
    num_stones = get_num_stones_after_blinks_depth_first(stones=input, blinks=75)
    print(num_stones)