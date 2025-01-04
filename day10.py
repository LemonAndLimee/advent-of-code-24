from utils import *

TRAILHEAD_NUMBER = 0
TRAIL_END_NUMBER = 9

def traverse(current_pos:tuple, positions:set, grid:list) -> int:
    '''Returns the number of distinct trails.'''
    value_at_current_pos = get_grid_value_at_position(position=current_pos, grid=grid)
    if value_at_current_pos == TRAIL_END_NUMBER:
        return 1
    
    num_trails = 0
    
    for direction in CARDINAL_DIRECTIONS:
        new_pos = apply_vector_to_position_2d(position=current_pos, vector=direction)

        if is_position_within_grid(position=new_pos, grid=grid) == False:
            continue

        value_at_new_pos = get_grid_value_at_position(position=new_pos, grid=grid)
        if value_at_new_pos == value_at_current_pos + 1:
            positions.add(new_pos)
            num_trails += traverse(new_pos, positions, grid)
    
    return num_trails

def get_trailhead_info(start_pos:tuple, grid:list) -> tuple[set,int]:
    '''Returns (trailhead map, no. distinct trails)'''
    positions = {start_pos}
    num_trails = traverse(start_pos, positions, grid)
    return (positions, num_trails)

def get_map_score(map:set, grid:list) -> int:
    total = 0
    for pos in map:
        value_at_pos = get_grid_value_at_position(position=pos, grid=grid)
        if value_at_pos == TRAIL_END_NUMBER:
            total += 1
    return total

def convert_map_to_list_of_strings(map:set, grid:list) -> list:
    lines = []
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            if (r, c) in map:
                line = line + str(grid[r][c])
            else:
                line = line + "."
        lines.append(line)
    return lines

def write_map_to_file(map:set, grid:list, filepath:str) -> list:
    map_strings = convert_map_to_list_of_strings(map, grid)
    write_lines_to_file(filepath=filepath, lines=map_strings)

def get_total_of_trailhead_scores(grid:list, debug_mode:bool=False) -> int:
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            cell_value = grid[r][c]
            if cell_value == TRAILHEAD_NUMBER:
                (trailhead_map, rating) = get_trailhead_info(start_pos=(r,c), grid=grid)
                trailhead_score = get_map_score(map=trailhead_map, grid=grid)
                total += trailhead_score

                if debug_mode == True:
                    trailhead_map_filename = f"outputs/trailhead_{r}_{c}.txt"
                    write_map_to_file(trailhead_map, grid, filepath=trailhead_map_filename)
    
    return total

def get_total_of_trailhead_ratings(grid:list, debug_mode:bool=False) -> int:
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            cell_value = grid[r][c]
            if cell_value == TRAILHEAD_NUMBER:
                (trailhead_map, rating) = get_trailhead_info(start_pos=(r,c), grid=grid)
                total += rating

                if debug_mode == True:
                    trailhead_map_filename = f"outputs/trailhead_{r}_{c}.txt"
                    write_map_to_file(trailhead_map, grid, filepath=trailhead_map_filename)
    
    return total

def part1():
    input = read_file_to_2d_list_of_ints(get_input_filepath(day=10))
    score_total = get_total_of_trailhead_scores(input, debug_mode=False)
    print(score_total)

def part2():
    input = read_file_to_2d_list_of_ints(get_input_filepath(day=10))
    rating_total = get_total_of_trailhead_ratings(input, debug_mode=False)
    print(rating_total)