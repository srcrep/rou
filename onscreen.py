from pynput.mouse import Button, Controller
import pyautogui
import time
import os

def screenshot(self):
        self.__screenshot = pyautogui.screenshot('settings/my_screenshot.png')



loop1 = True
while loop1 is True:
    roundCheck = feedbackScreen( coord.roundDone)
    if roundCheck > 18700:
        loop1 = False
    else:
        loop1 = True
        if feedbackScreen(coord.placeBet) == 16587:
            click(x,y)


loop2 = True
while loop2 is True:
    print(feedbackScreen(coord.Results))
    if results(feedbackScreen(coord.Results)) == 1:
        looStreak = 1
        print(lossStreak)
        loop2 = False
    elif results(feedbackScreen(coord.Results)) == 2 :
        lossStreak = lossStreak + 1
        print(lossStreak)
        loop2 = False
    else:
        loop2 = True
        print("Waiting on Results")