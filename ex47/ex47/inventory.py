class Item_list(object):

    def __init__(self):
        self.items = []
        pass

    def addItem(self, itemName):
        self.items.append(itemName)

    def removeItem(self, itemName):
        self.items.remove(itemName)

    def hasItem(self, itemName):
        if itemName in self.items:
            return True
        else:
            return False
