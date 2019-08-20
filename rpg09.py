#!/usr/bin/python3

def showInstructions():
    print('''
            RPG Game
            --------
            Commands:
                go [direction]
                get [item]
    ''')

def showStatus():
    print('----------------------')
    print(f"You are in the {currentRoom}")
    print("Inventory: " + str(inventory))
    if "item" in rooms[currentRoom]:
        print(f"You see a {rooms[currentRoom]['item']}")
    print("----------------------")

inventory = []

rooms = {
            'Hall' : {
                'south' : 'kitchen',
                'east' : 'Dining Room',
                'item' : 'skeletonkey'
                },
                'kitchen' : {
                    'north' : 'Hall',
                    'item' : 'monster'
                },
                'Dining Room' : {
                    'west' : 'kitchen',
                    'south' : 'Garden',
                    'item' : 'cookies'
                },
                'Garden' : {
                    'north' : 'Dining room'
                }
        }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input("> ")

    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You cannot go that way!")

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(f"You just picked uo {move[1]}!")
            del rooms[currentRoom]['item']

        else:
            print("You cannot pick that up!")


    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("A monster has you! Game Over")
        break




    if currentRoom == 'Garden' and 'skeletonkey' in inventory:
        print("You open the old rusty gate in the garden with the skeleton key and escaped! You Win!")
        break
