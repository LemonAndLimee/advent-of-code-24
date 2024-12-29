from utils import *

class Pointer():
    def __init__(self, section, block):
        self.section = section
        self.block = block
    
    def decrement(self, input_line:str):
        '''Decrements block by 1, moving to a new section if necessary'''
        if self.block == 0:
            # decrement section by 2 to skip the empty section next to it
            self.section = self.section - 2
            self.block = get_section_length(section_index=self.section, input_line=input_line) - 1
        else:
            self.block = self.block - 1

class IntWrapper():
    def __init__(self, value):
        self.value = value
    
    def increment(self, increment_amount:int=1):
        self.value = self.value + increment_amount

def is_section_empty(section_index:int) -> bool:
    return section_index % 2 != 0

def get_section_id(section_index:int) -> int:
    if is_section_empty(section_index):
        raise ValueError(f"Section at index {section_index} is an empty space, and has no ID.")
    return section_index // 2

def get_section_length(section_index:int, input_line:str) -> int:
    return int(input_line[section_index])

def get_checksum_for_non_empty_section(section_index:int,
                                       next_checksum_index:IntWrapper,
                                       end_ptr:Pointer,
                                       input_line:str) -> int:
    
    section_id = get_section_id(section_index)
    section_length = get_section_length(section_index, input_line)
    
    total = 0
    calculate_until = section_length
    if section_index == end_ptr.section:
        calculate_until = end_ptr.block + 1
        
    for i in range(calculate_until):
        total += section_id * next_checksum_index.value
        next_checksum_index.increment()
        
    return total

def get_checksum_for_empty_section(section_index:int,
                                   next_checksum_index:IntWrapper,
                                   end_ptr:Pointer,
                                   input_line:str) -> int:
    
    section_length = get_section_length(section_index, input_line)
    
    total = 0
    calculate_until = section_length
    if section_index == end_ptr.section - 1:
        calculate_until = end_ptr.block + 1
        
    for i in range(calculate_until):
        block_id = get_section_id(end_ptr.section)
        total += block_id * next_checksum_index.value
        next_checksum_index.increment()
        end_ptr.decrement(input_line)
        
    return total

def get_checksum_for_section(section_index:int,
                             next_checksum_index:IntWrapper,
                             end_ptr:Pointer,
                             input_line:str) -> int:
    '''
    For a given section (in example 12345, a section would be represented by a single digit),
    get the checksum for the blocks that occupy that section.
    
    If the section is not empty, get the ID of the blocks that occupy this section.
    Checksum = (checksum index * ID) + ((checksum index + 1) * ID) + ...
    If (section, block) hits the end pointer, stop and return.
    
    If section is empty, fill it from the end using end pointer.
    Calculate checksum using same method.
    
    '''
    if is_section_empty(section_index):
        checksum = get_checksum_for_empty_section(section_index, next_checksum_index, end_ptr, input_line)
        return checksum
    else:
        checksum = get_checksum_for_non_empty_section(section_index, next_checksum_index, end_ptr, input_line)
        return checksum

def get_checksum(input_line:str) -> int:
    checksum = 0
    checksum_index = IntWrapper(0)
    
    end_section_index = len(input_line)-1
    end_section_length = get_section_length(end_section_index, input_line)
    end_pointer = Pointer(section=end_section_index, block=end_section_length-1)
    
    section_index = 0
    while section_index <= end_pointer.section:
        section_checksum = get_checksum_for_section(section_index=section_index,
                                                    next_checksum_index=checksum_index,
                                                    end_ptr=end_pointer,
                                                    input_line=input_line)
        checksum += section_checksum
        section_index += 1
    
    return checksum

def part1():
    input = read_single_line_file_to_string(get_input_filepath(day=9))
    print(get_checksum(input))