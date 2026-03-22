import sys
import time

# 0:50 minute Start Lyrics
lyrics = [
    "I'm in love with the shape of you",
    "We push and pull like a magnet do",
    "Although my heart is falling too",
    "I'm in love with your body",
    "And last night you were in my room",
    "And now my bedsheets smell like you",
    "Every day discovering something brand new",
    "I'm in love with your body",
    "(Oh--I--oh--I--oh--I--oh--I)",
    "I'm in love with your body",
    "(Oh--I--oh--I--oh--I--oh--I)",
    "I'm in love with your body",
    "(Oh--I--oh--I--oh--I--oh--I)",
    "I'm in love with your body",
    "Every day discovering something brand new",
    "I'm in love with the shape of you",

]

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
    print()
