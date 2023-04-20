# create a room class that will have a name, description, items, exits and characters.items and characters will be an array and exits will be a dictionary
from room_game_map import Map


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}
        self.characters = []
        self.is_light = True
        self.is_open = True

        # create a function that will add an item to the room

    # create a method that will check if the room has a character
    def has_character(self, search_character):
        for character in self.characters:
            if character.name.lower() == search_character.lower():
                return True
        return False

    def toggle_light(self):
        self.is_light = not self.is_light

    # create a method to turn on the light in the room
    def turn_on_light(self):
        self.is_light = True

    # create a method to check if the light is on
    def is_light_on(self):
        return self.is_light

    # create a method that will open the door
    def open_door(self):
        self.is_open = True

    # create a method that will close the door

    def close_door(self):
        self.is_open = False

    # create a method that will check if the door is open
    def is_door_open(self):
        return self.is_open

    def add_item(self, item):
        self.items.append(item)

    # create a function that will add an exit to the room where the key is the direction and the value is the room
    def add_exit(self, direction, room):
        self.exits[direction] = room

    # create a function that will add a character to the room
    def add_character(self, character):
        self.characters.append(character)

    # create a function that will remove an item from the room
    def remove_item(self, item):
        index = self.items.index(item)
        the_item = self.items[index]
        self.items.remove(item)
        return the_item

    # create a function that will remove a character from the room
    def remove_character(self, character):
        self.characters.remove(character)

    # create a function that will search for an item by item name and return the item
    def search_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

# create an item that will have a name and a description
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# create a character that will have a name and a description
class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# create an inventory class that will hold all the items the player has
class Inventory:
    def __init__(self):
        self.items = []

    # create a function that will add an item to the inventory
    def add_item(self, item):
        self.items.append(item)

    # create a function that will remove an item from the inventory
    def remove_item(self, item):
        self.items.remove(item)

    # create a function that will search for an item by item name and return the item
    def search_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None


# create an action array that will hold all the actions the player can do
actions = {"move": {"left", "right", "up", "down"}, "item": {"take", "drop", "use"}, "help": {}, "quit": {}}


# create a world function that will create the rooms and add the items, exits and characters to the rooms
def world():
    room1 = Room("Room 1", "This is room 1.")
    room2 = Room("Room 2", "This is room 2.")
    room2.is_light = False
    room3 = Room("Room 3", "This is room 3.")
    room3.close_door()
    room4 = Room("Room 4", "This is room 4.")
    room5 = Room("Room 5", "This is room 5.")

    item_key = Item("Key", "A key unlocks a door.")
    item_torch = Item("Torch", "A torch to light your way.")
    item_sword = Item("Sword", "A sword to fight with.")

    character_guard = Character("Guard", "A guard blocking your path.")

    room1.add_exit("right", room2)
    room2.add_exit("left", room1)
    room2.add_exit("up", room3)
    room3.add_exit("down", room2)
    room3.add_exit("right", room4)
    room4.add_exit("left", room3)
    room4.add_exit("up", room5)
    room5.add_exit("down", room4)

    room1.add_item(item_torch)
    room4.add_character(character_guard)
    room2.add_item(item_key)
    room3.add_item(item_sword)

    # i need a list that will hold all the rooms
    rooms = [room1, room2, room3, room4, room5]
    game_map = Map(rooms)

    return room1, game_map


# create a game loop that starts with creating the world and then creates a player and a current room variable
def game_loop():
    inventory = Inventory()
    current_room, game_map = world()
    print("Welcome to the game!")
    game_map.draw_map(current_room)

    # create a while loop that will run until the player has won or lost
    while True:
        # print the current room's name and description
        print(f"You are in the {current_room.name}.")
        print(current_room.description)

        describe_room(current_room)
        describe_items_in_a_room(current_room)
        describe_characters_in_a_room(current_room)
        display_all_actions()
        showing_inventory(inventory)

        # get user input
        user_input = input("What would you like to do? ").lower()

        # process user input
        if user_input == "move":
            current_room = handle_move(current_room, inventory, user_input)
        elif user_input == "item":
            handle_item(current_room, inventory, user_input)
        elif user_input == "help":
            print("You can move, take, drop, use, and quit.")
        elif user_input == "quit":
            print("Thanks for playing!")
            break


