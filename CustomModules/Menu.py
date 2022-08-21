import os
import random

from CustomModules import FileReader, SongFileReader, SongUpdater, MenuDisplay, SongComparison


class Menu:

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

    def CompareSongs(self):
        """
        Provides two songs for the user to compare, recalculating ELO scores as needed.
        """
        k_value = self.GetKValue()
        comparing_songs = True

        while comparing_songs:

            both_songs = self.GetTwoRandomSongs()
            song_comparison = SongComparison.SongComparison(both_songs, self.songs, k_value)
            choosing_preferred_song = True

            while choosing_preferred_song:
                result = song_comparison.PromptPreferredChoice()

                if result == "1":
                    song_comparison.LeftSongWins()
                    choosing_preferred_song = False

                elif result == "2":
                    song_comparison.RightSongWins()
                    choosing_preferred_song = False

                elif result == "3":
                    choosing_preferred_song = False
                    comparing_songs = False
                else:
                    print("Wrong input. Try again.\n")

    def ChangeKValue(self):
        """
        Modifies the K value in settings. The K value is used in the ELO calculation
            to change the impact of wins or losses.
        """

        # Initialization.
        new_k = input("Set a new k value: ")
        self.settings.GetFileLines()

        # Making changes to k value.
        k_value = self.settings.GetLineNumber("k-value")
        field_end = self.settings.list_of_lines[k_value].rfind(":")
        self.settings.list_of_lines[k_value] = self.settings.list_of_lines[k_value][0:(field_end + 1)] + new_k

        # Committing changes to file.
        self.settings.WriteChangesToFile()

    def DisplayTopSongs(self):
        """
        Views the top number of songs. The exact number is determined by the program user.
        """
        num_songs = input("How many songs do you want to view?\n")
        ranked_songs = self.song_arranger.UpdateArrangedSongs(self.songs.list_of_lines)
        for rank in range(int(num_songs)):
            print(str(rank + 1) + ". " + str(ranked_songs[rank]))

    def ViewSpecificSong(self):
        """
        Views data of a specified song.
        """

        # Initialization.
        desired_song = input("What song do you want to view?\n") + "~"
        song_data = self.songs.GetSongData(desired_song)

        # Output.
        print("Song: " + song_data[0])
        print("Album: " + song_data[1])
        print("Artist: " + song_data[2])
        print("ELO: " + song_data[3])

    def ResetSongs(self):
        confirmation = input("Type 'yes' without quote marks to confirm song ELO reset: ")
        if confirmation == "yes":
            self.songs.ResetElo()
            self.songs.WriteChangesToFile()

    def RunMenu(self):
        """
        Generates a menu with options for the program user to select.
        """

        # Initializing commands.
        menu_commands = {
            "Compare Songs": self.CompareSongs,
            "Change K Value": self.ChangeKValue,
            "Display Top Songs": self.DisplayTopSongs,
            "View Song": self.ViewSpecificSong,
            "Reset Songs": self.ResetSongs
        }
        program_is_running = True
        while program_is_running:
            input_command = MenuDisplay.PromptInput()
            if input_command == "Exit":
                print("\nGoodbye!\n")
                program_is_running = False
            elif input_command not in menu_commands:
                print("\nInvalid command. Please try again.\n")
            else:
                menu_commands[input_command]()
