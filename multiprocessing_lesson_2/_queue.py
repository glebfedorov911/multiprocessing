import multiprocessing
import time
import random

def get_text(q: multiprocessing.Queue):
    val = random.randint(0, 10)
    q.put(str(val))


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    processes = []
    for _ in range(10):
        pr = multiprocessing.Process(target=get_text, args=(queue,))
        processes.append(pr)
        pr.start()

    for i in processes:
        i.join()

    for elem in iter(queue.get, None):
        print(elem)