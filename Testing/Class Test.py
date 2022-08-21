import os

from CustomModules import SongFileReader, EloCalculator


project_path = os.path.dirname(os.path.dirname(__file__))
file_path = project_path + "/ResourceFiles/BTS_Song_Data"

file_reader = SongFileReader.SongFileReader(file_path)

song_data = file_reader.GetSongData("Intro: Singularity~")

print("Testing FindSongData:")
print(song_data)

# testing ELO system functionality

# rating_a and rating_b are current ELO ratings
rating_a = 1200
rating_b = 1000
K = 30
d = 1
rating_a, rating_b = EloCalculator.UpdateEloRating(rating_a, rating_b, K, d)
print("UpdateEloRating test:")
print("rating_a = ", rating_a, "rating_b = ", rating_b, "\n")

# must now test editing the file
# idea:
# 1. copy whole file to memory
# 2. change file in memory
#   a. search file for text of first song name, building
# 3. output as a new file
# 4. rename the new file to original

file_reader.ChangeElo("Trivia: Love", rating_a)
song_data = file_reader.GetSongData("Trivia: Love~")
print("ChangeElo test:")
print(song_data, "\n")
# Tests resetting all of ELO scores

file_reader.ResetElo()
song_data = file_reader.GetSongData("Trivia: Love~")
print("ResetElo test:")
print(song_data, "\n")
