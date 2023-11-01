import keyboard
from Holder import Holder
from os import system

class Console:
    def __init__(self, name, items, options):
        self.__name = name
        self.__exploring = False
        self.__services = Holder(items)
        self.__options = Holder(options)

    def __clear(self):
        system('cls||clear')

    def __puts(self):
        if (self.__services.max <= 0):
            return
        self.__clear()
        print(f"############### {self.__name} ###############")
        for i in range(len(self.__services.items)):
            service = self.__services.items[i]
            print(f"{('>' if (i == self.__services.index and not self.__exploring) else ' ')} {('[x]' if (service.selected) else '[ ]')} {service.name}")
            if (i == self.__services.index):
                options = self.__options.items[self.__services.index].options
                optionsItems = options.items()
                optionsKeys = list(options.keys())
                for option, value in optionsItems:
                    if (self.__options.item(self.__services.index).edit):
                        # TODO  Edit mode
                        #       can do it with keyboard.write and input afterwards
                        #       PROBLEM: All too slow
                        pass
                    print(f"\t{('>' if (optionsKeys.index(option) == self.__options.index and self.__exploring) else ' ')} {option}: {'' if option == 'env' else value}")
        self.__printShortcuts()

    def __printShortcuts(self):
        print(f"\n[ENTER] {'un' if self.__services.item().selected else ''}select [E] {'exit' if self.__exploring else 'enter'} [ESC] quit")

    def __onUp(self):
        if (self.__exploring):
            self.__options.index = self.__options.index - 1 if (self.__options.index > 0) else self.__options.max - 1
            if (self.__options.index == 3):
                self.__onUp()
        else:
            self.__services.index = self.__services.index - 1 if (self.__services.index > 0) else self.__services.max - 1

    def __onDown(self):
        if (self.__exploring):
            self.__options.index = self.__options.index + 1 if (self.__options.index < self.__options.max - 1) else 0
            if (self.__options.index == 3):
                self.__onDown()
        else:
            self.__services.index = self.__services.index + 1 if (self.__services.index < self.__services.max - 1) else 0

    def __onEnter(self):
        if (self.__exploring):
            self.__options.item(self.__services.index).edit = not self.__options.item(self.__services.index).edit
        else:
            self.__services.item().selected = not self.__services.item().selected

    def __onE(self):
        self.__exploring = not self.__exploring
        if (self.__exploring):
            self.__options.max = self.__options.item(self.__services.index).max
        self.__options.index = 0

    def __onKeyPress(self, key):
        match key.name:
            case 'up':
                self.__onUp()
            case 'down':
                self.__onDown()
            case 'enter':
                self.__onEnter()
            case 'e':
                self.__onE()
        self.__puts()

    def __register(self):
        keyboard.on_press_key('up', self.__onKeyPress, True)
        keyboard.on_press_key('down', self.__onKeyPress, True)
        keyboard.on_press_key('enter', self.__onKeyPress, True)
        keyboard.on_press_key('e', self.__onKeyPress, True)

    def start(self):
        self.__register()
        self.__puts()
        keyboard.wait('esc', True)
        return '' # TODO return the new generated task