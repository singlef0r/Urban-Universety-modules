first = 'Мама мыла раму'
second = 'Рамена мало было'

list_one = list(map(lambda a, b: a == b, first, second))
print(list_one)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f'{data_set}\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        import random
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

