import tkinter as tk
import GuiMenu


class ViewSongGUI(GuiMenu.GuiMenu):
    def __init__(self):
        GuiMenu.GuiMenu.__init__(self)
        self.menu = tk.Toplevel()
        self.menu.geometry("500x500")

    def QuerySong(self):
        return

    def RunMenu(self):
        label = tk.Label(self.menu, **self.label_properties, text="Enter Song:")
        label.place(x=10, y=40)
        submit = tk.Button(self.menu, **self.button_properties, text="Submit", command=self.QuerySong)
        submit.place(x=200, y=100)
