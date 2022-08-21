import os
from pathlib import Path
import tkinter as tk
import PIL.ImageTk
from PIL import Image, ImageTk
from CustomModules import SongComparison
import GuiMenu


class SongComparisonGUI(GuiMenu.GuiMenu):
    def __init__(self):
        GuiMenu.GuiMenu.__init__(self)
        self.left_image = None
        self.right_image = None
        self.menu = None

    def BuildImage(self, song: list) -> PIL.ImageTk.PhotoImage:
        image_name = os.path.splitext(song[1])[0]
        path = Path(os.getcwd()).parent / "ResourceFiles\\Album Covers" / (image_name + ".jpg")
        return ImageTk.PhotoImage(Image.open(path).resize((150, 150)))

    def BuildImages(self, both_songs: list):
        left_image_name = os.path.splitext(both_songs[0][1])[0]
        left_path = Path(os.getcwd()).parent / "ResourceFiles\\Album Covers" / (left_image_name + ".jpg")
        self.left_image = ImageTk.PhotoImage(Image.open(left_path).resize((150, 150)))

        right_image_name = os.path.splitext(both_songs[1][1])[0]
        right_path = Path(os.getcwd()).parent / "ResourceFiles\\Album Covers" / (right_image_name + ".jpg")
        self.right_image = ImageTk.PhotoImage(Image.open(right_path).resize((150, 150)))

    def SelectLeftSong(self, both_songs, left):
        song_comparison = SongComparison.SongComparison(both_songs, self.songs, self.GetKValue())
        if left:
            song_comparison.LeftSongWins()
        else:
            song_comparison.RightSongWins()
        self.RunMenu()

    # TODO: refactor eventually (but this works as is)
    def BuildMenu(self):
        self.menu = tk.Toplevel()
        self.menu.geometry("500x500")
        both_songs = self.GetTwoRandomSongs()
        self.BuildImages(both_songs)

        header_frame = tk.Frame(self.menu, bg="light blue", width=500, height=100)
        header_frame.place(x=0, y=0)

        left_song_frame = tk.Frame(self.menu, bg="pale green", width=250, height=300)
        left_song_frame.place(x=0, y=100)

        left_canvas = tk.Canvas(left_song_frame, width=150, height=150)
        left_canvas.create_image(0, 0, image=self.left_image, anchor="nw")
        left_canvas.place(x=0, y=0)

        left_song_info = \
            tk.Label(left_song_frame, **self.label_properties,
                     text=both_songs[0][2] + ": " + both_songs[0][1])
        left_song_info.place(x=0, y=194)

        left_song_button = \
            tk.Button(left_song_frame, **self.button_properties,
                      text=both_songs[0][0], command=lambda: self.SelectLeftSong(both_songs, True))
        left_song_button.place(x=0, y=244)

        right_song_frame = tk.Frame(self.menu, bg="pale green", width=250, height=300)
        right_song_frame.place(x=250, y=100)

        right_canvas = tk.Canvas(right_song_frame, width=150, height=150)
        right_canvas.create_image(0, 0, image=self.right_image, anchor="nw")
        right_canvas.place(x=95, y=0)

        right_song_info = tk.Label(right_song_frame, **self.label_properties,
                                   text=both_songs[1][2] + ": " + both_songs[1][1])
        right_song_info.place(x=105, y=194)

        right_song_button = \
            tk.Button(right_song_frame, **self.button_properties,
                      text=both_songs[1][0], command=lambda: self.SelectLeftSong(both_songs, False))
        right_song_button.place(x=105, y=244)

        footer_frame = tk.Frame(self.menu, bg="light blue", width=500, height=100)
        footer_frame.place(x=0, y=400)

        exit_button = tk.Button(footer_frame, **self.button_properties, text="Exit", command=self.menu.destroy)
        exit_button.place(x=351, y=45)

    def RunMenu(self):
        if self.menu:
            self.menu.destroy()
        self.BuildMenu()
        self.menu.mainloop()
