class GlobalState:
    def __init__(self):
        self.opened = False

    def setOpen(self, value:bool)->None:
        self.opened = value

    def getOpen(self)->bool:
        return  self.opened