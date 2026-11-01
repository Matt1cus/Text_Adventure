import time

#this will give the slow ahh text like a typewriter
def typewriter_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.02)
    print()

def title_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.001)
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
        "west": "Bedroom",
        "east": "Kitchen",
        "south": "Front Door"
    },
    "Kitchen" : {
        "description" : "A rotting scent fills the air, mold and mildew linger on every surface.",
        "west": "Hall",
        "down" : "basement",
        "item" : "candle",
    },
    "Library" : {
        "description": "Shelves of musty books line the walls.",
        "south" : "Hall",
        "item" : "key",
    },
    "Bedroom" : {
        "description" : "A single, creaky bed sits underneath a cracked window.",
        "east" : "Hall",
        "up" : "Attic",
    },
    "Front Door" : {
        "description" : "A heavy, solid wooden door. Freedom is just on the other side.",
        "north" : "Hall"
    },
    "Attic" : {
        "description" : "Dust swirls in a thin stream of moonlight. Old trunks and a broken chair fill the cramped space.",
        "down" : "Bedroom",
    },
    "Basement" : {
        "description" : "Cold stone walls drip with water from moisture. Something skitters away in the darkness",
        "up" : "Kitchen",
    }
}

shortcuts = {
    "n" : "north",
    "s" : "south",
    "e" : "east",
    "w" : "west",
    "u" : "up",
    "d" : "down",
    "i" : "inventory",
    "l" : "look",
}
current_room = "Hall"
inventory = []
moves = 0
show_room = True


title_print(TITLE)
typewriter_print("You wake up on a cold floor. You have no memory of arriving or how you got here.")
typewriter_print("The house is silent, the door is locked.")
typewriter_print("Find a way out")
typewriter_print("Type 'quit' to exit")
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

    if command in shortcuts:
        command = shortcuts[command]

    if command == "quit":
        print("Goodbye!")
        break

    elif command == "help":
        print("Move:  north, south, east, west, up, down (n, s, e, w, u, d)")
        print("Do:    take, look (l), inventory (i)")
        print("Other: help, quit")

    elif command == "look":
        show_room = True

    elif command in ["north", "south", "east", "west", "up", "down"]: #navigation through rooms
        if command in rooms[current_room]:
            next_room = rooms[current_room][command]

            if next_room == "Library" and "candle" not in inventory:
                print("It is too dark to see, you need some form of light. ")

            elif next_room == "Front Door" and "key" not in inventory:
                print("The front door is locked, perhaps there is a key?")


            else:
                current_room = next_room
                moves = moves + 1
                show_room = True
        else:
            print("You cannot go this way.")

        if current_room == "Front Door":
            print()
            print("You turn the key, and the heavy wooden door slowly creaks open. ")
            print("A cold rush of air brushes your face, the fear is over. You escaped the house!")
            print("CONGRATULATIONS!")
            print("You escaped in", moves, "moves.")
            break

    elif command == "take" or command.startswith("take "):
        if "item" in rooms[current_room]:
            item = rooms[current_room]["item"]
            if command == "take" or command == "take " + item:
                inventory.append(item)
                del rooms[current_room]["item"] #this will make sure there is only 1 of the item
                print("You picked up the " + item +".")
            else:
                print("You do not see that here.")
        else:
            print("There is nothing here to take.")

    elif command == "inventory":
        if len(inventory) == 0: #if u got nothing or pickup nothing
            print("You aren't carrying anything.")
        else:
            print("You are carrying " + ", ".join(inventory))

    else:
        print("Command cannot be understood, type 'help' for commands.")


