import sys
import time

# 0:50 minute Start Lyrics
print('"🎧 Now Playing: Tera Zikr"'+ " - Darshan Raval\n")
lyrics = [
    "Mujhe khone ke baad ik din",
    "Tum mujhe yaad karooooge   ",
    "Phir dekhna milne ki mujhse",
    "Tum fariyad karoooooge ....\n",

    "Mujhe khone ke baad ik din",
    "Tum mujhe yaad karooooge   ",
    "Phir dekhna milne ki mujhse",
    "Tum fariyad karoooooge .... \n",
]

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.16)
    print()