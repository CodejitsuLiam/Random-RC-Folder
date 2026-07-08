CURSOR_UP = "\033[1A"
CLEAR="\x1b[2K"
import time
time.sleep(0.5)
for e in range(999):
    print(CLEAR + CURSOR_UP, end="")