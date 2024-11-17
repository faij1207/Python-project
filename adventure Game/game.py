import random

# Player class to manage inventory, health, and game state
class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.game_over = False

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if self.inventory:
            print(f"Your inventory: {', '.join(self.inventory)}")
        else:
            print("Your inventory is empty.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"\nYou take {damage} damage. Current health: {self.health}")
        if self.health <= 0:
            print("You've run out of health. Game Over!")
            self.game_over = True

player = Player()

# Save game function
def save_game():
    with open('game_save.txt', 'w') as f:
        f.write(f"{player.health},{','.join(player.inventory)}\n")
    print("Game saved successfully!")

# Load game function
def load_game():
    try:
        with open('game_save.txt', 'r') as f:
            data = f.read().strip().split(',')
            player.health = int(data[0])
            player.inventory = data[1:]
            print("Game loaded successfully!")
    except FileNotFoundError:
        print("No saved game found.")

# Advanced Game Functions
def start_game():
    print("\nWelcome to 'The Lost Treasure Adventure'!")
    print("You have 100 health points. Along the way, you'll find items and face dangers.")
    print("You can check your inventory anytime by typing 'inventory'.")
    choice = input("Do you want to start a 'new' game or 'load' a previous game? ")

    if choice.lower() == 'new':
        print("\nYou begin your journey in the jungle...")
        jungle_path()
    elif choice.lower() == 'load':
        load_game()
        jungle_path()
    else:
        print("Invalid choice. Starting a new game by default.")
        jungle_path()

def jungle_path():
    while not player.game_over:
        print("\nYou are in a dense jungle. Ahead, you see two paths: one leading to a waterfall, another to a dark cave.")
        choice = input("Do you choose the 'waterfall' path or the 'cave' path? ")

        if choice.lower() == 'waterfall':
            waterfall_encounter()
        elif choice.lower() == 'cave':
            cave_entrance()
        elif choice.lower() == 'inventory':
            player.show_inventory()
        else:
            print("Invalid choice. Try again.")

def waterfall_encounter():
    print("\nYou approach the waterfall. Suddenly, you slip and fall into the river!")
    print("You lose health trying to swim to safety.")
    player.take_damage(20)

    if not player.game_over:
        print("After swimming to safety, you find a shiny object on the ground.")
        choice = input("Do you want to 'take' the object or 'leave' it? ")

        if choice.lower() == 'take':
            print("You found a map! This might help you navigate the jungle.")
            player.add_item("map")
        elif choice.lower() == 'leave':
            print("You decided not to take the object.")
        else:
            print("Invalid input. You leave without taking the object.")

        jungle_path()

def cave_entrance():
    print("\nYou enter the dark cave. It's eerily quiet.")
    if "torch" not in player.inventory:
        print("It's too dark to see anything. Maybe if you had a torch...")
        jungle_path()
    else:
        print("With the torch in hand, you light your way deeper into the cave.")
        cave_exploration()

def cave_exploration():
    print("\nAs you move deeper into the cave, you find a treasure chest!")
    choice = input("Do you want to 'open' the chest or 'leave' it? ")

    if choice.lower() == 'open':
        print("Inside the chest, you find gold and a healing potion!")
        player.add_item("healing potion")
        player.add_item("gold")
        print("Your health is restored by 50 points.")
        player.health += 50
    else:
        print("You leave the chest behind and exit the cave.")

    jungle_path()

def random_encounter():
    if random.choice([True, False]):
        print("\nA wild animal appears!")
        choice = input("Do you want to 'fight' or 'run'? ")

        if choice.lower() == 'fight':
            outcome = random.choice([True, False])
            if outcome:
                print("You defeated the animal and survived.")
            else:
                print("You got injured in the fight.")
                player.take_damage(30)
        elif choice.lower() == 'run':
            print("You managed to escape safely.")
        else:
            print("Invalid input. You hesitated and the animal attacked!")
            player.take_damage(30)
    else:
        print("\nThe path ahead is clear. You move forward without trouble.")

def save_or_continue():
    choice = input("\nDo you want to 'save' the game or 'continue'? ")
    if choice.lower() == 'save':
        save_game()
    elif choice.lower() == 'continue':
        jungle_path()
    else:
        print("Invalid input. Continuing without saving.")
        jungle_path()

# Start the advanced game
start_game()
