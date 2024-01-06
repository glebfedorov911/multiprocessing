import multiprocessing
import time


def test():
    for _ in range(3):
        print(f"{multiprocessing.current_process().name}", time.time())
        time.sleep(1)

if __name__ == '__main__':
    # pr.start()

    # time.sleep(5)
    # print(pr.pid)
    # pr.terminate() # stop

    prc = []
    for i in range(3):
        pr = multiprocessing.Process(target=test, name=f'prc-{i}', daemon=True)
        prc.append(pr)
        pr.start()

    for i in prc:
        i.join()

    print("123312312")