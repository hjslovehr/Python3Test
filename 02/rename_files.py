import os
import sys
sys.path.append('..\\common')
from helpers import *

@func_use_time
def rename_files(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            new_filename = dir + '\\' + file.split('_')[2]
            os.rename(dir + '\\' + file, new_filename)


if __name__ == "__main__":
    rename_files(r'.\temp')

