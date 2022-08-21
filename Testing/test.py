from CustomModules import FileReader
from CustomModules import EloCalculator

# testing File IO from another file
new_path = FileReader.GetFilePath()

song_data = FileReader.FindString("Trivia: Love~", new_path)
print("FindString test:")
print(song_data, "\n")

# testing ELO system functionality

# rating_a and rating_b are current ELO ratings
rating_a = 1200.00
rating_b = 1000.00
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

FileReader.ChangeElo("Trivia: Love", rating_a)
song_data = FileReader.FindString("Trivia: Love~", new_path)
print("ChangeElo test:")
print(song_data,"\n")
# Tests resetting all of ELO scores

FileReader.ResetElo()
song_data = FileReader.FindString("Trivia: Love~", new_path)
print("ResetElo test:")
print(song_data,"\n")
