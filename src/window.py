from PIL import Image as Img
from pydub.playback import _play_with_simpleaudio
from pydub import AudioSegment
from PIL import ImageTk
from tkinter import *
import tkvideo
import cv2


class Window(Tk):
    def center(self, width: int = 900, height: int = 500):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    @staticmethod
    def play_sound(path):
        return _play_with_simpleaudio(AudioSegment.from_file(path))

    def play_video(self, filename: str):
        # Create a holder for the video
        holder = Label(self)
        holder.pack(side=TOP, expand=YES)

        # Create the video player
        player = tkvideo.tkvideo(filename, holder, loop=0, size=(self.winfo_width(), self.winfo_height()))
        player.play()

        # Calculate the duration of the video
        video = cv2.VideoCapture(filename)
        fps = video.get(cv2.CAP_PROP_FPS)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = int(frame_count / fps) * 1000
        video.release()

        # Start playing the video's sound
        audio = self.play_sound(filename)

        # Schedule frame for deletion and audio for stopping when video ends
        self.after(duration, func=lambda: [holder.destroy(), audio.stop()])

    def display_image(self, filename, duration=0):
        image = ImageTk.PhotoImage(Img.open(filename))
        image_holder = Label(self, image=image)
        image_holder.pack(side=TOP, expand=YES)
        self.update()

        if duration > 0:
            self.after(duration, func=image_holder.destroy)

        elif duration < 0:
            raise ValueError("Duration must be greater or equal to 0")

        return image_holder
