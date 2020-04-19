import datetime
import time

def show_time():
    while True:
        print(datetime.datetime.now())
        time.sleep(1)

if __name__ == "__main__":
    show_time()

