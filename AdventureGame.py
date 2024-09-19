import random

def intro():
    print("Welcome to the Adventure Game!")
    print("You are in a dark forest. There are two paths in front of you.")
    print("You can go 'left' towards the river or 'right' towards the mountains.")

def river_path():
    print("You chose to go towards the river.")
    print("You arrive at the riverbank. It's calm and peaceful.")
    print("Do you want to 'swim' across the river or 'follow' the river downstream?")

def mountain_path():
    print("You chose to go towards the mountains.")
    print("You start climbing the rocky path. It's steep and challenging.")
    print("Do you want to 'climb' further up the mountain or 'rest' in a cave?")

def swim_decision():
    if random.choice([True, False]):
        print("You swim across the river safely and find a hidden treasure on the other side!")
    else:
        print("As you swim, a strong current pulls you under. You struggle but manage to reach the shore safely.")
    
def follow_decision():
    if random.choice([True, False]):
        print("You follow the river downstream and find a small village where you can rest.")
    else:
        print("You follow the river for hours but find nothing. You are now tired and hungry.")

def climb_decision():
    if random.choice([True, False]):
        print("You climb further and discover a beautiful view from the top of the mountain!")
    else:
        print("As you climb, the rocks become slippery. You lose your footing but manage to grab a ledge and pull yourself to safety.")

def rest_decision():
    if random.choice([True, False]):
        print("You rest in the cave and wake up feeling refreshed. A mysterious stranger offers you food and guidance.")
    else:
        print("While resting, you hear strange noises from deeper within the cave. You decide to leave before anything finds you.")

def adventure_game():
    intro()
    
    choice1 = input("Do you choose to go 'left' or 'right'? ").lower()
    
    if choice1 == "left":
        river_path()
        choice2 = input("Do you want to 'swim' or 'follow' the river? ").lower()
        if choice2 == "swim":
            swim_decision()
        elif choice2 == "follow":
            follow_decision()
        else:
            print("That's not a valid option. The adventure ends here.")
    
    elif choice1 == "right":
        mountain_path()
        choice2 = input("Do you want to 'climb' or 'rest' in the cave? ").lower()
        if choice2 == "climb":
            climb_decision()
        elif choice2 == "rest":
            rest_decision()
        else:
            print("That's not a valid option. The adventure ends here.")
    
    else:
        print("That's not a valid option. The adventure ends here.")

    print("Thank you for playing the Adventure Game!")

# Start the game
adventure_game()
