from src.process import Background
from src.file_utils import *
from src.window import *

from num2words import num2words
from tkinter import *
import subprocess
import sys
import os

# Keep track of the amount of times the project has died and recovered
suicide_count = 1
PARENT_DIR = sys.path[0]


window = Window()
window.title(f"Suicide Bomber The {num2words(suicide_count, to='ordinal').capitalize()}")
window.center()


# Let us commence forth
def CommitSuicide():
    # First backup all files in memory
    backup_thread = Background(target=Backup, args=(PARENT_DIR,))
    backup_thread.start()

    # Show audiovisual assets
    escubi = f"{PARENT_DIR}/res/escubi.mp3"
    explosion = f"{PARENT_DIR}/res/explosion.mp4"
    rebibis = f"{PARENT_DIR}/res/rebibis.jpg"

    # Display shaggy's image and play sound
    rebibis = window.display_image(rebibis)
    window.play_sound(escubi).wait_done()
    rebibis.destroy()

    # Play explosion video
    window.play_video(explosion)

    # Close the window
    window.destroy()
    
    # Wait for the thread to finish backing up files
    if backup_thread.is_alive():
        backup_thread.join()

    # Aquire the backed up project as a dict
    project = backup_thread.get_return_value()

    # Increase the suicide count
    main = f"{PARENT_DIR}/main.py"
    source: str = project[main].decode("utf-8")
    source = source.replace(f"suicide_count = {suicide_count}", f"suicide_count = {suicide_count + 1}")
    project[main] = source.encode("utf-8")

    # Call the restoration script
    # restore.py <pid> <time> <directory> <relaunch> <path> <project>
    project = str(project)
    project = [project[i:i + 10_000] for i in range(0, len(project), 10_000)]
    args = [str(os.getpid()), "7", PARENT_DIR, "True", f"{PARENT_DIR}/main.py", *project]
    subprocess.Popen(["python3", f"{PARENT_DIR}/src/restore.py", *args])

    # Then start recurively deleting the project's files
    Obliterate(PARENT_DIR)


# Bri'ish?!
button = Button(window, text="Don't click me")
button["command"] = lambda: [button.destroy(), CommitSuicide()]
button.pack(side=TOP, expand=YES)


window.mainloop()
