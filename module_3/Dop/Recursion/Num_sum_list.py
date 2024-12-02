def calculate_structure_num_sum(number):
    first = number[0]
    if len(number) > 1:
        return first + calculate_structure_num_sum(number[1:])
    else:
        return first


print(calculate_structure_num_sum([2, 4, 2, 4, 5]))
