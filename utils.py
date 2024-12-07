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