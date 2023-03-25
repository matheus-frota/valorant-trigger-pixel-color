import keyboard
import os

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
    print('======MENU======')
    print('Press key: Ctrl')
    print('Exit key : Shift')
    print('Author   : Matheus Frota')
    print('================')


if __name__ == '__main__':
    banner()
    while True:
        screen = get_screeshot('extended-minor')
        if keyboard.is_pressed('ctrl'):
            check_fire(screen)
            banner()
            continue

        if keyboard.is_pressed('shift'):
            banner()
            break
