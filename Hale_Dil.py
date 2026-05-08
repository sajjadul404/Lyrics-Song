import sys
import time

# 0:50 minute Start Lyrics
print("\n\033[34m🎧 Now Playing: Tera Zikr - Darshan Raval\033[0m\n")
lyrics = [
    
"Haal e dil tujhko sunata",
"Dil agar yeh bol paata",
"Bakhuda tujhko hai chahta jaa aaa aaa aan\n",

"Tere sang jo pal bitaata",
"Waqt se main woh maang lata",
"Yaad karke muskuraata haan",
"Woo… ooo woooo.\n"
]

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.14)
    print()