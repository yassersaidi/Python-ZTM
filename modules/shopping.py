print(__name__)

class Shopping():
    def __init__(self,*item_name,**kawrgs):
        self.item_name = item_name
    def showBuys(self):
        print(f"you buy this item: {self.item_name}")
    def delete(self,name):
        while True:
            if name == self.item_name:
                self.item_name = None
                break
        return self




