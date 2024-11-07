def calculate_structure_sum(args):
    Summ = 0
    if isinstance(args, str):
        return Summ + len(args)
    elif isinstance(args, int):
        return Summ + args
    elif isinstance(args, dict):
        for key, item in args.items():
            Summ += len(key) + calculate_structure_sum(args[key])
    else:
        if len(args) > 1:
            Summ = calculate_structure_sum(args[0])
            return calculate_structure_sum(args[1:])
        else:
            return Summ


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

print(calculate_structure_sum(data_structure))
