print("type 'help' for a list of commands")
command = ""
while command != "quit":
    command = input(">")
    if command == "start".lower():
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - quit the game")
    elif command == "quit":
        break
    else:
        print("I don't understand that command")
print("type 'help' for a list of commands")