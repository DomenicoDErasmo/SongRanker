from CustomModules import EloCalculator, FileReader, SongFileReader


class SongComparison:

    def __init__(self, both_songs, all_songs, k_value):
        self.left_song_data, self.right_song_data = both_songs[0], both_songs[1]
        self.left_song_elo, self.right_song_elo = float(self.left_song_data[3]), float(self.right_song_data[3])
        self.songs = all_songs
        self.k_value = k_value

    def PromptPreferredChoice(self):
        print("1. " + self.left_song_data[0])
        print("2. " + self.right_song_data[0])
        result = input("Which song do you prefer? Type the number next to the song or type 3 to end: ")
        return result

    def LeftSongWins(self):
        self.left_song_elo, self.right_song_elo = \
            EloCalculator.UpdateEloRating(self.left_song_elo, self.right_song_elo, self.k_value, 1)

        self.songs.ChangeElo(self.left_song_data, self.left_song_elo)
        self.songs.ChangeElo(self.right_song_data, self.right_song_elo)
        self.songs.WriteChangesToFile()

    def RightSongWins(self):
        left_song_elo, right_song_elo = \
            EloCalculator.UpdateEloRating(self.left_song_elo, self.right_song_elo, self.k_value, 2)

        self.songs.ChangeElo(self.left_song_data, left_song_elo)
        self.songs.ChangeElo(self.right_song_data, right_song_elo)
        self.songs.WriteChangesToFile()

