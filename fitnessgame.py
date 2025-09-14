import random
import datetime
from workout import physicalworkout, mentalworkout, memorygame, slowprint



slowprint ("---FIT IT!---\n")

def repeat():
    while True:
        timedate = datetime.datetime.now()
        time = timedate.strftime("%H:%M %p")
        date = timedate.strftime("%B %d, %Y")

        name = input ("Name: ")
        course = input ("Course: ")
        print ("\n---SELECTION---\n")
        while True:
            slowprint("What type of activity would you like:\n1. Physical\n2. Mental\n3. Random")
            type1 = input("Chosen Activity: ").strip().upper()
            
            if type1 == 'PHYSICAL' or type1 == '1':
                chosen = 'PHYSICAL'
                break
            elif type1 == 'MENTAL' or type1 == '2':
                chosen = 'MENTAL'
                break
            elif type1 == 'RANDOM' or type1 == '3':
                randomizer = random.randint(1,2)
                match (randomizer):
                    case 1:
                        chosen = 'PHYSICAL'
                        break
                    case 2:   
                        chosen = 'MENTAL'
                        break
            else:
                print("\n---INVALID INPUT!---\nPlease chose the correct options")

        slowprint ("\n---EXERCISE!!---")

        if chosen == 'PHYSICAL':
            currentactivity = physicalworkout()

        elif chosen == 'MENTAL':
            randomizer = random.randint(1,2)
            match (randomizer):
                case 1:
                    currentactivity = memorygame()
                case 2:
                    currentactivity = mentalworkout()
        
        else:
             print("Invalid choice! Please chose the correct options")
             slowprint("What type of activity would you like:\n1. Physical\n2. Mental\n3. Random")
                     
        while True:
            slowprint ("\nHave you completed the Exercise?")
            choice = input ("(Yes/No):").strip().lower()
            lives = 3
            score = 0

            if choice == 'yes':
                    slowprint("\n---RESULT!!---\n")
                    slowprint (f"Name: {name}\nCourse: {course}")
                    slowprint (f"Chosen Activity: {type1}")
                    slowprint (f"Date Finished: {date}")
                    slowprint (f"Time Finished: {time}\n")
                    return
            elif choice == 'no':
                    print (f"\n---TRY AGAIN!!---\n")
                    if type1 == 'PHYSICAL':
                        print (f"Your Activity: {currentactivity}")
                    elif type1 == 'MENTAL':
                        if randomizer == 2:
                            for q, a in currentactivity:
                                
                                user_input = input(q).lower()

                                if user_input == a:
                                    score += 1
                                    print (f"Lives Remaining: {lives}")
                                else:
                                    print ("Wrong answer the correct answer is", a)
                                    lives -= 1
                                    print (f"Lives Remaining: {lives}")
                                
                                if lives == 0:
                                    print ("Game Over")

                            print (f"Great job, Your total score is {score}/{len(currentactivity)}")  
                        elif randomizer == 1:
                            memorygame()
                
            else:
                print("\n---INVALID INPUT!---\nPlease Chose the correct Input")
            

repeat()
         
