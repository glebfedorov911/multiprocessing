import multiprocessing
import random


def end_func(response):
    print("end func:", response)

def out(x):
    print(f"value: {x}")
    return x

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p: # для оптимизации, перезапуск процессов, если они уже выполнились
        for i in range(10):
            p.apply_async(out, args=(i, ), callback=end_func) #response is element, 0 and more arg
        p.close()
        p.join()

