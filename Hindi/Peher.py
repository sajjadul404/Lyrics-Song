import sys
import time

lyrics = [
"Akhiyan tarse teri yaadon mai",
"Vekkhiyan bhar ke mukhra soniye",
"Rakheya noor kitne tu... dil che",
"Mahiye tu bata, tere bin ye",
"Peher nu peher mai",
"Tere shehar mai",
"Kese gujarenge ye raate",
"Ye lamhe bhi hamse",
"Kehne lage hai",
"Tere hi pyar ki vo baate",
]

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.16)
    print()