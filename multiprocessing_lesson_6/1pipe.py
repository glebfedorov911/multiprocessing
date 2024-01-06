import multiprocessing
import time
from multiprocessing import Pipe


def send_data(conn, msg):
    conn.send(msg)
    conn.close()

if __name__ == '__main__':
    output_c, input_c = Pipe()
    multiprocessing.Process(target=send_data, args=(input_c, 'hello', )).start()
    multiprocessing.Process(target=send_data, args=(input_c, 'world', )).start()
    print("data:", output_c.recv())#hello
    print("data:", output_c.recv())#world
    print("data:", output_c.recv()) # пустой если всего два процесса, а в них по 1 выводу
