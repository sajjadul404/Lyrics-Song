import sys
import time


lyrics = [
    "Mujhe khone ke baad ik din",
    "Tum mujhe yaad karoge ....",
    "Phir dekhna milne ki mujhse",
    "Tum fariyad karoooooge ....\n",

    "Mujhe khone ke baad ik din",
    "Tum mujhe yaad karoge ....",
    "Phir dekhna milne ki mujhse",
    "Tum fariyad karoooooge .... \n",
]

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.16)
    print()