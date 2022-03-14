import os
import sys
import pyautogui
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def is_template_in_image(img):
    return pyautogui.locateOnScreen(img, confidence=0.65) is not None

#needed because py autogui click doesnt register for first one only moves mouse
def right_click(x, y):
    pyautogui.click(x, y, button='right')
    pyautogui.click(x, y, button='right')

def left_click(x, y):
    pyautogui.click(x, y)
    pyautogui.click(x, y)

def hold_key(key, hold_time):
    pyautogui.keyDown(key)
    time.sleep(hold_time)
    pyautogui.keyUp(key);

def alt_p():
    pyautogui.keyDown("alt")
    pyautogui.press("p")
    pyautogui.keyUp("alt")

def reapir():
    alt_p()
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('repairlogo.png', confidence=0.8)
    left_click(x, y)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('repair.png', confidence=0.8)
    left_click(x, y)
    time.sleep(1)
    pyautogui.press('esc')
    pyautogui.press('esc')
    time.sleep(1)

def auto_fish():
    flag = "thrown"
    template = resource_path('punika.png')
    counter = 0

    print("Throw the fishing rod in and afk to get started")
    while(1):
        if flag == "pulled":
            print("throwing a fishing rod. Times done:", counter)
            pyautogui.press('e')
            flag = "thrown"
        
        elif flag == "thrown":
            if (is_template_in_image(template)):
                print("Time to fish!")
                pyautogui.press('e')
                flag = "pulled"
                counter+=1
                time.sleep(6)



def chaos_gunlancer():
    x, y = pyautogui.locateCenterOnScreen('statue.png', confidence=0.4)
    right_click(x, y)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('enter.png', confidence=0.8)
    left_click(x, y)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('accept.png', confidence=0.8)
    left_click(x, y)
    time.sleep(7)
    right_click(x, y)
    time.sleep(8)
    pyautogui.press('e')
    time.sleep(1)
    pyautogui.press('f')
    time.sleep(8)
    hold_key('s', 3.5)
    time.sleep(4)
    pyautogui.press('a')
    time.sleep(4)
    pyautogui.press('f')
    time.sleep(3)
    pyautogui.press('q')
    time.sleep(3)
    pyautogui.press('e')
    time.sleep(1.5)
    pyautogui.press('z')
    time.sleep(4)
    hold_key('s', 3.5)
    time.sleep(6)
    pyautogui.press('e')
    time.sleep(1)
    pyautogui.press('f')
    time.sleep(6)
    hold_key('s', 3.5)
    x, y = pyautogui.locateCenterOnScreen('leave.png', confidence=0.8)
    left_click(x, y)
    pyautogui.press('enter')
    time.sleep(15)


def auto_chaos():
    counter = 0
    print("Starting in 5 seconds. Tab back in the game and be near a chaos dungeon statue (punika if possible).")
    time.sleep(5)
    while(1):
        chaos_gunlancer()
        counter+=1
        print("Runs done:", counter)
        if (counter%5 == 0):
            repair()



def run_bot():    
    text = input("What would you like to do in Lost Ark? Current commands: [fish] [chaos (Gunlance Only)]\n")
    if text == "fish":
        auto_fish()
    elif text == "chaos":
        auto_chaos()

def main():
    run_bot()

if __name__ == "__main__":
    main()
