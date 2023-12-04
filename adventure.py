import json
import sys

# Helper function to load the game map
def load_map(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)

# Basic command functions
def go(direction, current_room, rooms):
    exits = rooms[current_room]['exits']
    if direction in exits:
        return exits[direction]
    else:
        print(f"There's no way to go {direction}.")
        return current_room

def look(current_room, rooms):
    room = rooms[current_room]
    print(f"\n> {room['name']}\n\n{room['desc']}\n")
    if 'items' in room:
        print("Items:", ", ".join(room['items']))
    print("Exits:", " ".join(room['exits'].keys()))

def get(item, current_room, rooms, inventory):
    room = rooms[current_room]
    if 'items' in room and item in room['items']:
        inventory.append(item)
        room['items'].remove(item)
        print(f"You pick up the {item}.")
    else:
        print(f"There's no {item} here.")

def inventory_display(inventory):
    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("You're not carrying anything.")

def drop(item, current_room, rooms, inventory):
    if item in inventory:
        inventory.remove(item)
        rooms[current_room].setdefault('items', []).append(item)
        print(f"You dropped the {item}.")
    else:
        print(f"You don't have a {item} to drop.")

def help_command(commands):
    print("You can run the following commands:")
    for cmd, (desc, _) in commands.items():
        print(f"  {cmd}{' ...' if cmd in ['go', 'get', 'drop'] else ''} - {desc}")

# Command parsing logic
def parse_command(input_text, commands, direction_commands):
    parts = input_text.strip().lower().split()
    if not parts:
        return None, None

    cmd, *args = parts
    if cmd in direction_commands:
        return 'go', [direction_commands[cmd]]
    elif cmd in commands:
        return cmd, args
    else:
        print("Unknown command. Type 'help' for a list of commands.")
        return None, None

# Main game loop
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        return

    rooms = load_map(sys.argv[1])
    current_room = 0
    player_inventory = []

    commands = {
        "go": ("Move in a specified direction", go),
        "get": ("Pick up an item", get),
        "drop": ("Drop an item from your inventory", drop),
        "look": ("Get a description of your surroundings", look),
        "inventory": ("Check your inventory", inventory_display),
        "quit": ("Exit the game", lambda: exit()),
        "help": ("Show this help message", lambda: help_command(commands))
    }

    direction_commands = {
        "n": "north", "north": "north",
        "e": "east", "east": "east",
        "s": "south", "south": "south",
        "w": "west", "west": "west",
        "ne": "northeast", "northeast": "northeast",
        "nw": "northwest", "northwest": "northwest",
        "se": "southeast", "southeast": "southeast",
        "sw": "southwest", "southwest": "southwest",
        "u": "up", "up": "up",
        "d": "down", "down": "down"
    }

    while True:
        look(current_room, rooms)
        cmd, args = parse_command(input("What would you like to do? "), commands, direction_commands)
        if cmd:
            if cmd == "quit":
                print("Goodbye!")
                break
            elif cmd == "help":
                commands[cmd][1]()
            else:
                func = commands[cmd][1]
                if func:
                    if cmd in ["go", "get", "look", "drop"]:
                        current_room = func(*args, current_room, rooms, player_inventory)
                    else:
                        func(*args)


   
