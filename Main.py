import sys
from threading import  Thread
import subprocess
import multiprocessing
import  os

def bye():
    os.close("check_CPU.py")

if __name__ == '__main__':
    os.startfile("check_CPU.py")
    os.startfile('app.py')


