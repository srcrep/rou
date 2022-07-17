from pynput.mouse import Button, Controller
import time
import pyautogui
import os

screen = pyautogui.screenshot()

black = r,g,b
red = r,g,b
green = r,g,b

def win(self):
    if pyautogui.pixelMatchesColor(x,y(r,g,b)) is True:
        win = True
    else:
        win = False

def loss(self):
    if pyautogui.pixelMatchesColor(x,y(r,g,b)) is False:
        loss = True
    else:
        loss = False

def bet(self):
    if win is True and loss is False:
        pyautogui.click(x=,y=)
    elif loss is True and win is False:
        pyautogui.click(x=,y=)
        time.sleep(0.5)
        pyautogui.click(x=,y=)
    else:
        break

