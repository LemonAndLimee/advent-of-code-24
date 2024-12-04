import utils

grid = utils.read_file_to_2d_list_of_chars("day4_input.txt")
direction_vectors = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]
]

def is_match(remaining_string:str, row:int, col:int, direction:list) -> bool:
    
    if len(remaining_string) == 0:
        return True
    
    new_row = row + direction[0]
    new_col = col + direction[1]
    
    if new_row < 0 or new_col < 0:
        return False
    
    try:
        cell = grid[new_row][new_col]
    except:
        return False
    
    if cell == remaining_string[0]:
        return is_match(remaining_string[1:], new_row, new_col, direction)
    else:
        return False

def get_occurrences_from_first_letter(string:str, row:int, col:int):
    occurrences = 0
    for direction in direction_vectors:
        if is_match(string[1:], row, col, direction):
            occurrences += 1

    return occurrences

def get_string_occurrences(string:str):
    occurrences = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col]
            if char == string[0]:
                occurrences += get_occurrences_from_first_letter(string, row, col)
    return occurrences

def part1():
    print(get_string_occurrences("XMAS"))

def get_x_occurrences():
    occurrences = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col]
            if char == 'A':
                if is_x_match_from_centre(row, col):
                    occurrences += 1
    return occurrences

def is_x_match_from_centre(row:int, col:int):
    diagonal_directions = [ [1, 1], [1, -1] ]
    
    for diagonal in diagonal_directions:
        if not is_diagonal_mas_match(row, col, diagonal):
            return False
    
    return True

def is_diagonal_mas_match(row:int, col:int, diagonal:list):
    required_letters = ['M', 'S']
    
    row_dir = diagonal[0]
    col_dir = diagonal[1]
    
    if matches_one_of_expected_chars(row, col, diagonal, required_letters):
        found_char = grid[row+row_dir][col+col_dir]
        required_letters.remove(found_char)
        
        opposite_diagonal = [-row_dir, -col_dir]
        return matches_one_of_expected_chars(row, col, opposite_diagonal, required_letters)
    else:
        return False
    
def matches_one_of_expected_chars(row:int, col:int, direction:list, expected_chars:list):
    new_row = row + direction[0]
    new_col = col + direction[1]
    
    if new_row < 0 or new_col < 0:
        return False
    
    try:
        cell = grid[new_row][new_col]
    except:
        return False
    
    if cell in expected_chars:
        return True
    else:
        return False

def part2():
    print(get_x_occurrences())