#!/usr/bin/python3

from Console import Console
from Launcher import Launcher
from Option import Option
from os import system
from sys import exit, argv
from Gigachad import GIGACHAD
import keyboard

if __name__ == '__main__':
    system('cls||clear')
    print(GIGACHAD)
    print("Press ENTER to continue")
    keyboard.wait('enter', True)

    argv = argv
    if (len(argv) < 2):
        exit(1)
    console = Console(argv[1], [
            Launcher(True, 'launcher_1.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Launcher(False, 'launcher_2.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Launcher(True, 'launcher_3.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Launcher(True, 'launcher_4.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Launcher(False, 'launcher_5.launch', '/c/Users/Pepe/Desktop/TODO.txt')
        ],
        [
            Option('a', '/c/Users/Pepe/Desktop/TODO.txt', '~', '-a', {}),
            Option('b', '/c/Users/Pepe/Desktop/TODO.txt', '~', '-u', {}),
            Option('c', '/c/Users/Pepe/Desktop/TODO.txt', '~', '-ls', {}),
            Option('d', '/c/Users/Pepe/Desktop/TODO.txt', '~', '-r', {}),
            Option('e', '/c/Users/Pepe/Desktop/TODO.txt', '~', '-q', {})
        ])
    console.start()


# import readline

# def input_with_prefill(prompt, text):
#     def hook():
#         readline.insert_text(text)
#         readline.redisplay()
#     readline.set_pre_input_hook(hook)
#     result = input(prompt)
#     readline.set_pre_input_hook()
#     return result