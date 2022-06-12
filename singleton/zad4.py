
import multiprocessing


class Singleton:

    def __init__(*args,**kwargs):
        if not shared_state:
            with shared_state_lock:
                shared_state['x'] = 1
                shared_state['y'] = 2


def task():
    a = Singleton()


if __name__ == '__main__':
    shared_state = multiprocessing.Manager().dict()
    shared_state_lock = multiprocessing.Lock()

    pro_1 = multiprocessing.Process(target=task)
    pro_2 = multiprocessing.Process(target=task)
    pro_1.start()
    pro_2.start()

    pro_1.join()
    pro_2.join()
