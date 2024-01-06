import multiprocessing
import random
# ДЛЯ БОЛЕЕ БЫСТРОГО ПАРСИНГА (СРАЗУ МНОГО СТРАНИЦ)
def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}] value: {value}")
    return name

def end_func(response):
    print("Задание завершено!")
    print(response)

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p: # для оптимизации, перезапуск процессов, если они уже выполнились
        # p.map(get_value, list(range(111)))
        p.map_async(get_value, list(range(100)), callback=end_func) #response is list, only 1 or 0 arg
        p.close()
        p.join()