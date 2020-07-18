class Item():
    def __init__(self,name, description,currentRoom):
        self.name=name
        self.description = description
        self.currentRoom = currentRoom
    def __str__(self):
        return f'\n{self.name.upper()}\n{self.description}'
    def __repr__(self):
        return f'debugger Item.name=={self.name.upper()}\nItem.description=={self.description}\nItem.currentRoom=={self.currentRoom} '
    def toggleCarry(self):
        if self.currentRoom==rooms['PlayersPocket']:
            self.currentRoom==playerOne.currentRoom
            print(f'You dropped {self.name}..It lives in {self.currentRoom}for now.')

        elif self.currentRoom==rooms['PlayersPocket']
            print(f'You picked up {self.name}..It lives in your pocket for now.')
            
        