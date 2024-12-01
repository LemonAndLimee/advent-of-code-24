INPUT_FILE = "day1_input.txt"

list1 = []
list2 = []

def place_in_ordered_position(number, list:list):
    index = 0
    while index < len(list) and number < list[index]:
        index += 1
    list.insert(index, number)

def get_total_of_differences(list_a, list_b):
    if len(list_a) != len(list_b):
        raise Exception("Lists must be same length")
    
    total = 0
    for i in range(len(list_a)):
        difference = abs(list_a[i] - list_b[i])
        total += difference
    
    return total

def get_number_of_occurrences(number, list):
    # assume list is ordered
    index = 0
    while index < len(list) and number != list[index]:
        index += 1
    
    if index == len(list):
        return 0
    
    # index now points to first occurence
    occurrences = 1
    index += 1
    while index < len(list) and number == list[index]:
        occurrences += 1
        index += 1
    
    return occurrences

with open(INPUT_FILE, 'r') as input_file:
    for line in input_file:
        line_items = line.split()
        place_in_ordered_position(int(line_items[0]), list1)
        place_in_ordered_position(int(line_items[1]), list2)

def part1():
    total = get_total_of_differences(list1, list2)
    print(total)

def part2():
    similarity_score = 0
    for number in list1:
        occurrences_in_list2 = get_number_of_occurrences(number, list2)
        similarity_score += (number * occurrences_in_list2)
    print(similarity_score)