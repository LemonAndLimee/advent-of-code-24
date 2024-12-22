import day6
from utils import *

# for each traversed square
# imagine you added a # there, where would the new direction be?
# to cause a loop, there has to be another # in that direction that causes the next setup to be a previous one
# i.e. the position and direction match a previous one

ORIGINAL_GRID = read_file_to_list_of_lines(get_input_filepath(day=6))
day6.traverse_grid(ORIGINAL_GRID.copy())
TRAVERSED_SQUARES = day6.visited_squares.copy()
TRAVERSED_SETUPS = day6.setups.copy()

def get_next_direction_assuming_obstacle(setup:tuple, grid:list) -> tuple:
    direction = setup[1]
    checks = 1
    while checks < 4:
        direction = day6.rotate(direction)
        next_square_pos = day6.get_next_square_pos((setup[0], direction))
        if day6.get_grid_square(next_square_pos, grid) not in day6.OBSTACLE_SYMBOLS:
            return direction
        else:
            checks += 1
    
    day6.print_subsection(ORIGINAL_GRID, setup[0], radius=3)
    raise Exception(f"Adding obstacle in front causes no viable direction. {setup}")
            
def does_traversal_cause_loop(setup:tuple, traversed_setups:list, grid:list) -> bool:
    try:
        while True:
            if setup in traversed_setups:
                return True
            else:
                traversed_setups.append(setup)
            setup = day6.get_next_setup(setup, grid)
    except IndexError as e:
        return False

def adding_obstacle_in_front_causes_loop(setup:tuple, next_square:tuple, traversed_setups_idx:int, grid:list) -> bool:
    # get next direction/setup upon adding an obstacle
    next_direction = get_next_direction_assuming_obstacle(setup, grid)
    new_setup = (setup[0], next_direction)

    # traverse until end or hits loop
    case_specific_traversed_setups = TRAVERSED_SETUPS[:traversed_setups_idx]
    day6.set_position(next_square, "O", grid)
    return does_traversal_cause_loop(new_setup, traversed_setups=case_specific_traversed_setups, grid=grid)

def get_setup_index_from_square(square:tuple, setups:list) -> int:
    for i in range(len(setups)):
        if setups[i][0] == square:
            return i
    raise Exception(f"Setup index not found for square {square}")

def get_num_obstacles_that_cause_loop() -> int:
    guard_pos = day6.get_guard_position(ORIGINAL_GRID)
    total = 0
    
    for i in range(1, len(TRAVERSED_SQUARES)):
        #added square = squares [i]
        #setup on that square = get setup from square i
        # previous setup = setups [idx - 1]
        
        next_square = TRAVERSED_SQUARES[i]
        setup_index_on_next_square = get_setup_index_from_square(next_square, TRAVERSED_SETUPS)
        current_setup_index = setup_index_on_next_square - 1
        setup = TRAVERSED_SETUPS[current_setup_index]
        
        if next_square == guard_pos:
            print(f" skipping {i}/{len(TRAVERSED_SQUARES)-1} with setup {setup} as square is start pos {next_square}")
            continue
        print(f"{i}/{len(TRAVERSED_SQUARES)-1} with setup {setup} and square {next_square}")
        
        grid = ORIGINAL_GRID.copy()
        if adding_obstacle_in_front_causes_loop(setup, next_square, traversed_setups_idx=current_setup_index, grid=grid):
            print(f"causes obstacle, total= {total}")
            total += 1
        
    return total

def write_setup_to_grid(setup:tuple, grid:list):
    symbol = ""
    direction = setup[1]
    if direction == (-1, 0):
        symbol = "^"
    elif direction == (1, 0):
        symbol = "v"
    elif direction == (0, 1):
        symbol = ">"
    elif direction == (0, -1):
        symbol = "<"
    else:
        raise Exception(f"Unknown direction {direction}")
    
    day6.set_position(setup[0], symbol, grid)

def write_setups_to_grid(setups:list, grid:list):
    for setup in setups:
        write_setup_to_grid(setup, grid)

def output_specific_case(added_square:tuple):
    grid = ORIGINAL_GRID.copy()
    day6.set_position(added_square, 'O', grid)
    
    case_specific_traversed_setups = []
    start_setup = (day6.get_guard_position(grid), (-1, 0))
    
    does_traversal_cause_loop(start_setup, case_specific_traversed_setups, grid)
    
    write_setups_to_grid(case_specific_traversed_setups, grid)

    write_lines_to_file(filepath=f"outputs\\day6_pt2_{str(added_square[0])}_{str(added_square[1])}.txt", lines=grid)

def get_loop_subset_of_setups(setups:list, grid:list) -> list:
    repeat_setup = day6.get_next_setup(setups[-1], grid)
    loop_start_index = setups.index(repeat_setup)
    
    return setups[loop_start_index:]

def output_loop_case(added_square:tuple):
    grid = ORIGINAL_GRID.copy()
    day6.set_position(added_square, 'O', grid)
    
    case_specific_traversed_setups = []
    start_setup = (day6.get_guard_position(grid), (-1, 0))
    
    if does_traversal_cause_loop(start_setup, case_specific_traversed_setups, grid):
        loop_setups = get_loop_subset_of_setups(case_specific_traversed_setups, grid)
        write_setups_to_grid(loop_setups, grid)
    else:
        raise Exception(f"This case is not a loop")

    write_lines_to_file(filepath=f"outputs\\day6_pt2_{str(added_square[0])}_{str(added_square[1])}.txt", lines=grid)

def part2():
    print(get_num_obstacles_that_cause_loop())

part2()
