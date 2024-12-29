from utils import *
from day9 import IntWrapper, get_section_id, get_section_length, is_section_empty

def get_checksum_for_non_empty_section(section_index:int,
                                       next_checksum_index:IntWrapper,
                                       input_line:str) -> int:
    
    section_id = get_section_id(section_index)
    section_length = get_section_length(section_index, input_line)
    
    total = 0
    for i in range(section_length):
        total += section_id * next_checksum_index.value
        next_checksum_index.increment()
        
    return total

def does_file_fit_in_space(file_index:int,
                           input_line:str,
                           empty_space:int):
    
    file_length = get_section_length(file_index, input_line)
    if file_length <= empty_space:
        return True
    else:
        return False

class NoFileFits(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def get_next_file_to_insert_index(space_length:int,
                                  available_file_indexes:list,
                                  input_line:str) -> int:
    index_of_file_index = len(available_file_indexes) - 1
    while index_of_file_index >= 0:
        file_index = available_file_indexes[index_of_file_index]
        if does_file_fit_in_space(file_index=file_index, input_line=input_line, empty_space=space_length):
            return file_index
        index_of_file_index -= 1

    raise NoFileFits()

def get_checksum_for_empty_section(section_index:int,
                                   next_checksum_index:IntWrapper,
                                   available_file_indexes:list,
                                   input_line:str,
                                   debug_mode:bool=False) -> int:
    
    checksum = 0
    space_left = get_section_length(section_index, input_line)
    
    if debug_mode:
        print(f"\nEmpty space at index {section_index} with length {space_left}:")
    
    while space_left > 0:
        try:
            file_to_insert_index = get_next_file_to_insert_index(space_length=space_left,
                                                                 available_file_indexes=available_file_indexes,
                                                                 input_line=input_line)
            checksum_from_inserted_file = get_checksum_for_non_empty_section(section_index=file_to_insert_index,
                                                                             next_checksum_index=next_checksum_index,
                                                                             input_line=input_line)
            checksum += checksum_from_inserted_file
            space_left -= get_section_length(file_to_insert_index, input_line)
            
            if debug_mode:
                print(f"Insert file at index {file_to_insert_index}, space left = {space_left}, running checksum = {checksum}")
            
            available_file_indexes.remove(file_to_insert_index)
        except NoFileFits:
            next_checksum_index.increment(space_left)
            break
    
    if debug_mode:
        print(f"Returning empty space checksum {checksum}. Available file indexes = {available_file_indexes}")
    return checksum

def get_even_indexes(input_len:int) -> list:
    result = []
    for i in range(input_len):
        if i % 2 == 0:
            result.append(i)
    return result

def get_checksum(input_line:str, debug_mode:bool=False) -> int:
    checksum = 0
    checksum_index = IntWrapper(0)
    
    available_file_indexes = get_even_indexes(len(input_line))
    
    for i in range(len(input_line)):
        if len(available_file_indexes) == 0:
            break
        if is_section_empty(section_index=i):
            empty_checksum  = get_checksum_for_empty_section(section_index=i,
                                                             next_checksum_index=checksum_index,
                                                             available_file_indexes=available_file_indexes,
                                                             input_line=input_line,
                                                             debug_mode=debug_mode)
            checksum += empty_checksum
        else:
            if i == available_file_indexes[0]:
                section_index = available_file_indexes[0]
                non_empty_checksum = get_checksum_for_non_empty_section(section_index=i,
                                                                        next_checksum_index=checksum_index,
                                                                        input_line=input_line)
                if debug_mode:
                    print(f"\nNon empty file at index {section_index}, checksum = {non_empty_checksum}")
                checksum += non_empty_checksum
                available_file_indexes.pop(0)
                
            else:
                # if index is not available, it has been moved, and therefore the checksum ptr needs
                # to be incremented to account for the empty space it has left behind
                section_length = get_section_length(i, input_line)
                checksum_index.increment(section_length)
                
                if debug_mode:
                    print(f"Gap left at index {i}, checksum ptr incremented by {section_length}")
    
    return checksum


def part2():
    input = read_single_line_file_to_string(get_input_filepath(day=9))
    print(get_checksum(input))