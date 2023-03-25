import keyboard
import os

from trigger_pixel_color.config import (
    HEIGHT,
    WIDTH,
    BUTTON_PRESS_TIME,
    HOLD_BUTTON,
    TOGGLE_BUTTON,
    EXIT_BUTTON,
    IS_RUNING)
from trigger_pixel_color.trigger_bot import check_fire, get_screeshot


def title():
    return """
    .-----.    _                          .---.       .-. 
    `-. .-'   :_;                         : .; :     .' `.
    : :.--. .-. .--.  .--.  .--. .--.   :   .' .--.`. .'
    : :: ..': :' .; :' .; :' '_.': ..'  : .; :' .; :: : 
    :_;:_;  :_;`._. ;`._. ;`.__.':_;    :___.'`.__.':_; 
                .-. : .-. :                             
                `._.' `._.'                             
    """


def banner():
    os.system('cls')
    print(title())
    print('====== INFORMATIONS ======')
    print(F'Hold key          : {HOLD_BUTTON.upper()}')
    print(F'Toggle key        : {TOGGLE_BUTTON.upper()}')
    print(f'Exit key          : {EXIT_BUTTON.upper()}')
    print(f'Button press time : {BUTTON_PRESS_TIME}')
    print(f'Resolution window : {WIDTH}x{HEIGHT}')
    print('==========================')


if __name__ == '__main__':
    banner()
    while True:
        screen = get_screeshot('extended-minor')
        if keyboard.is_pressed(HOLD_BUTTON):
            check_fire(screen)
            banner()
            continue

        if keyboard.is_pressed(EXIT_BUTTON):
            banner()
            break

        else:
            if keyboard.is_pressed(TOGGLE_BUTTON):
                IS_RUNING = not IS_RUNING
                banner()

            if IS_RUNING:
                check_fire(screen)
                banner()
                continue