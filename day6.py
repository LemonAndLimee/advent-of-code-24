from utils import *

OBSTACLE_SYMBOLS = ['#', 'O']

visited_squares = []
setups = []

def get_guard_position(grid:list) -> tuple:
    for r in range(len(grid)):
        row = grid[r]
        for c in range(len(row)):
            if row[c] == "^":
                return (r, c)
    raise Exception("Could not find guard.")

def set_position(square:tuple, char, grid:list):
    row_str = grid[square[0]]
    new_str = row_str[:square[1]] + char + row_str[square[1]+1:]
    grid[square[0]] = new_str

def rotate(current_direction:tuple) -> tuple:
    # north
    if current_direction == (-1,0):
        return (0,1)
    # east
    elif current_direction == (0,1):
        return (1,0)
    # south
    elif current_direction == (1,0):
        return (0,-1)
    # west
    elif current_direction == (0,-1):
        return (-1,0)
    else:
        raise Exception("Invalid direction")

def get_next_square_pos(setup:tuple) -> tuple:
    current_row = setup[0][0]
    current_col = setup[0][1]
    current_direction = setup[1]
    return (current_row+current_direction[0], current_col+current_direction[1])

def get_grid_square(square:tuple, grid:list):
    if square[0] < 0 or square[1] < 0:
        raise IndexError
    return grid[square[0]][square[1]]

def get_next_setup(current_setup:tuple, grid:list) -> tuple:
    current_pos = current_setup[0]
    direction = current_setup[1]
    new_square_pos = get_next_square_pos(current_setup)
    while get_grid_square(new_square_pos, grid) in OBSTACLE_SYMBOLS:
        direction = rotate(direction)
        new_square_pos = get_next_square_pos((current_pos, direction))
    
    return (new_square_pos, direction)

def traverse_grid(grid:list):
    # direction vector in terms of row,col where [-1,0] points upwards
    direction = (-1,0)
    start_pos = get_guard_position(grid)
    try:
        setup = (start_pos, direction)
        while True:
            if setup[0] not in visited_squares:
                visited_squares.append(setup[0])
            setups.append(setup)
            setup = get_next_setup(setup, grid)
    except IndexError as e:
        #print(f"exception while traversing grid: {e}")
        return

def print_subsection(grid:list, square:tuple, radius:int):
    for r in range(square[0]-radius, square[0]+radius+1):
        row = ""
        for c in range(square[1]-radius, square[1]+radius+1):
            try:
                row = row + f" {grid[r][c]} "
            except:
                pass
        print(row)

def part1():
    rows = read_file_to_list_of_lines(get_input_filepath(day=6))
    traverse_grid(rows)
    print(len(visited_squares))

#part1()