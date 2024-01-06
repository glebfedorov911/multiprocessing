import random
from multiprocessing import Process, Event
import time
#все и сразу
#True, сделал задачу, True...
event = Event()

def test():
    print('func test start')
    while True:
        event.wait()
        print("test")
        time.sleep(1)

def test_event():
    while True:
        time.sleep(2)
        event.set()
        print('Event True')
        time.sleep(5)
        event.clear()
        print('Event False')


if __name__ == '__main__':
    Process(target=test).start() # во время процесса event.set()
    Process(target=test_event).start()
