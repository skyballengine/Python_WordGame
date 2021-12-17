# Eusebius Ballentine - IT-140

game_map = {
    'Maple Tree': {'North': 'Pine Tree', 'West': 'Walnut Tree', 'East': 'Chestnut Tree', 'South': 'Hazelnut Tree'},
    'Pine Tree': {'South': 'Maple Tree', 'East': 'Oak Tree', 'item': 'Pine Nuts'},
    'Oak Tree': {'West': 'Pine Tree', 'item': 'Acorns'},
    'Hickory Tree': {'South': 'Chestnut Tree', 'item': 'Hickory Nuts'},
    'Chestnut Tree': {'North': 'Hickory Tree', 'West': 'Maple Tree', 'item': 'Chestnuts'},
    'Cherry Tree': {'West': 'Hazelnut Tree', 'item': 'Fiendish Fox'},
    'Hazelnut Tree': {'North': 'Maple Tree', 'East': 'Cherry Tree', 'item': 'Hazelnuts'},
    'Walnut Tree': {'East': 'Maple Tree', 'item': 'Walnuts'}
}

divider = '-----------------------------'
current_location = 'Maple Tree'
inventory = []
total_items = 6


def game_instructions():
    # print welcome and game instructions
    print('Welcome to the Sneaky Squirrel Game')
    print('Collect all 6 types of nuts to win the game.  If you encounter Fiendish Fox before you collect all 6 items, then you lose the game!')
    print('The Move commands are: go North, go East, go South, go West')
    print("To get an item and add it to your inventory, the command is: get 'item name'")
    print(divider)



def display_currentlocation():
    # display current tree/location in game
    print('You are in the {}'.format(current_location))
    print(divider)

def show_inventory():
    # show current item inventory
    print('Inventory: {}'.format(inventory))
    print(divider)

def show_item(location):
    # show the item in the current_location
    if 'item' in game_map[location]:
        item = game_map[location]['item']
        if item == 'Fiendish Fox':
            print('You have encountered the Fiendish Fox and.....')
        else:
            print('There are {} in this tree.'.format(item))
    else:
        print('There are no nuts in this tree!')

def player_move(location, inventory_list):
    # player moves in a direction or gets an item based on user input
    # user input will display directions for actions
    # if user input is 'exit' or 'Exit', the game ends
    # if user input doesn't follow the action directions, then it will notify the user and ask for new input
    action = input("What's your next move?\n 1. Exit (Enter 'exit')\n 2. Move to a new tree (Enter 'go (specify direction)')\n 3. Get item (Enter 'get item')\n Enter Move: ").split()
    #print(action)
    print(divider)
    if 'exit' in action or 'Exit' in action:
        print('You have left the game, thank you for playing!')
        location = 'exit'
        #print(location)
        return location

    elif len(action) != 2:
        print("Command not understood, please enter 'go (and then the direction)'")

    elif (' ').join(action) == 'get item':
        if 'item' in game_map[location]:
            print("You added {} to your inventory.".format(game_map[location]['item']))
            get_item(location, inventory_list)
            del game_map[location]['item']
            return location, inventory_list
        else:
            print('Sorry, there are no nuts in this tree! :(')
            return location, inventory_list
    else:
        direction = action[1].lower().capitalize()
        #print(direction)

        if direction in game_map[location]:
            location = game_map[location][direction]
            print('You are now in the {}'.format(location))
            show_item(location)
            if 'Fiendish Fox' in game_map[location].values():
                location = 'exit'
                print('You have been consumed by The Fiendish Fox.\nGoodbye.')
                return location, inventory_list
            else:
                print(divider)
                return location, inventory_list

        else:
            print('Cannot move in that direction, please try again.')
            return location, inventory_list


def get_item(location, inventory_list):
    # puts item in inventory
    inventory_list.append(game_map[location]['item'])
    return inventory_list

# Game Loop
while True:
    if current_location == 'exit':
        break
    else:
        game_instructions()
        current_location = 'Maple Tree'
        display_currentlocation()
    while current_location != 'exit':
        current_location, inventory = player_move(current_location, inventory)
        #print(current_location)
        show_inventory()
        if len(inventory) == 6:
            print('You have won the game, congratulations!!\nFiendish Fox will now be forced to help you gather nuts for the season!! :)')
            break
        else:
            continue






