def calculate_structure_str(number):
    str_number = ''.join([str(i) for i in number])
    first = str_number[0]
    if len(str_number) > 1:
        return first + calculate_structure_str(str_number[1:].split())
    else:
        return first


print(calculate_structure_str([1, 2, 3, 4]))
