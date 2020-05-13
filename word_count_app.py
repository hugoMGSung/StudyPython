import os

f = open("./data/yesterday_lyrics.txt")
lyrics = f.readlines()
f.close()

#print(lyrics)
contents = ""
for line in lyrics:
    contents = contents + line.strip() + "\n"

word_count = contents.upper().count("YESTERDAY")

print("Number of a word 'Yesterday' : {}".format(word_count))