print("Welcome to the TEXT ADVENTURE GAME!")
print("Type 'quit' to exit")

while True:
    command = input("> ")

    if command == "quit":
        print("Goodbye!")
        break

    print("You typed " + command)


