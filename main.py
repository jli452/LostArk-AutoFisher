import logging
import os
import sys
import pyautogui
import time
from time import gmtime, strftime

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def is_template_in_image(img):
    return pyautogui.locateOnScreen(img, confidence=0.8) is not None

def run_bot():
    flag = "pulled"
    found = False
    template = resource_path('test1.png')
    counter = 0
    
    print(strftime("%H:%M:%S", gmtime()), "starting a bot")
    time.sleep(3)
    while(1):
        if flag == "pulled":
            print(strftime("%H:%M:%S", gmtime()), "throwing a fishing rod,", counter)
            pyautogui.press('e')
            flag = "thrown"
        
        elif flag == "thrown":
            if (is_template_in_image(template)):
                print(strftime("%H:%M:%S", gmtime()), "Time to fish!")
                pyautogui.press('e')
                flag = "pulled"
                counter+=1
                found = False
                time.sleep(6)
def main():
    run_bot()

if __name__ == "__main__":
    main()
