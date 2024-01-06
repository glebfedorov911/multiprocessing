import multiprocessing
import random


def endfunc(response):
    print("end func:", response)

def out(x, y, z):
    print(f"value: {x} {y} {z}")
    return x, y, z

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p: # для оптимизации, перезапуск процессов, если они уже выполнились
        # p.starmap(out, [(1, 2, 3), (4, 5, 6)]) # in tuple all args func
        p.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=endfunc) # in tuple all args func
        p.close()
        p.join()