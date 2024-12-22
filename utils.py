def get_input_filepath(day:int) -> str:
    return f"inputs/day{day}_input.txt"

def read_file_to_list_of_lines(filepath:str) -> list:
    with open(filepath, 'r') as input_file:
        lines = []
        for line in input_file:
            lines.append(line[:-1])
    
    return lines

def read_file_to_2d_list_of_chars(filepath:str) -> list:
    with open(filepath, 'r') as input_file:
        grid = []
        for line in input_file:
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            grid.append(row)
    
    return grid

def get_middle_element(list:list) -> int:
    middle_index = int((len(list)-1) / 2)
    return list[middle_index]

def has_any_items_in_common(list1:list, list2:list) -> bool:
    for item in list1:
        if item in list2:
            return True
    return False

def write_lines_to_file(filepath:str, lines:list):
    with open(filepath, 'w') as output_file:
        for line in lines:
            output_file.write(line + "\n")

def copy_2d_list(src_list:list) -> list:
    result = []
    for row in src_list:
        new_row = row.copy()
        result.append(new_row)
    return result
        