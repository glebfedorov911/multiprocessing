import multiprocessing
import time
from multiprocessing import Pipe


def send_data(conn, msg):
    conn.close()
    conn.send(msg)

def send_data2(conn, msg):
    conn.send(msg)

if __name__ == '__main__':
    output_c, input_c = Pipe()
    multiprocessing.Process(target=send_data, args=(input_c, 'hello', )).start()
    multiprocessing.Process(target=send_data2, args=(input_c, 'world', )).start()
    print("data:", output_c.recv())
