import os

from CustomModules import EloCalculator, FileReader, SongFileReader, SongUpdater

project_path = os.path.dirname(os.path.dirname(__file__))
song_file_path = "/ResourceFiles/BTS_Song_Data"
settings_file_path = "/ResourceFiles/Settings"

# Constructs the file paths.
song_file = project_path + song_file_path
settings_file = project_path + settings_file_path

# Building Song File Reader
song_reader = SongFileReader.SongFileReader(song_file)
song_reader.GetFileLines()

# Building Song Arranger
song_arranger = SongUpdater.SongArranger(song_reader.list_of_lines)
song_arranger.ParseSongData()

# Testing RankSongs
sorted_songs = song_arranger.RankSongs()
print(sorted_songs[0])

song_reader.ResetElo()
