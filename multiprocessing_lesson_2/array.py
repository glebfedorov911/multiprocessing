import multiprocessing
import random
import time


def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f"array[{index}] = {num}, time = {vtime}")
        time.sleep(num)

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    arr = multiprocessing.Array("i", range(10))
    processes = []

    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(lock, arr, i))
        processes.append(pr)
        pr.start()

    for i in processes:
        i.join()

    print(list(arr))