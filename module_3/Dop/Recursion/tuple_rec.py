def fun(args):
    Summ = 0
    if isinstance(args, str):
        return len(args)
    elif isinstance(args, int):
        return args
    else:
        if args[0] != ():
            if len(args) > 1:
                Summ += fun(args[0])
                return Summ + fun(args[1:])
            else:
                return Summ + fun(args[0])
        else:
            return Summ + fun(args[1:])


print(fun((((), 1), 1, 2, 3, "asda", 3, (1, 3, 4, 4, (2, 3, 4)))))
