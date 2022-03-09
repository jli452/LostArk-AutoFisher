import numpy as np
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random

flag = "pulled"
found = False
template = cv2.imread("template.png")
method = cv2.TM_SQDIFF
counter = 0
threshold = .8

def is_template_in_image(img, templ):
    res = cv2.matchTemplate(img, templ, method)
    min_val = cv2.minMaxLoc(res)[0]
    return min_val <= threshold

print(strftime("%H:%M:%S", gmtime()), "starting a bot")
time.sleep(3)

while(1):
    if flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "throwing a fishing rod,", counter)
        pyautogui.press('e')
        flag = "thrown"
    
    if flag == "thrown":
        screenshot = pyautogui.screenshot()
        screenshot.save(r'C:\Users\liron\Downloads\fishbot\screenshot.png')
        screenshot = cv2.imread("screenshot.png")
        res = cv2.matchTemplate(screenshot, template, method)
        if (is_template_in_image(screenshot, template)):
            print(strftime("%H:%M:%S", gmtime()), "Time to fish!")
            pyautogui.press('e')
            flag = "pulled"
            counter+=1
            found = False
            time.sleep(200)
