from contextlib import contextmanager
import os
import time

import keyboard
from matplotlib import pyplot as plt
import numpy as np
import pyautogui as pag
import pygetwindow as gw
import win32api

from config import HEIGHT, WIDTH

global atirando
atirando = False

def get_screeshot(type = 'all'):
    window = gw.getWindowsWithTitle('VALORANT')[0]

    left, top = window.topleft
    
    if type == 'all':
        return pag.screenshot(region=(left, top, WIDTH, HEIGHT))
    elif type == 'minor':
        return pag.screenshot(region=(left+WIDTH/2-5, top+HEIGHT/2+15, 30, 30))
    elif type == 'extended-minor':
        return pag.screenshot(region=(left+WIDTH/2-5, top+HEIGHT/2+15, 30, 70))


def show_vision_trigger(arr):
    plt.imshow(arr, cmap='gray')
    plt.show()


def descriptive_statistics(arr, show: bool = False):
    r_sum, r_mean, r_median, r_std = np.sum(arr), np.mean(arr), np.median(arr), np.std(arr)
    if show:
        print(f"Media: {r_mean} - Soma: {r_sum} - Mediana: {r_median} - Std: {r_std}")
    return r_sum, r_mean, r_median, r_std


def enemy(r_mean):
    return (r_mean >= 5) and (r_mean < 20)


def check_fire(screen, show=False):
    red_layer = np.array(screen)[:, :, 0]
    
    red_layer[red_layer >= 250] = 255
    red_layer[red_layer < 250] = 0

    _, r_mean, _, _ = descriptive_statistics(red_layer)

    if show:
        show_vision_trigger(red_layer)

    if enemy(r_mean):
        pag.mouseDown()
        time.sleep(0.2)
        pag.mouseUp()


def banner():
    return """
    .-----.    _                          .---.       .-. 
    `-. .-'   :_;                         : .; :     .' `.
    : :.--. .-. .--.  .--.  .--. .--.   :   .' .--.`. .'
    : :: ..': :' .; :' .; :' '_.': ..'  : .; :' .; :: : 
    :_;:_;  :_;`._. ;`._. ;`.__.':_;    :___.'`.__.':_; 
                .-. : .-. :                             
                `._.' `._.'                             
    """


def menu():
    print(banner())
    print('1 - Pressione "Ctrl" para atirar e parar de atirar.')
    print('2 - Pressione "Ctrl+Alt" para fechar o programa.')
    print("Pressione as teclas correspondentes para selecionar a opção")
    while True:
        screen = get_screeshot('extended-minor')
        if keyboard.read_key() == 'ctrl':
            print('Começar a atirar!')
            check_fire(screen)

        if keyboard.is_pressed('ctrl+alt'):
            print("Fechando o programa...")
            break


if __name__ == '__main__':
    menu()