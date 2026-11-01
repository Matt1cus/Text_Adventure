rooms = {
    "Hall" : {
        "description" : "A dusty hall, cobwebs are hanging from the ceiling. ",
        "north": "Library",
        "east": "Kitchen",
        "west": "Bedroom",
        "south": "Front Door"
    },
    "Kitchen" : {
        "description" : "A rotting scent fills the air, mold and mildew linger on every surface.",
        "west": "Hall",
    },
    "Library" : {
        "description": "Shelves of musty books line the walls.",
        "south" : "Hall",
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



print("Welcome to the TEXT ADVENTURE GAME!")
print("Welcome to the Old House Adventure!")
print("Type 'quit' to exit")
print("Type 'quit' to exit")

while True:
    print()
    print("You are in the ", current_room)
    print(rooms[current_room]["description"])
    command = input("> ").lower().strip()


    if command == "quit":
        print("Goodbye!")
        break
    elif command == "help":
        print("Commands: north, south, east, west, help, quit")

    elif command in ["north", "south", "east", "west"]:
        if command in rooms[current_room]:
            current_room = rooms[current_room][command]
        else:
            print("You cannot go this way.")

    else:
        print("Command cannot be understood.")

    print("You typed " + command)


