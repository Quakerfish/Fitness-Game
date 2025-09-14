import random
import os
import time
from exercises import EasyMen, EasyPhy, MedMen, MedPhy, HardMen, HardPhy, MemoryWord

difficulty = random.randint(1, 3)

def slowprint(text):
    for char in text:
        print(char, end="", flush = True)
        time.sleep(0.03)
    print()

def clear():
    if os.name == 'nt':
        os.system('cls')
       
def physicalworkout():
            match difficulty:
                case 3:
                    phy_activity = random.choice(EasyPhy)
                case 1:
                    phy_activity = random.choice(MedPhy)
                case 2:
                    phy_activity = random.choice(HardPhy)

            slowprint(f"\nYou have to do {phy_activity}")
            return phy_activity

        
def mentalworkout():   
            match difficulty:
                case 1:
                    activity = random.sample(EasyMen, 5)
                case 2:
                    activity = random.sample(MedMen, 5)
                case 3:
                    activity = random.sample(HardMen, 5)

            score = 0
            lives = 3
            for q, a in activity:
                
                user_input = input(q).strip().lower()

                if user_input == a:
                    score += 1
                    print (f"Remaining Lives: {lives}")

                else:
                    print ("Wrong answer the correct answer is", a)
                    lives -= 1
                    print (f"Remaining Lives: {lives}")
                
                if lives == 0:
                    print ("Game Over")
                    break

            slowprint (f"Great job, Your total score is {score}/{len(activity)}")  
            return activity

def memorygame():
        activity = random.choice(MemoryWord)
        print (f"Pattern Test!\nRemember these patterns:{activity}\n")

        for number in range (10, 0, -1):
            print(f"Clearing in {number} Seconds!!")
            time.sleep(1)

        print("Clearing")
        clear()

        print ("---PATTERN MEMORY---\n")
        answer = input("What was the Pattern?\nAnswer:").strip().upper()

        if answer.replace(" ", "") == activity.replace (" ", ""):
            print("\nCORRECT!")
            
        else:
            print("\nINCORRECT!!")
            
        return activity
        


        