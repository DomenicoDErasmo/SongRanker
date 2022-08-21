class SongArranger:

    def __init__(self, list_of_songs):
        self.list_of_songs = list_of_songs
        self.all_song_data = []
        self.ParseSongData()

    def UpdateSongData(self, list_of_songs):
        self.list_of_songs = list_of_songs

    def ParseSongData(self):
        self.all_song_data = []
        for line_num in range(len(self.list_of_songs)):
            self.all_song_data.append(self.list_of_songs[line_num].split("~"))

    def RankSongs(self):
        sorted_songs = sorted(self.all_song_data, key=lambda x: float(x[3]), reverse=True)
        return sorted_songs

    def UpdateArrangedSongs(self, list_of_songs):
        self.UpdateSongData(list_of_songs)
        self.ParseSongData()
        sorted_songs = self.RankSongs()
        return sorted_songs
