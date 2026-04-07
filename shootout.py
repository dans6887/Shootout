import time
import os
import random
def shootout_game():
    os.system('cls||clear') #clears the screen before the game starts

    print("SHOOTOUT")
    print()

    time.sleep(2)

    print("You are in a shootout with a robot.")
    #print("You have 10 seconds to draw your weapon and shoot.")
    #print("If you shoot first, you win. If the robot shoots first, you lose.")

    #the wait phase
    print("Get ready...")
    time.sleep(random.uniform(2, 5)) #waits a random amount of time between 2 and 5 seconds

    #the draw phase
    print("\n----DRAW!!!!----")
    start_time = time.time()
    input("Press [ENTER] to shoot: ")
    # Note: input() waits for the user to press Enter and release it.
    end_time = time.time()
    reaction_time = end_time - start_time
    
    #win/loss logic
    print(f"\nYour reaction time was {reaction_time:.2f} seconds.")
    if reaction_time <=2.0: #if the player reacts in 2 seconds or less, they win
        print("You shot the robot in time! You win!")
    else:
        print("The robot shot you! You lose!")
    
    

if __name__ == "__main__":
    shootout_game()
