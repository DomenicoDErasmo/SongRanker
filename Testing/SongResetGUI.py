import tkinter as tk
import GuiMenu


class SongResetGUI(GuiMenu.GuiMenu):
    def __init__(self):
        GuiMenu.GuiMenu.__init__(self)
        self.menu = tk.Toplevel()

    def ResetAll(self):
        self.songs.ResetElo()
        self.songs.WriteChangesToFile()
        self.menu.destroy()

    def RunMenu(self):
        self.menu.geometry("500x500")

        header_frame = tk.Frame(self.menu, bg="light blue", width=500, height=100)
        header_frame.place(x=0, y=0)

        confirmation = tk.Label(header_frame, text="Are you sure you want to reset all songs?")

        left_frame = tk.Frame(self.menu, bg="pale green", width=250, height=300)
        left_frame.place(x=0, y=100)

        yes_button = tk.Button(left_frame, text="Yes", command=self.ResetAll)
        yes_button.place(x=0, y=0)

        right_frame = tk.Frame(self.menu, bg="pale green", width=250, height=300)
        right_frame.place(x=250, y=100)

        yes_button = tk.Button(right_frame, text="No", command=self.menu.destroy)
        yes_button.place(x=0, y=0)

        footer_frame = tk.Frame(self.menu, bg="light blue", width=500, height=100)
        footer_frame.place(x=0, y=400)

        self.menu.mainloop()
