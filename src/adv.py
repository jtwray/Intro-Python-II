import sys
from room import Room
from player import Player
# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
'playersPocket':Room("Players Pocket","""Where all the Important Items from your Journey Are Stored""")
}
print(rooms)
class Room:
    def __init__(self, name, description,position, n_to='',s_to='',e_to='',w_to=''):
        self.name=name
        self.description = description
        self.position=position
        self.n_to=self.position[0]
        self.s_to=self.position[1]
        self.e_to=self.position[2]
        self.w_to=self.position[3]
    def __repr__(self):
        return f'{self.name}\n {self.description}\n {self.postion}\n items:{self.items}'

    def __str__(self):
        return f'{self.name} \n {self.description}'

    def searchForItems(self):
        if len(items)>0:
            print(f'You found {items[-1]}')
            foundItem=True
        while foundItem==True:
            selection = int(input(f'Pick up {items[-1]}? \n 1:Yes  \n 2:No'))
            if selection == 1:
                    item.currentlocation=rooms["playerspocket"]
            elif selction==2:
                    item.currentLocation=item.currentLocation
        print(f'Nothing to be found here 🙈')



        


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['narrow'].n_to = rooms['treasure']
rooms['playersPocket'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerOne=Player(outside)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



#gameplayloop