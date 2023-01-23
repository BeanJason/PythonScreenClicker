# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):w
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pyautogui
import time
import random

def press_key(key, n_times = 1):
    for _ in range(n_times):
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)

buttons = ["w", "a", "s", "d", "z", "x"];

def getRand():
    rand = random.randint(0, 5);
    return rand

def getButtonClick(number, arr):
    return(arr[number])

def pressRandKey():
    key = getButtonClick(getRand(), buttons)
    press_key(key, 1)
    print('Button sent ', getButtonClick(getRand(), buttons))

def move_unit(left=0,right=0,up=0,down=0):
    ret_list = [left,right,up,down]
    if left>right:
        press_key('a', left-right)
    elif right>left:
        press_key('d', right-left)
    if up>down:
        press_key('w', up-down)
    elif down>up:
        press_key('s', down-up)
    press_key("'")
    time.sleep(0.2)
    return ret_list

#select emulator
# pyautogui.moveTo(15, 70, 0.2)
# pyautogui.click()
# time.sleep(0.3)

count = 0
timeElapsed = 0.0
# for x in range(10000):
#     print("Input #: ", count)
#     pressRandKey()
#     count+=1
#     time.sleep(0.7)
#     timeElapsed+=0.7
#     print("~Time Elapsed: ", timeElapsed)

for x in range(10):

    pressRandKey()



