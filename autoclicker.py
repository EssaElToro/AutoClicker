import pyautogui
import time
import keyboard
import sys

def click():
    time.sleep(0.01)
    pyautogui.click()
    #pyautogui.mouseDown()
def main():
    while not keyboard.is_pressed('r'):
        click()
    #pyautogui.mouseUp()

keyboard.add_hotkey("e", lambda: main())

keyboard.wait("esc")