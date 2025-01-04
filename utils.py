CARDINAL_DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def get_input_filepath(day:int) -> str:
    return f"inputs/day{day}_input.txt"

def read_file_to_list_of_lines(filepath:str) -> list:
    with open(filepath, 'r') as input_file:
        lines = []
        for line in input_file:
            if line[-1] == "\n":
                lines.append(line[:-1])
            else:
                lines.append(line)
    
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

def read_file_to_2d_list_of_ints(filepath:str) -> list:
    with open(filepath, 'r') as input_file:
        grid = []
        for line in input_file:
            row = []
            for char in line:
                if char != '\n':
                    row.append(int(char))
            grid.append(row)
    
    return grid

def read_single_line_file_to_string(filepath:str) -> str:
    with open(filepath, 'r') as input_file:
        string = input_file.readline()
    return string

def read_single_line_file_to_list_of_words(filepath:str) -> list[str]:
    line = read_single_line_file_to_string(filepath)
    words = line.split()
    return words

def read_single_line_file_to_list_of_ints(filepath:str) -> list[int]:
    words = read_single_line_file_to_list_of_words(filepath)
    ints = []
    for word in words:
        ints.append(int(word))
    return ints

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

def write_grid_to_file(filepath:str, grid:list):
    with open(filepath, 'w') as output_file:
        for row in grid:
            line = ""
            for cell in row:
                line = line + str(cell)
            output_file.write(line + "\n")

def copy_2d_list(src_list:list) -> list:
    result = []
    for row in src_list:
        new_row = row.copy()
        result.append(new_row)
    return result

def get_vector_between_two_positions_2d(src:tuple, dest:tuple) -> tuple:
    x = dest[0] - src[0]
    y = dest[1] - src[1]
    return (x, y)

def apply_vector_to_position_2d(position:tuple, vector:tuple) -> tuple:
    return (position[0] + vector[0], position[1] + vector[1])

def get_numeric_inverse_of_tuple_2d(t:tuple) -> tuple:
    return (-t[0], -t[1])

def is_position_within_grid_dimensions(position:tuple, grid_dimensions:tuple) -> bool:
    height = grid_dimensions[0]
    width = grid_dimensions[1]
    
    if position[0] < 0 or position[0] >= height:
        return False
    if position[1] < 0 or position[1] >= width:
        return False
    return True

def is_position_within_grid(position:tuple, grid:list) -> bool:
    grid_dimensions = (len(grid), len(grid[0]))
    return is_position_within_grid_dimensions(position, grid_dimensions)

def get_grid_value_at_position(position:tuple, grid:list):
    return grid[position[0]][position[1]]

def multiply_string_number(num:str, operand:int) -> str:
    '''Multiplies a number stored as a string, returning a string.'''
    num_int = int(num)
    result_int = num_int*operand
    return str(result_int)

def split_string_in_half(string:str) -> tuple[str]:
    if len(string) % 2 != 0:
        raise ValueError("String length must be even")
    
    midpoint = len(string) // 2
    string1 = string[:midpoint]
    string2 = string[midpoint:]

    return (string1, string2)