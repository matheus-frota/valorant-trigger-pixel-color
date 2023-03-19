import time

import keyboard
from matplotlib import pyplot as plt
import numpy as np
import pyautogui as pag
import pygetwindow as gw
import win32api

from config import HEIGHT, WIDTH

def get_screeshot(type = 'all'):
    window = gw.getWindowsWithTitle('VALORANT')[0]

    left, top = window.topleft
    
    if type == 'all':
        return pag.screenshot(region=(left, top, WIDTH, HEIGHT))
    elif type == 'minor':
        return pag.screenshot(region=(left+WIDTH/2-5, top+HEIGHT/2+15, 30, 30))
    elif type == 'test':
        return pag.screenshot(region=(left+WIDTH/2-5, top+HEIGHT/2+15, 30, 70))


def check_key_pressed():
    if not (keyboard.is_pressed('w') or keyboard.is_pressed('a') or keyboard.is_pressed('s') or keyboard.is_pressed('d')):
        return False
    elif keyboard.is_pressed('1') or keyboard.is_pressed('2') or keyboard.is_pressed('3') or keyboard.is_pressed('f'):
        return True
    return False


def is_mouse_down():    # Returns true if the left mouse button is pressed
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0


def show_vision_trigger(arr):
    plt.imshow(arr, cmap='gray')
    plt.show()

while True:
    screen = get_screeshot('test')

    arr = np.array(screen)

    r = arr[:, :, 0]
    
    r[r >= 250] = 255
    r[r < 250] = 0

    r_sum = np.sum(r)
    r_mean = np.mean(r)
    r_median = np.median(r)
    r_std = np.std(r)
    print(f"Media: {r_mean} - Soma: {r_sum} - Mediana: {r_median} - Std: {r_std}")
    if (r_mean >= 5) and (r_mean < 20):
        pag.mouseDown()
        time.sleep(0.4)
        pag.mouseUp()
    