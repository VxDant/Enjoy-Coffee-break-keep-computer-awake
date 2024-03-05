import time

import pyautogui
from random import randrange


while True:
    x = randrange(-20, 21)  # random number from -20 to 20
    y = randrange(-20, 21)  # random number from -20 to 20
    pyautogui.move(x, y)  # move your mouse cursor
    time.sleep(5)

