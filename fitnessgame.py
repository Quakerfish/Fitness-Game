import random
import datetime
from workout import physicalworkout, mentalworkout, memorygame, adventuregame,  slowprint, wordle, riddlegame, reactiontime

slowprint ("💪🧠 ---FIT IT!--- 🎯\n")

def repeat():
    while True:
        timedate = datetime.datetime.now()
        time = timedate.strftime("%H:%M %p")
        date = timedate.strftime("%B %d, %Y")

        name = input ("👤 Name: ")
        course = input ("📚 Course: ")
        print ("\n---📌 SELECTION---\n")
        while True:
            while True:
                slowprint("🤔 What type of activity would you like:\n1️⃣  Physical 🏃\n2️⃣  Mental 🧩\n3️⃣  Random 🎲")
                type1 = input("🎯 Chosen Activity: ").strip().upper()
                
                if type1 == 'PHYSICAL' or type1 == '1':
                    chosen = 'Physical'
                    break
                elif type1 == 'MENTAL' or type1 == '2':
                    chosen = 'Mental'
                    break
                elif type1 == 'RANDOM' or type1 == '3':
                    randomizer = random.randint(1,2)
                    match (randomizer):
                        case 1:
                            chosen = 'Physical'
                            break
                        case 2:   
                            chosen = 'Mental'
                            break
                else:
                    print("\n⚠️ ---INVALID INPUT!---\nPlease choose the correct option ✅")

            slowprint ("\n🔥 ---EXERCISE TIME!!--- 💯")

            if chosen == 'Physical':
                currentactivity = physicalworkout()

            elif chosen == 'Mental':
                randomizer = random.randint(1, 5)
                match (randomizer):
                    case 3:
                        currentactivity = wordle()
                    case 2:
                        currentactivity = mentalworkout()
                    case 1:
                        currentactivity = memorygame()
                    case 4:
                        currentactivity = riddlegame()
                    case 5:
                        currentactivity = reactiontime()
            
            else:
                print("⚠️ Invalid choice! Please choose the correct options.")
                slowprint("🤔 What type of activity would you like:\n1️⃣ Physical 🏃\n2️⃣ Mental 🧩\n3️⃣ Random 🎲")
                        
            while True:
                slowprint ("\n✅ Have you completed the Exercise?")
                choice = input ("(Yes/No): ").strip().lower()
                lives = 3
                score = 0

                if choice == 'yes':
                        slowprint("\n🏆 ---RESULT!!--- 🎉\n")
                        slowprint (f"👤 Name: {name}\n📚 Course: {course}")
                        slowprint (f"🎯 Chosen Activity: {chosen}")
                        slowprint (f"📅 Date Finished: {date}")
                        slowprint (f"⏰ Time Finished: {time}\n")
                        break
                elif choice == 'no':
                        print (f"\n🔄 ---TRY AGAIN!!--- 💪\n")
                        if chosen == 'Physical':
                            print (f"🏃 Your Activity: {currentactivity}")
                        elif chosen == 'Mental':
                            if randomizer == 2:
                                for q, a in currentactivity:
                                    
                                    user_input = input(q).lower()

                                    if user_input == a:
                                        score += 1
                                        print (f"💖 Correct! Lives Remaining: {lives}")
                                    else:
                                        print ("❌ Wrong answer! The correct answer is", a)
                                        lives -= 1
                                        print (f"❤️ Lives Remaining: {lives}")
                                    
                                    if lives == 0:
                                        print ("💀 Game Over ☠️")

                                print (f"🎉Your total score is {score}/{len(currentactivity)}")  
                            elif randomizer == 1:
                                memorygame()
                            elif randomizer == 3:
                                wordle()
                            elif randomizer == 4:
                                riddlegame()
                            elif randomizer == 5:
                                reactiontime()
                else:
                    print("\n⚠️ ---INVALID INPUT!---\nPlease choose the correct input ✅")
            while True:
                tryagain = input ("\nDo you want to play again?\n(yes/no) ")
            
                if tryagain == 'yes':
                    print ("")
                    break
                elif tryagain == 'no':
                    slowprint ("Goodbye :<")
                    return
                else:
                    slowprint ("\n⚠️ ---INVALID INPUT!---\nPlease choose the correct input ✅")
            
            

repeat()
