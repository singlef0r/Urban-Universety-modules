def riddle(number):
    list_numbers = [num + 1 for num in range(number - 1)]
    list_pairs = []
    for num_one in list_numbers:
        for num_two in list_numbers[num_one::]:
            if number % (num_one + num_two) == 0:
                list_pairs.append(f'{num_one}{num_two}')
    result = ''.join(list_pairs)
    return result


print(riddle(int(input())))
