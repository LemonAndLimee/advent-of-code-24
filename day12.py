from utils import *

def traverse(current_pos:tuple, current_region:list, grid:list) -> None:
    current_char = get_grid_value_at_position(current_pos, grid)

    for direction in CARDINAL_DIRECTIONS:
        new_pos = apply_vector_to_position_2d(position=current_pos, vector=direction)
        if is_position_within_grid(new_pos, grid):
            if new_pos not in current_region:
                new_char = get_grid_value_at_position(new_pos, grid)
                if new_char == current_char:
                    current_region.append(new_pos)
                    traverse(new_pos, current_region, grid)


def get_region_from_start_pos(start_pos:tuple, grid:list) -> list[tuple]:
    region = [start_pos]
    traverse(start_pos, region, grid)
    return region

def get_list_of_regions(grid:list) -> list:
    regions = []
    positions = get_list_of_grid_positions(grid)

    while len(positions) > 0:
        position = positions[0]
        region = get_region_from_start_pos(start_pos=position, grid=grid)
        remove_list_from_other_list(list_to_remove=region, list_to_remove_from=positions)
        regions.append(region)
    
    return regions

def is_border_edge(position:tuple, direction:tuple, region:list) -> bool:
    adjacent_pos = apply_vector_to_position_2d(position, direction)
    if adjacent_pos not in region:
        return True
    return False

def get_fences_needed_for_square(position:tuple, region:list) -> int:
    total = 0
    for direction in CARDINAL_DIRECTIONS:
        if is_border_edge(position, direction, region):
            total += 1
    return total

def get_region_perimeter(region:list) -> int:
    perimeter = 0
    for position in region:
        fences = get_fences_needed_for_square(position, region)
        perimeter += fences
    return perimeter

def traverse_edge_in_one_direction(position:tuple,
                                   edge_direction:tuple,
                                   traversal_direction:tuple,
                                   uncounted_edges:list) -> None:
    current_pos = position
    continue_loop = True
    while continue_loop:
        next_pos = apply_vector_to_position_2d(current_pos, traversal_direction)
        if (next_pos, edge_direction) in uncounted_edges:
            uncounted_edges.remove((next_pos, edge_direction))
            current_pos = next_pos
        else:
            continue_loop = False

def traverse_edge(position:tuple, direction:tuple, uncounted_border_edges:list) -> None:
    normal_vector1 = (direction[1], direction[0])
    traverse_edge_in_one_direction(position, direction, normal_vector1, uncounted_border_edges)
    
    normal_vector2 = (-direction[1], -direction[0])
    traverse_edge_in_one_direction(position, direction, normal_vector2, uncounted_border_edges)

    uncounted_border_edges.remove((position, direction))

def get_num_sides_of_region(region:list) -> int:

    num_sides = 0
    uncounted_border_edges = get_border_edges(region)

    while len(uncounted_border_edges) > 0:
        edge = uncounted_border_edges[0]
        num_sides += 1
        traverse_edge(position=edge[0], direction=edge[1], uncounted_border_edges=uncounted_border_edges)
    
    return num_sides

def get_border_edges(region) -> list:
    edges = []
    for position in region:
        for direction in CARDINAL_DIRECTIONS:
            if is_border_edge(position, direction, region):
                edges.append((position, direction))
    return edges

def get_fence_price_for_region(region:list, using_perimeter:bool) -> int:
    region_area = len(region)
    if using_perimeter:
        region_perimeter = get_region_perimeter(region)
        result = region_area * region_perimeter
    else:
        num_sides = get_num_sides_of_region(region)
        result = region_area * num_sides
    return result

def get_total_fence_prices(grid:list, using_perimeter:bool=True) -> int:
    total = 0
    regions = get_list_of_regions(grid)

    for region in regions:
        region_price = get_fence_price_for_region(region, using_perimeter)
        total += region_price
    
    return total

def part1():
    input = read_file_to_2d_list_of_chars(get_input_filepath(day=12))
    price = get_total_fence_prices(input)
    print(price)

def part2():
    input = read_file_to_2d_list_of_chars(get_input_filepath(day=12))
    price = get_total_fence_prices(input, using_perimeter=False)
    print(price)