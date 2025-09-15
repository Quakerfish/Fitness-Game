import random
import os
import time
from exercises import EasyMen, EasyPhy, MedMen, MedPhy, HardMen, HardPhy, MemoryWord, EasyRiddle, MedRiddle, HardRiddle, Scrambled

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

    slowprint(f"\n🏃 You have to do {phy_activity} 💪")
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
        user_input = input(f"🧩 {q} ").strip().lower()

        if user_input == a:
            print (f"✅ Correct! 💖 Lives Remaining: {lives}\n")
            score += 1
        else:
            print (f"❌ Wrong! The correct answer is 👉 {a}")
            lives -= 1
            print (f"❤️ Lives Remaining: {lives}\n")
                
        if lives == 0:
            print ("💀 Game Over ☠️")
            break

    slowprint (f"🎉 Your total score is {score}/{len(activity)}")  
    return activity

def riddlegame():
    match (difficulty):
        case 1:
            activity = random.sample(EasyRiddle, 1)
        case 2:
            activity = random.sample(MedRiddle, 1)
        case 3:
            activity = random.sample(HardRiddle, 1)
                        
    score = 0
    lives = 3

    while True:       
        for q, a, h in activity:
            user_input = input(f"❓ Riddle: {q} ").strip().lower()

        if user_input == a:
            print ("✅ Correct!")
            score += 1
            print (f"💖 Lives Remaining: {lives}\n")
            break
        else:
            print ("❌ Wrong!")
            print (f"💡 Hint: {h}")
            lives -= 1
            print (f"❤️ Lives Remaining: {lives}\n")

        if lives == 0:
            print (f"\n💀 Game Over ☠️\nThe answer was 👉 {a}")
            break
                

def memorygame():
    activity = random.choice(MemoryWord)

    for number in range (3, 0, -1):
        print (f"🧠 ---PATTERN IT!!---\n\nRemember this pattern: {activity}\n")
        print(f"⏳ Clearing in {number} seconds!!")
        time.sleep(1)
        print("🧹 Clearing...")
        clear()

    print ("🔎 ---PATTERN MEMORY---\n")
    answer = input("What was the pattern?\n✍️ Answer: ").strip().upper()

    if answer.replace(" ", "") == activity.replace (" ", ""):
        print("\n✅ CORRECT! 🎉")
    else:
        print("\n❌ INCORRECT!! 😢")
            
    return activity
        
def wordle():
    print ("🔤 ---WORD SCRAMBLE--- 🎲\n")

    score = 0  
    lives = 3
    activity = random.choice(Scrambled)
    letters = list(activity)
    random.shuffle(letters)
    scrambled = "".join(letters)
    
    while True:    
        print(f"🤔 Guess the word: {scrambled}")
        user_input = input("✍️ Your answer: ").strip().lower()

        if user_input == activity:
            print ("✅ Correct!! 🎉")
            score += 1
            print (f"💖 Lives Remaining: {lives}\n")
            break
        else:
            print ("❌ Wrong!")
            lives -= 1
            print (f"❤️ Lives Remaining: {lives}\n")

        if lives == 0:
            print (f"💀 ---GAME OVER!!!--- ☠️\nThe answer was 👉 {activity}")
            break

def reactiontime():
    print("⚠️ Press Enter to start the Reaction Time Test...")
    print("⏳ Get ready...")
    
    time.sleep(random.randint(2, 5))
    starting = time.time()
    
    input("🚀 Press Enter as fast as you can!")
    ending = time.time()
    
    reactiontime = ending - starting

    slowprint(f"⏱️ Your reaction time is {reactiontime:.3f} seconds!")

    
