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

current_room = "Hall"
inventory = []



print("Welcome to the TEXT ADVENTURE GAME!")
print("Welcome to the Old House Adventure!")
print("Type 'quit' to exit")
print("Type 'help' for more info")

while True:
    print()
    print("You are in the ", current_room)
    print(rooms[current_room]["description"])

    if "item" in rooms[current_room]:
        print("You see a ", rooms[current_room]["item"])

    command = input("> ").lower().strip()
    print("You typed " + command)
    if command == "quit":
        print("Goodbye!")
        break
    elif command == "help":
        print("Commands: north, south, east, west, take, inventory, help, quit")

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




