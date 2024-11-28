def custom_write(file_name, strings):
    strings_positions = dict()
    number = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        number += 1
        strings_positions[(number, file.tell())] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
