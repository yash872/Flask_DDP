

# def execute(cmd_path):
#     p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE)
#     out, err = p.communicate()
#     yield out.decode('utf-8')
  

import io
import subprocess
import sys
from subprocess import Popen, PIPE
def execute():
    proc = Popen([sys.executable, "-u", "demo.py"], stdout=PIPE, bufsize=1)
    for line in iter(proc.stdout.readline, b''):
        yield line
    proc.communicate()   



