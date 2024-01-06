from multiprocessing.managers import BaseManager


BaseManager.register('ge1t')
manager = BaseManager(address=('127.0.0.1', 4444), authkey=b'abc')
print('client connected')
manager.connect()

res = manager.ge1t()
print("result:", res)