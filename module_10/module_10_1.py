import threading, time, datetime


def wite_words(word_count, file_name):
    with open(f'{file_name}', 'a', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_stop = datetime.datetime.now()

print(f'Работа потоков 0:00:{time_stop - time_start}')

time_start = datetime.datetime.now()

tread_one = threading.Thread(target=wite_words, args=(10, 'example5.txt'))

tread_two = threading.Thread(target=wite_words, args=(30, 'example6.txt'))

tread_free = threading.Thread(target=wite_words, args=(200, 'example7.txt'))

tread_four = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

tread_one.start()
tread_two.start()
tread_free.start()
tread_four.start()

tread_one.join()
tread_two.join()
tread_free.join()
tread_four.join()

time_stop = datetime.datetime.now()

print(f'Работа потоков 0:00:{time_stop - time_start}')
