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
argv0         argv1    argv2     argv3         argv4        argv5      argv6*
restore.py    <pid>    <time>    <directory>   <relaunch>   <path>     <project>

pid: The PID of the parent process
time: The time to wait before restoring the project
directory: The project's parent directory
relaunch: Boolean stating if main program should be relaunched or not
path: If reopen is true, a path to main.py must be specified
project*: A dictionary containing the files in the project and its data

NOTE: Project was changed as an *args because Operative Systems have a
single-argument length limit, and given the fact we're passing entire
binary dumps of files, the length gets quite long, so this script will
received small chunks and add it all together.
"""

# Ignore SIGHUP
signal.signal(signal.SIGHUP, signal.SIG_IGN)

# Parse arguments into variables
pid = int(sys.argv[1])
time = float(sys.argv[2])
directory = sys.argv[3]
relaunch = bool("True" == sys.argv[4])
path = sys.argv[5]
del sys.argv[0:6]   # Clean argv list

# Add al project chunks into a single string
project = "".join(sys.argv)


# Wait for parent process to die
while os.getppid() == pid:
    sleep(0.5)

# Wait specified time
sleep(time)

# Create parent directory once again
if not os.path.exists(directory):
    os.mkdir(directory)

# Restore all the project's files
project = literal_eval(project)
Restore(project)

# Restart the main script if requested
if relaunch:
    subprocess.Popen(["python3", path])  # Not specifying path raises IndexError
