#!/usr/bin/python3

from Console import Console
from Service import Service
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
            Service(True, 'launcher_1.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Service(False, 'launcher_2.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Service(True, 'launcher_3.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Service(True, 'launcher_4.launch', '/c/Users/Pepe/Desktop/TODO.txt'),
            Service(False, 'launcher_5.launch', '/c/Users/Pepe/Desktop/TODO.txt')
        ],
        [
            Option('a', '~', '-a', { "path": "/usr/bin", "enc": "/dev/null"}),
            Option('b', '~', '-u', {"path": "/usr/bin", "enc": "/dev/null", "idlk": "test"}),
            Option('c', '~', '-ls', {}),
            Option('d', '~', '-r', {}),
            Option('e', '~', '-q', {})
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