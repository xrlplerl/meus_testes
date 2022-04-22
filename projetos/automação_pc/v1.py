import pyautogui, os, time

#teste de automação v1
pyautogui.press("winleft")
time.sleep(2)
pyautogui.write("chrome")
time.sleep(4)
pyautogui.press("enter")
time.sleep(4)
pyautogui.hotkey("ctrl","shift","n")
time.sleep(2)
pyautogui.write("http://github.com/xrlp/f")
pyautogui.press("enter")