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


def is_mouse_down():    # Returns true if the left mouse button is pressed
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0


def show_vision_trigger(arr):
    plt.imshow(arr, cmap='gray')
    plt.show()


def descriptive_statistics(arr, show: bool = False):
    r_sum, r_mean, r_median, r_std = np.sum(arr), np.mean(arr), np.median(arr), np.std(arr)
    if show:
        print(f"Media: {r_mean} - Soma: {r_sum} - Mediana: {r_median} - Std: {r_std}")
    return np.sum(arr), np.mean(arr), np.median(arr), np.std(arr)


def enemy(r_mean):
    return (r_mean >= 5) and (r_mean < 20)


def fire(screen):
    red_layer = np.array(screen)[:, :, 0]
    
    red_layer[red_layer >= 250] = 255
    red_layer[red_layer < 250] = 0

    _, r_mean, _, _ = descriptive_statistics(red_layer)

    if enemy(r_mean):
        pag.mouseDown()
        time.sleep(0.2)
        pag.mouseUp()
        return True
    return False


while True:
    screen = get_screeshot('test')

    fire(screen)
    