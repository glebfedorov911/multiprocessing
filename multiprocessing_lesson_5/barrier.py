import multiprocessing
import time
import random
from multiprocessing import Process, Barrier

# все процессы доходят до wait => выполняются -> выводится код ниже

def f1(bar):
    name = multiprocessing.current_process().name
    sleep = random.randint(2, 10)
    print(f"[{name}] - спим {sleep} секунд!")
    time.sleep(sleep)
    bar.wait()
    print(f"[{name}] - запущено!")

if __name__ == '__main__':
    b = Barrier(5) # 5 процессов, 3 процесса ожидают если всего 8 / выполняются только кратные указанному числу в классе
    for i in range(10):
        Process(target=f1, args=(b, )).start()