import random
from multiprocessing import Process, Condition
import time

# в определенные (один раз)
# установил True, сделал задачу, False
cond = Condition()

def f1():
    while True:
        with cond:
            cond.wait()
            print("Получили событие")

def f2():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f"f2: {i}")
        time.sleep(1)

if __name__ == '__main__':
    Process(target=f1).start()
    Process(target=f2).start()