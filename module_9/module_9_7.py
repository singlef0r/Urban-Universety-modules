def is_prime(func):
    def wrapper(*args):
        count = 0
        num = func(*args)
        for i in range(1, num):
            if num % i == 0:
                count += 1
        if count > 2:
            print("Составное")
        else:
            print("Простое")
        return num
    return wrapper


@is_prime
def sum_three(x, y, z):
    return x + y + z


result = sum_three(2, 3, 6)
print(result)
