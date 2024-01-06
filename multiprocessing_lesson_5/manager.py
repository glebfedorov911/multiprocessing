import multiprocessing
import time
import random
from multiprocessing import Process, Manager


def f(m_dict, m_array):
    m_dict['name'] = 'test'
    m_dict['version'] = '1.0'
    m_dict['f1'] = True
    m_array.append(1)
    m_array.append(2)

def f2(m_dict, m_array):
    m_dict['f2'] = True
    m_dict['version'] = '2.0'
    m_array.append(3)
    m_array.append(4)

if __name__ == '__main__':
    with Manager() as m:
        d = m.dict()
        l = m.list()
        process = [Process(target=f, args=(d, l, )), Process(target=f2, args=(d, l, ))]

        for i in process:
            i.start()
            i.join()

        print("dict:", d)
        print("list:", l)