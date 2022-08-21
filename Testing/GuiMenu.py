import os
import tkinter as tk
import random
from CustomModules import FileReader, SongFileReader, SongUpdater, MenuDisplay, SongComparison


class GuiMenu:

    def __init__(self):
        """
        Initializes the file readers used in the program.
        """

        # Gets our file paths components.
        project_path = os.path.dirname(os.path.dirname(__file__))
        song_file_path = "/ResourceFiles/BTS_Song_Data"
        settings_file_path = "/ResourceFiles/Settings"

        # Constructs the file paths.
        song_file = project_path + song_file_path
        settings_file = project_path + settings_file_path

        # Initializes the file readers based on the file paths provided.
        self.songs = SongFileReader.SongFileReader(song_file)
        self.settings = FileReader.FileReader(settings_file)

        # Initializes the song ranker
        self.songs.GetFileLines()
        self.song_arranger = SongUpdater.SongArranger(self.songs.list_of_lines)

        # Builds GUI button properties
        self.button_properties = \
            {
                "bg": "orchid1",
                "height": 3,
                "width": 20,
                "wraplength": 110
            }

        self.label_properties = \
            {
                "bg": "light goldenrod",
                "height": 3,
                "width": 20,
                "wraplength": 110
            }

    def GetKValue(self):
        """
        Gets the k value from settings.

        Returned Values:
            k_value -- The value for k determined in settings.
        """
        self.settings.GetFileLines()
        start_char = self.settings.list_of_lines[0].rfind(":")
        end_char = len(self.settings.list_of_lines[0])
        k_value = int(self.settings.list_of_lines[0][start_char + 1:end_char])
        return k_value

    def GetTwoRandomSongs(self):
        """
        Randomly selects two songs for the user to compare.

        Returned Values:
            left_song_data -- Data for the first song chosen.
            right_song_data -- Data for the second song chosen.

            Both left_song_data and right_song_data are structs consisting of the following fields of data:
                song_name -- The name of the song.
                album -- The album the song comes from.
                artist -- The artist that performs the song.
                elo -- The ELO score of the song, used for ranking songs.
        """
        # Determine two songs to compare based on line number
        left_song_pos = random.randrange(0, len(self.songs.list_of_lines) - 1, 1)
        right_song_pos = random.randrange(0, len(self.songs.list_of_lines) - 1, 1)

        # Ensures two distinct numbers
        while right_song_pos == left_song_pos:
            right_song_pos = random.randrange(0, len(self.songs.list_of_lines) - 1, 1)

        # Parse data for the two songs
        left_song_data = self.songs.list_of_lines[left_song_pos].split('~')
        right_song_data = self.songs.list_of_lines[right_song_pos].split('~')
        both_songs = [left_song_data, right_song_data]

        return both_songs

    def RankSongs(self):
        import SongComparisonGUI
        song_comparison = SongComparisonGUI.SongComparisonGUI()
        song_comparison.RunMenu()

    def ResetSongs(self):
        import SongResetGUI
        song_reset = SongResetGUI.SongResetGUI()
        song_reset.RunMenu()

    def ChangeKValue(self):
        import ChangeKValueGUI
        change_k = ChangeKValueGUI.ChangeKValueGUI()
        change_k.RunMenu()

    def ViewSong(self):
        import ViewSongGUI
        view_song = ViewSongGUI.ViewSongGUI()
        view_song.RunMenu()

    def BuildButtons(self, gui):
        rank_songs = tk.Button(gui, **self.button_properties, text="Rank Songs", command=self.RankSongs)
        change_k_value = tk.Button(gui, **self.button_properties, text="Change K Value", command=self.ChangeKValue)
        display_top_songs = tk.Button(gui, **self.button_properties, text="Display Top Songs", )
        view_song = tk.Button(gui, **self.button_properties, text="View Song", command=self.ViewSong)
        reset_song = tk.Button(gui, **self.button_properties, text="Reset Songs", command=self.ResetSongs)
        exit_button = tk.Button(gui, **self.button_properties, text="Exit", command=exit)

        rank_songs.place(x=0, y=50)
        change_k_value.place(x=0, y=105)
        display_top_songs.place(x=0, y=160)
        view_song.place(x=200, y=50)
        reset_song.place(x=200, y=105)
        exit_button.place(x=200, y=160)

    # TODO: add functions to BuildButtons and to class, replace all command line prompts with GUIs
    def RunMenu(self):
        gui = tk.Tk()
        gui.geometry("350x300")
        gui.configure(bg="powder blue")
        self.BuildButtons(gui)
        gui.mainloop()