def display_all_actions():
    print("Actions:")
    for action in actions.keys():
        print(f"{action}")


def handle_move(current_room, inventory, user_input):
    display_actions(user_input)
    user_input = input("Which direction you want to move? ").lower()
    if user_input in current_room.exits:
        previous_room = current_room
        current_room = current_room.exits[user_input]
        # check if the light is on
        if not current_room.is_light_on():
            print("It is too dark to see you need to turn on the torch.")
            current_room = previous_room
        elif not current_room.is_door_open():
            current_room = handle_closed_door(current_room, inventory, previous_room, user_input)
        elif current_room.name == "Room 3":
            current_room = make_sure_you_have_a_sword(current_room, inventory, previous_room, user_input)
        elif current_room.name == "Room 5":
            if previous_room.has_character("Guard"):
                print("You can't move to room 5 until you kill the guard.")
                current_room = previous_room
            else:
                print(f"You moved {user_input}.")
                finish_game()

        else:
            print(f"You moved {user_input}.")
    else:
        print("Invalid input. Try again.")

    return current_room


def finish_game():
    print("You won the game!")
    quit()


def make_sure_you_have_a_sword(current_room, inventory, previous_room, user_input):
    if inventory.search_item("sword") is None:
        print("You can't move to room 4 without a sword to protect yourself.")
        current_room = previous_room
    else:
        print(f"You moved {user_input}.")
    return current_room


def handle_closed_door(current_room, inventory, previous_room, user_input):
    if inventory.search_item("key") is not None:
        print("You used the key to open the door.")
        current_room.open_door()
        print(f"You moved {user_input}.")
    else:
        print("The door is locked you need a key to open the door.")
        current_room = previous_room
    return current_room


def handle_item(current_room, inventory, user_input):
    display_actions(user_input)
    user_input = input("What would you like to do with the item? ").lower()
    if user_input == "take":
        if len(current_room.items) == 0:
            print("There are no items in this room.")
        else:
            describe_items_in_a_room(current_room)
            user_input = input("What item would you like to take? ").lower()
            item_to_take = current_room.search_item(user_input)
            current_room.remove_item(item_to_take)
            inventory.add_item(item_to_take)
            showing_inventory(inventory)
    elif user_input == "drop":
        if len(inventory.items) == 0:
            print("There are no items in your inventory.")
        else:
            showing_inventory(inventory)
            user_input = input("What item would you like to drop? ").lower()
            item_to_drop = inventory.search_item(user_input)
            inventory.remove_item(item_to_drop)
            current_room.add_item(item_to_drop)
            showing_inventory(inventory)
    elif user_input == "use":
        showing_inventory(inventory)
        user_input = input("What item would you like to use? ").lower()
        item_to_use = inventory.search_item(user_input)
        if item_to_use.name == "Key":
            print("You unlocked the door.")

        elif item_to_use.name == "Torch":
            print("You lit the torch.")
            #    toggle the light in th next room
            for room in current_room.exits.values():
                room.turn_on_light()

        elif item_to_use.name == "Sword":
            for character in current_room.characters:
                if character.name == "Guard":
                    print("You killed the guard.")
                    current_room.remove_character(character)
                    print("You can now move to room 5.")
                else:
                    print("There are no enemies in this room.")

        else:
            print("Invalid input. Try again.")


def showing_inventory(inventory):
    # display the items in the inventory
    print("Inventory:")
    for item in inventory.items:
        print(f"{item.name} - {item.description}")


def display_actions(action):
    for action in actions[action]:
        print(f"{action}")


def describe_characters_in_a_room(current_room):
    # list all characters in the room
    print("Characters:")
    for character in current_room.characters:
        print(f"{character.name} - {character.description}")


def describe_items_in_a_room(current_room):
    # list all items in the room
    print("Items:")
    for item in current_room.items:
        print(f"{item.name} - {item.description}")


def describe_room(current_room):
    # list all available exits by room and direction
    print("Exits:")
    for direction, room in current_room.exits.items():
        print(f"{direction} - {room.name}")


# run the game loop
if __name__ == "__main__":
    game_loop()
