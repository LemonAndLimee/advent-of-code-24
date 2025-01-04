from utils import *

def get_symbols_and_positions_as_dict(grid:list, exclude:str) -> dict:
    symbols_positions = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            cell = grid[r][c]
            if cell not in exclude:
                if cell in symbols_positions:
                    positions = symbols_positions[cell]
                    positions.append((r, c))
                    symbols_positions[cell] = positions
                else:
                    symbols_positions[cell] = [(r,c)]
    return symbols_positions

def generate_positions_in_one_direction(start_pos:tuple, vector:tuple, unlimited_positions:bool, grid_dimensions:tuple) -> list:
    positions = []
    continue_loop = True
    current_pos = start_pos
    while continue_loop:
        continue_loop = unlimited_positions
        new_pos = apply_vector_to_position_2d(position=current_pos, vector=vector)
        if is_position_within_grid_dimensions(new_pos, grid_dimensions):
            positions.append(new_pos)
        else:
            continue_loop = False
        current_pos = new_pos
    
    return positions

def get_antinode_positions_for_pair(position1:tuple, position2:tuple, grid_dimensions:tuple, unlimited_antinodes:bool) -> list:
    vector_pos1_to_pos2 = get_vector_between_two_positions_2d(src=position1, dest=position2)
    
    positions_in_positive_direction = generate_positions_in_one_direction(position2, 
                                                                          vector_pos1_to_pos2,
                                                                          unlimited_antinodes,
                                                                          grid_dimensions)
    
    inverse_vector = get_numeric_inverse_of_tuple_2d(vector_pos1_to_pos2)
    positions_in_negative_direction = generate_positions_in_one_direction(position1,
                                                                          inverse_vector,
                                                                          unlimited_antinodes,
                                                                          grid_dimensions)
    positions = positions_in_positive_direction + positions_in_negative_direction
    return positions

def get_antinode_positions_for_symbol(antenna_positions:list, grid_dimensions:tuple, unlimited_antinodes:bool) -> list:
    if len(antenna_positions) == 1:
        return []
    
    distinct_positions = []
    
    for i in range(len(antenna_positions)-1):
        pos1 = antenna_positions[i]
        for j in range(i+1, len(antenna_positions)):
            pos2 = antenna_positions[j]
            antinode_positions = get_antinode_positions_for_pair(pos1, pos2, grid_dimensions, unlimited_antinodes)
            
            for pos in antinode_positions:
                if pos not in distinct_positions:
                    distinct_positions.append(pos)
    
    return distinct_positions

def write_antinodes_to_grid(antinode_positions:list, grid:list):
    for pos in antinode_positions:
        r = pos[0]
        c = pos[1]
        grid[r][c] = "#"

def write_antinodes_to_file(filename:str, antinode_positions:list, original_grid:list):
    grid_copy = copy_2d_list(original_grid)
    write_antinodes_to_grid(antinode_positions, grid_copy)
    write_grid_to_file(filepath=filename, grid=grid_copy)

def write_symbol_antinodes_to_file(symbol:str, antinode_positions:list, original_grid:list):
    suffix = ""
    if symbol.isupper():
        suffix = "_upper"
    filename = f"outputs/day8_{symbol}{suffix}.txt"
    write_antinodes_to_file(filename, antinode_positions, original_grid)

def get_distinct_antinode_positions(grid:list, unlimited_antinodes:bool=False, count_antenna:bool=False) -> list:
    grid_dimensions = (len(grid), len(grid[0]))
    symbols_positions = get_symbols_and_positions_as_dict(grid, exclude=".")
    
    distinct_antinode_positions = []
    
    for symbol in symbols_positions:
        antinode_positions = get_antinode_positions_for_symbol(symbols_positions[symbol], grid_dimensions, unlimited_antinodes)
        for pos in antinode_positions:
            if pos not in distinct_antinode_positions:
                distinct_antinode_positions.append(pos)
        
        if count_antenna:
            antenna_positions = symbols_positions[symbol]
            if len(antenna_positions) > 1:
                for pos in antenna_positions:
                    if pos not in distinct_antinode_positions:
                        distinct_antinode_positions.append(pos)
    
    return distinct_antinode_positions

def part1():
    grid = read_file_to_2d_list_of_chars(get_input_filepath(day=8))
    distinct_antinode_positions = get_distinct_antinode_positions(grid)
    print(len(distinct_antinode_positions))

def part2():
    grid = read_file_to_2d_list_of_chars(get_input_filepath(day=8))
    distinct_antinode_positions = get_distinct_antinode_positions(grid, unlimited_antinodes=True, count_antenna=True)
    print(len(distinct_antinode_positions))