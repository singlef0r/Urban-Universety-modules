def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('1', 2, 3)
print_params(3, 'привет', False)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [True, 234, "for"]
values_dict = {"a": 2, "b": "Строка", "c": True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [32, "не строка"]
print_params(*values_list_2, 42)
