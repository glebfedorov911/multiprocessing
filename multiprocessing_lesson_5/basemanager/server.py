from multiprocessing.managers import BaseManager
import time


def get_time():
    return time.time()

if __name__ == '__main__':
    BaseManager.register("ge1t", callable=get_time)
    manager = BaseManager(address=('', 4444), authkey=b'abc')
    server = manager.get_server()
    print('server start')
    server.serve_forever()