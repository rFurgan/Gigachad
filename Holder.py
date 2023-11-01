class Holder:
    def __init__(self, items):
        self.index = 0
        self.items = items
        self.max = len(self.items)

    def item(self, index=-1):
        return self.items[self.index if index == -1 else index]
