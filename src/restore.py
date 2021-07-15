"""
Originally, both backup and restore process were performed in the
main script already loaded into memory without letting the process
die, but given the fact that every file is backed up in memory, in
order to optimize memory usage it's a better solution to start a
separate process with just the files loaded onto memory, as the
main script has a bunch of modules, libraries and functions.
"""

from ast import literal_eval
from file_utils import *
from time import sleep
import subprocess
import signal
import sys
import os

"""
argv0         argv1    argv2     argv3       argv4         argv5        argv6*
restore.py    <pid>    <time>    <project>   <directory>   <relaunch>   [path]

pid: The PID of the parent process
time: The time to wait before restoring the project
project: A dictionary containing the files in the project and its data
directory: The project's parent directory
relaunch: Boolean stating if main program should be relaunched or not
path*: If reopen is true, a path to main.py must be specified
"""


# Ignore SIGHUP
signal.signal(signal.SIGHUP, signal.SIG_IGN)

# Wait for parent process to die
pid = int(sys.argv[1])
while os.getppid() == pid:
    sleep(0.5)

# Wait specified time
time = float(sys.argv[2])    # Could potentially raise TypeError
sleep(time)

# Create parent directory once again
if not os.path.exists(sys.argv[4]):
    os.mkdir(sys.argv[4])

# Restore all the project's files
project = literal_eval(sys.argv[3])
Restore(project)

# Restart the main script if requested
relaunch: bool = (sys.argv[5] == "True")
if relaunch:
    path = sys.argv[6]
    subprocess.Popen(["python3", path])  # Not specifying path raises IndexError
