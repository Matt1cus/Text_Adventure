import time

#this will give the slow ahh text like a typewriter
def typewriter_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.02)
    print()

#TITLE!!!!!!!!!!!
TITLE = r"""

___________.__             ________  .__       .___   ___ ___                             
\__    ___/|  |__   ____   \_____  \ |  |    __| _/  /   |   \  ____  __ __  ______ ____  
  |    |   |  |  \_/ __ \   /   |   \|  |   / __ |  /    ~    \/  _ \|  |  \/  ___// __ \ 
  |    |   |   Y  \  ___/  /    |    \  |__/ /_/ |  \    Y    (  <_> )  |  /\___ \\  ___/ 
  |____|   |___|  /\___  > \_______  /____/\____ |   \___|_  / \____/|____//____  >\___  >
                \/     \/          \/           \/         \/                   \/     \/ 

                              ___         /\         ___
                              | |        /  \        | |
                              | |       / /\ \       | |
                              | |      / |  | \      | |
                           ___| |_____/  |__|  \_____| |___
                          /          /          \          \
                         /__________________________________\
                          |    ____      ____      ____    |
                          |   /    \    /    \    /    \   |
                          |   | || |    | || |    | || |   |
                          |   |-++-|    |-++-|    |-++-|   |
                          |   |_||_|    |_||_|    |_||_|   |
                       ___|________________________________|___
                       |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
                        | |  ___   ___   ____   ___   ___  | |
                        | | |   | |   | |    | |   | |   | | |
                        | | |---| |---| |    | |---| |---| | |
                        | | |   | |   | |   o| |   | |   | | |
                        | | |___| |___| |    | |___| |___| | |
                        | |             |____|             | |
                       ========================================
                                       [______]
           

"""


#house
rooms = {
    "Hall" : {
        "description" : "A dusty hall, cobwebs are hanging from the ceiling. ",
        "north": "Library",
        "west": "Kitchen",
        "east": "Bedroom",
        "south": "Front Door"
    },
    "Kitchen" : {
        "description" : "A rotting scent fills the air, mold and mildew linger on every surface.",
        "west": "Hall",
        "item" : "Candle"
    },
    "Library" : {
        "description": "Shelves of musty books line the walls.",
        "south" : "Hall",
        "item" : "Key",
    },
    "Bedroom" : {
        "description" : "A single, creaky bed sits underneath a cracked window.",
        "east" : "Hall",
    },
    "Front Door" : {
        "description" : "A heavy, solid wooden door. Freedom is just on the other side.",
        "north" : "Hall"
    },
}

shortcuts = {
    "n" : "north",
    "s" : "south",
    "e" : "east",
    "w" : "west",
    "i" : "inventory",
    "l" : "look",
}
current_room = "Hall"
inventory = []
moves = 0
show_room = True


print(TITLE)
print("You wake up on a cold floor. You have no memory of arriving or how you got here.")
print("The house is silent, the door is locked.")
typewriter_print("Find a way out")
print("Type 'quit' to exit")
print("Type 'help' for more info")

while True:
    if show_room:
        print()
        print("== " + current_room + " ==")
        typewriter_print(rooms[current_room]["description"])
        if "item" in rooms[current_room]:
        print("You see a ", rooms[current_room]["item"] + ".")
        show_room = False

    command = input("> ").lower().strip()
    print("You typed " + command)

    if command == "quit":
        print("Goodbye!")
        break

    elif command == "help":
        print("Move:  north, south, east, west (n, s, e, w)")
        print("Do:    take, look (l), inventory (i)")
        print("Other: help, quit")

    elif command == "look":
        show_room = True

    elif command in ["north", "south", "east", "west"]: #navigation through rooms
        if command in rooms[current_room]:
            next_room = rooms[current_room][command]

            if next_room == "Library" and "candle" not in inventory:
                print("It is too dark to see, you need some form of light. ")

            elif next_room == "Library" and "candle" not in inventory:
                print("The front door is locked, perhaps there is a key?")

                if current_room == "Front Door":
                    print()
                    print("You turn the key, and the heavy wooden door slowly creaks open. ")
                    print("A cold rush of air brushes you face, the fear is over. You escaped the house!")
                    print("CONGRATULATIONS!")
            else:
                current_room = next_room
                moves = moves + 1
                show_room = True


    elif command == "take":
        if "item" in rooms[current_room]:
            item = rooms[current_room]["item"]
            inventory.append(item)
            del rooms[current_room]["item"] #this will make sure there is only 1 of the item

        else:

            print("Nothing to take.")
    elif command == "inventory":
        if len(inventory) < 0: #if u got nothing or pickup nothing
            print("You aren't carrying anything.")
        else:
            print("You are carrying", inventory)

    else:
        print("Command cannot be understood.")




