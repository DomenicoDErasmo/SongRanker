from CustomModules import FileReader


class SongFileReader(FileReader.FileReader):

    def GetSongData(self, input_string):
        """
        Finds a string from the given file and returns all data from the line

        Keyword Arguments:
         input_string -- The text to search for. This is typically the song name, followed by a ~ to delimit easily.
         filename -- The name of the file that we search through.

        Returned Values:
            song_data -- A struct containing each song's information. This consists of the following fields:
                song_name -- The name of the song.
                album -- The album the song comes from.
                artist -- The artist that performs the song.
                elo -- The ELO score of the song, used for ranking songs.
                line_number -- The line number that input_string occurs at.
        """
        line_number = self.GetLineNumber(input_string)

        song_data = self.list_of_lines[line_number].split('~')
        song_data.append(line_number)

        return song_data

    def ChangeElo(self, song_data, new_elo):
        """
        Changes the ELO score of a given song

        Keyword Arguments:
            song -- The song to modify.
            new_elo -- The new ELO score that we assign to the given song.
        """
        song_input = song_data[0] + "~"

        line_number = self.GetLineNumber(song_input)

        self.list_of_lines[line_number] = song_data[0] + "~" + song_data[1] \
            + "~" + song_data[2] + "~" + str(new_elo) + "\n"

    def ResetElo(self):
        """
        Resets the ELO score of every song to 1000.
        """
        self.GetFileLines()

        for line in range(len(self.list_of_lines)):
            last_delimiter = self.list_of_lines[line].rfind("~")
            updated_line = self.list_of_lines[line][0:last_delimiter] + "~1000\n"
            self.list_of_lines[line] = updated_line
