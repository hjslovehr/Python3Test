import os
import sys
sys.path.append('..\\common')
from helpers import *

@func_use_time
def create_files(count):
    for i in range(count):
        with open('.\\temp\\{0}_{0}_{0}.txt'.format(i), 'a+') as f:
            pass


if __name__ == "__main__":
    create_files(1000)
