import threading, random, time


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 100
        while counter:
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            number = random.randint(50, 500)
            self.balance += number
            print(f"Пополнение: {number}. Баланс: {self.balance} ")
            counter -= 1
            time.sleep(0.001)

    def take(self):
        counter = 100
        while counter:
            number = random.randint(50, 500)
            print(f"Запрос на {number} ")
            if number <= self.balance:
                self.balance -= number
                print(f"Снятие: {number}. Баланс: {self.balance} ")
            else:
                self.lock.acquire()
                print("Запрос отклонён, недостаточно средств ")
            time.sleep(0.001)
            counter -= 1


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
