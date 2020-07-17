# Write a class to hold player information, e.g. what room they are in
# currently.
from room import rooms 
class Player:
    def __init__(self, name, description,notepad, items=[],currentroom=rooms['outside']):
        self.name = name
        self.description=description
        self.notepad=notepad
        self.items=items
        self.currentRoom=currentRoom


print(Player)