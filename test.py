# data_structure = [[1, 2, 3],
#                   {'a': 4, 'b': 5},
#                   (6, {'cube': 7, 'drum': 8}),
#                   "Hello",
#                   ((), [{(2, 'Urban', ('Urban2', 35))}])
#                   ]

def calculate_structure_sum(args):
    Summ = 0
    if isinstance(args, str):
        return Summ + len(args)
    elif isinstance(args, int):
        return Summ + args
    else:
        first = args[0]
        if isinstance(first, list):
            second = first[0]
            if len(first) > 1:
                Summ += second + calculate_structure_sum(first[1:])
        elif isinstance(args, tuple):
            Summ += first + calculate_structure_sum(args[1:])
        elif isinstance(args, dict):
            for key, item in first.items():
                Summ += len(key) + calculate_structure_sum(first[key])
        elif isinstance(args, set):
            return Summ + calculate_structure_sum(first[1:])
    return calculate_structure_sum(args[1:])



print(calculate_structure_sum([[1, 2, 3],
                               {'a': 4, 'b': 5},
                               (6, {'cube': 7, 'drum': 8}),
                               "Hello"]))
