import multiprocessing


lock = multiprocessing.RLock()
# разблокирует тот кто блокирует
def get_value(lck: multiprocessing.RLock):
    lck.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Процесс [{pr_name}] запущен')
    lck.release()

if __name__ == '__main__':
    multiprocessing.Process(target=get_value, args=(lock, ), name='pr1').start()
    multiprocessing.Process(target=get_value, args=(lock, ), name='pr2').start()
