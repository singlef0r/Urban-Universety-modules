def calculate_structure_num_sum(number):
    Summ = 0
    if isinstance(number, str):
        return Summ + len(number)
    elif isinstance(number, int):
        return Summ + number
    else:
        for key, item in number.items():
            Summ += len(key) + calculate_structure_num_sum(number[key])
        return Summ




print(calculate_structure_num_sum({'cube': 7, 'drum': 8}))
