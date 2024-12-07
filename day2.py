import utils

reports = []

def is_report_safe_part1(report:list) -> bool:
    is_increasing = None
    for i in range(len(report)):
        level = report[i]
        if i > 0:
            previous_level = report[i-1]
            diff = level - previous_level
            
            if diff > 0:
                if is_increasing == None:
                    is_increasing = True
                elif is_increasing == False:
                    return False
            elif diff < 0:
                if is_increasing == None:
                    is_increasing = False
                elif is_increasing == True:
                    return False
            else:
                return False
            
            abs_diff = abs(diff)
            if abs_diff < 1 or abs_diff > 3:
                return False
    
    return True

def try_removing_level(report:list, index:int) -> bool:
    copy_report = report.copy()
    copy_report.pop(index)
    return is_report_safe_part1(copy_report)

def is_report_safe_part2(report:list) -> bool:
    if is_report_safe_part1(report):
        return True
    else:
        for i in range(len(report)):
            if try_removing_level(report, i):
                return True
        return False
            

with open(utils.get_input_filepath(day=2), 'r') as input_file:
    for line in input_file:
        line_items = line.split()
        levels = []
        for item in line_items:
            levels.append(int(item))
        reports.append(levels)

def part1():
    safe_reports = 0
    for report in reports:
        if is_report_safe_part1(report):
            safe_reports += 1
    print(safe_reports)

def part2():
    safe_reports = 0
    for report in reports:
        if is_report_safe_part2(report):
            safe_reports += 1
    print(safe_reports)