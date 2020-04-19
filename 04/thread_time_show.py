import datetime
import time
import threading

def show_time():
    while True:
        print(datetime.datetime.now())
        time.sleep(0.01)
    pass


if __name__ == '__main__':
    threading.Thread(name='show time', target=show_time).start()
    pass


