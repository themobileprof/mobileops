# Python 3
# Author: Samuel Anyaele - TheMobileprof.com
# scripts/help/modules/misc.py

import subprocess
import os
import time
from urllib.request import urlopen

# Check the Internet
def internet_on(url='https://github.com/'):
    try:
        response = urlopen(url, timeout=10)
        return True
    except:
        return False

# Check if App is installed
def which(app):
        return True if subprocess.run(['which', app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False

def current_dir():
    # Get current directory
    home_dir = os.path.expanduser("~")
    current_dir = os.getcwd()           
    return "~/" + os.path.relpath(current_dir,home_dir)

def short_wait():
    time.sleep(2)

def long_wait():
    time.sleep(4)

def breaker():
    print("####################")
    self.long_wait()

