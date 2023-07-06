import time
import sys

def zigzag_game(character):
    count = 0
    direction = "right"
    space = " " * count
    while True:
        sys.stdout.write(space + character*10 + '\r')
        sys.stdout.flush()
        time.sleep(1)
        
        if direction == "right":
            count += 1
            if count == 20:
                direction = "left"
        else:
            count -= 1
            if count == 0:
                direction = "right"

        space = " " * count
        
try:
    zigzag_game("****")
except KeyboardInterrupt:
    pass