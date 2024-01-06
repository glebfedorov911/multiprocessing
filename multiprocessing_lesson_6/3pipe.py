import multiprocessing
import time
from multiprocessing import Pipe


def getter(pipe):
    out, inp = pipe
    inp.close()
    while True:
        try:
            print("data:", out.recv())
        except:
            break

def setter(sequence, input_c):
    for item in sequence:
        time.sleep(1)
        input_c.send(item)

if __name__ == '__main__':
    output_c, input_c = Pipe()
    g = multiprocessing.Process(target=getter, args=((output_c, input_c), ))
    g.start()
    output_c.close()
    setter(list(range(10)), input_c)
    input_c.close()
    g.join()