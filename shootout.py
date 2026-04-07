import time
import os
import keyboard

try:
    import keyboard
    print("Keyboard module is already installed.")
except ImportError as e:
    print("Error: The 'keyboard' module is not installed. Please install it using 'pip install keyboard' and try again.", e)

def shootout_game():
    os.system('cls||clear') #clears the screen before the game starts

    print("SHOOTOUT")
    print()

    time.sleep(2)

    print("You are in a shootout with a robot.")
    print("You have 3 seconds to draw your weapon and shoot.")
    print("If you shoot first, you win. If the robot shoots first, you lose.")

    time.sleep(5)

    os.system('cls||clear') #clears the screen

    start_time = time.time()
    input("Press [ENTER] to draw your weapon...")
    end_time = time.time()

    reaction_time = end_time - start_time
    input("Press [ENTER] to shoot...")
    if keyboard.is_pressed('enter'): #check if the user pressed enter to shoot
        if reaction_time < 3: #check if reaction time is less than 3 seconds
        
            print("You shot the robot first! You win!") #if the user shot and won, print the message and exit the game
            exit
        else:
            print("The robot shot you first! You lose!")#if the user shot but lost, print the message and restart the game
            shootout_game()
    
    else:
        print("You didn't shoot in time! The robot shot you first! You lose!")#if the user didnt shoot at all, print the message and restart the game
        shootout_game()

if __name__ == "__main__":
    shootout_game()