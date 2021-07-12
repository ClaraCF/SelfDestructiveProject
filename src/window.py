from tkinter import *
import tkvideo


class Window(Tk):
    def center(self, width: int = 900, height: int = 500):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def play_video(self, path: str):
        holder = Label(self)
        player = tkvideo.tkvideo(path, holder, loop=0, size=(self.winfo_height(), self.winfo_width()))

        holder.pack(side=TOP, expand=YES)
        player.play()

        return holder
