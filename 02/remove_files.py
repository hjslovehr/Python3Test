import os
import sys
sys.path.append('..\\common')
from helpers import *

@func_use_time
def remove_files(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_name = os.path.join(dir, file)
            os.remove(file_name)


if __name__ == "__main__":
    remove_files('.\\temp')
