import calc

def test_add(a, b):
    if calc.add(a, b) == a + b:
        print('This test compleat!')
    else:
        print('This test is fail!')

def test_sub(a, b):
    if calc.sub(a, b) == a - b:
        print('This test compleat!')
    else:
        print('This test is fail!')

def test_mul(a, b):
    if calc.mul(a, b) == a * b:
        print('This test compleat!')
    else:
        print('This test is fail!')

def test_div(a, b):
    if calc.div(a, b) == a / b:
        print('This test compleat!')
    else:
        print('This test is fail!')

if __name__ == '__main__':
    test_add(2, 5)
    test_sub(2, 2)
    test_mul(10, 11)
    test_div(54, 6)