import pyautogui as pag
import pygetwindow as gw
import keyboard
import time
import numpy as np
import cv2
from matplotlib import pyplot as plt
import win32api
import random

HEIGHT = 768
WIDTH = 1360
YELLOW_R, YELLOW_G, YELLOW_B = (145, 120, 90)

def get_screeshot(type = 'all'):
    window = gw.getWindowsWithTitle('VALORANT')[0]
    # window = gw.getWindowsWithTitle('vava')[0]

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

r_total = []
g_total = []
b_total = []

# print("Prepare-se para tirar a media de coloração de pixel")
while True:
    # print("Posicione o mouse...")
    # time.sleep(5)
    screen = get_screeshot('test')

    arr = np.array(screen)
    arr_gray = np.mean(arr, axis=2)
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    r[r >= 250] = 255
    r[r < 250] = 0

    r_sum = np.sum(r)
    r_mean = np.mean(r)
    r_median = np.median(r)
    r_std = np.std(r)
    print(f"Media: {r_mean} - Soma: {r_sum} - Mediana: {r_median} - Std: {r_std}")
    # if (b_sum > 140000) and (b_sum <= 205409):
    if (r_mean >= 5) and (r_mean < 20):
        # pag.click(clicks=5, interval=0.05)
        pag.drag(0, 100, 0.2, button='left')
        # pag.mouseDown()
        # time.sleep(0.4)
        # pag.mouseUp()
    # plt.imshow(r, cmap='gray')
    # plt.imshow(g, cmap='gray')
    # plt.imshow(b, cmap='gray')
    # plt.show()
    # capture = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    # cv2.imshow("image",arr)
    # cv2.waitKey(0)
    # screen.save(f'C:/Users/mathe/OneDrive/Documentos/funny/vava/screenshots/comp.png')
    # print("Próximo...")
    # time.sleep(5)