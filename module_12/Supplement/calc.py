import logging


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a, b):
    try:
        a / b
        logging.info(f"Число {a} успешно разделилось на {b}")
        return a / b
    except:
        logging.error('Не получилось!', exc_info=True)
        return 0

def sqrt(a):
    try:
        a**0.5
        logging.info(f'Корень из числа {a} успешно вычислен!')
        return a**0.5
    except:
        logging.error('Не получилось извлечь корень!', exc_info=True)
        return 0


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='py.log', filemode='w',
                        format="%(asctime)s | %(levelname)s | %(message)s", encoding='utf-8')
    print(div(4, 2))
    print(div(2, 0))
    print(sqrt(4))
    print(sqrt(-4))
    print(sqrt(0))
    print(add(100, 2))