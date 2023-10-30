import os
import sys
import time

def get369(unum:int) -> str:
    """
    This is a generator function.
    It takes an input (int) and convert into a string.
    If the number contains 3 or 6 or 9, it will clap(X)
    Otherwise it will return string converted from the number.

    README.md
    """

    snum = str(unum)
    count = 0

    # TODO: write a check logic
    for digit in snum:
        if digit == '3' or digit == '6' or digit == '9':
            count += 1

    if count == 0:
        return snum
    elif count == 1:
        return 'x'
    else:
        snum = ""
        for d in range(0,count):
            snum += 'x'
        return snum

    

if __name__ == '__main__':
    num_players = input("How many players are playing? ")
    num_players = int(num_players)

    round = 1
    
    # Assuming I am the always the first player
    while True:
        if round % num_players == 1: 
            # my turn
            unum = input("you: ")
            unum = unum.strip()
            if unum != get369(round):
                # TODO: Fix grammar bug in player order
                print(f"Ahahahah.. I won.  You should have {get369(round)}")
                sys.exit(0)
        else:
            time.sleep(1)
            print(f"player {round % num_players}: {get369(round)} ")
        round += 1



