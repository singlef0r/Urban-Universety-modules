def calculate_structure_sum(args):
    Summa = 0
    if isinstance(args, str):
        return Summa + len(args)
    elif isinstance(args, int):
        return Summa + args
    elif isinstance(args, float):
        return Summa + args
    elif isinstance(args, bool):
        return 1 if args else 0
    elif isinstance(args, dict):
        for key, item in args.items():
            Summa += len(key) + calculate_structure_sum(args[key])
        return Summa
    elif isinstance(args, tuple):
        if args[0] != ():
            if len(args) > 1:
                Summa += calculate_structure_sum(args[0])
                return Summa + calculate_structure_sum(args[1:])
            else:
                return Summa + calculate_structure_sum(args[0])
        else:
            return Summa + calculate_structure_sum(args[1:])
    elif isinstance(args, set):
        return calculate_structure_sum(*args)
    else:
        if len(args) > 1:
            Summa += calculate_structure_sum(args[0])
            return Summa + calculate_structure_sum(args[1:])
        else:
            return Summa + calculate_structure_sum(args[0])


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

result = calculate_structure_sum(data_structure)
print(result)
