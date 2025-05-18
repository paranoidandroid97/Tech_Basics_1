import time

def pause():
    time.sleep(2)

# --- Game State ---

inventory = []
MAX_INVENTORY_SIZE = 5

# Story introduction
print("You're a traveller wandering through the uncharted lands of Mentisia.")
pause()
print("A land of hills overgrown with grass as far as the eye can see.")
pause()
print("You’ve stumbled upon an ancient field camp long forgotten.")
pause()
print("You’ll need to find useful items to survive and make it out of the wilderness.")

# Items in the area

items_in_room = [
    {"name": "Map", "type": "tool", "description": "A weathered map of Mentisia’s hills. Could help you escape."},
    {"name": "Canteen", "type": "food", "description": "Contains enough water to keep you going for a day."},
    {"name": "Herbs", "type": "healing", "description": "Wild herbs. You remember they can stop bleeding."},
    {"name": "Lantern", "type": "tool", "description": "It glows faintly. Could be useful in the cave nearby."},
    {"name": "Bread", "type": "food", "description": "Stale but edible. Better than starving."},
    {"name": "Journal", "type": "tool", "description": "Filled with field notes. Might contain useful information."},
]

# --- Functions ---

def show_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("You are carrying:")
        for item in inventory:
            print(f"- {item['name']}")

def show_room_items():
    if not items_in_room:
        print("There’s nothing in this area.")
    else:
        print("You see the following items:")
        for item in items_in_room:
            print(f"- {item['name']}")

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("You can’t carry any more. Drop something first.")
        return
    for item in items_in_room:
        if item['name'].lower() == item_name:
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You picked up the {item['name']}.")
            return
    print("That item is not here.")

def drop(item_name):
    for item in inventory:
        if item['name'].lower() == item_name:
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You dropped the {item['name']}.")
            return
    print("You don’t have that item.")

def use(item_name):
    for item in inventory:
        if item['name'].lower() == item_name:
            if item['type'] == "food":
                print(f"You consume the {item['name']}. You feel a bit stronger.")
                inventory.remove(item)
            elif item['type'] == "healing":
                print(f"You use the {item['name']}. Wounds stop bleeding.")
                inventory.remove(item)
            elif item['type'] == "tool":
                print(f"You try to use the {item['name']}, but you’re not sure where yet.")
            else:
                print("You’re not sure how to use that.")
            return
    print("You don’t have that item.")

def inspect(item_name):
    # Check inventory
    for item in inventory:
        if item['name'].lower() == item_name:
            print(f"{item['name']}: {item.get('description', 'No description available.')}")
            return
    # Check room
    for item in items_in_room:
        if item['name'].lower() == item_name:
            print(f"{item['name']}: {item.get('description', 'No description available.')}")
            return
    print("You don’t see that item here.")

# --- Game Loop ---

def game_loop():
    print("\nType 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], inspect [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("inspect "):
            item_name = command[8:]
            inspect(item_name)
        elif command == "quit":
            print("You turn away from the hills of Mentisia and vanish into the unknown.")
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
