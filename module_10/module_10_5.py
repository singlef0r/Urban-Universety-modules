import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line.strip())


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_start = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    time_finish = datetime.datetime.now()
    print(f'0:00:{time_finish - time_start} (линейный)')

    time_start = datetime.datetime.now()
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, filenames)
    time_finish = datetime.datetime.now()
    print(f'0:00:{time_finish - time_start} (многопроцессный)')
