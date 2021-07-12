from PIL import Image as Img, ImageTk
from pydub.playback import play
from num2words import num2words
from pydub import AudioSegment
from tkinter import *
import tkvideo
import time
import sys
import os


suicide_count = 6

PARENT_DIR = sys.path[0]

window = Tk()
window.title(f"Suicide Bomber The {num2words(suicide_count, to='ordinal').capitalize()}")

width = 900
height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))


rebibis = None
rebibis_holder = None


def PlayShaggy():
    global PARENT_DIR
    global window
    global rebibis
    global rebibis_holder

    rebibis = ImageTk.PhotoImage(Img.open(f"{PARENT_DIR}/res/rebibis.jpg"))
    rebibis_holder = Label(window, image=rebibis)
    rebibis_holder.pack(side=TOP, expand=YES)

    play(AudioSegment.from_mp3(f"{PARENT_DIR}/res/escubi.mp3"))
    rebibis_holder.destroy()
    window.update()


holder = Label(window)
player = tkvideo.tkvideo(f"{PARENT_DIR}/res/explosion.mp4", holder, loop=0, size=(int(width), int(height)))


def Kamikaze():
    global PARENT_DIR
    global window
    global holder
    global player

    holder.pack(side=TOP, expand=YES)
    player.play()

    window.update()


def Magic():
    global PARENT_DIR

    source_path = f"{PARENT_DIR}/fuaLaRebibis_{suicide_count}.py"
    escubi_mp3_path = f"{PARENT_DIR}/res/escubi.mp3"
    explosion_mp4_path = f"{PARENT_DIR}/res/explosion.mp4"
    rebibis_jpg_path = f"{PARENT_DIR}/res/rebibis.jpg"
    paths = [source_path, escubi_mp3_path, explosion_mp4_path, rebibis_jpg_path]

    source = Backup(source_path).decode("utf-8")
    source = source.replace(f"suicide_count = {suicide_count}", f"suicide_count = {suicide_count + 1}").encode("utf-8")

    escubi_mp3 = Backup(escubi_mp3_path)
    explosion_mp4 = Backup(explosion_mp4_path)
    rebibis_jpg = Backup(rebibis_jpg_path)
    backups = (source, escubi_mp3, explosion_mp4, rebibis_jpg)

    os.system("rm -rf ./*")
    time.sleep(7)
    os.system("mkdir res")
    paths[0] = source_path.replace(str(suicide_count), str(suicide_count + 1))
    paths = tuple(paths)

    for i, j in zip(paths, backups):
        Restore(i, j)


button = Button(window, text="No me presiones")

button["command"] = lambda: [button.destroy(), PlayShaggy(), Kamikaze(), window.destroy()]  # , Magic()]
button.pack(side=TOP, expand=YES)


window.mainloop()
