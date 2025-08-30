import random
from exercises import EasyMen, EasyPhy, MedPhy, MedMen, HardMen, HardPhy

print ("Welcome Students")
def repeat():
    while True:
    
        difficulty = random.randint(1, 3)
       
        def physicalworkout():
            match difficulty:
                case 3:
                    easyphy_activity = random.choice(EasyPhy)
                    print ("You have to do a", easyphy_activity)
                case 1:
                    medphy_activity = random.choice(MedPhy)
                    print ("You have to do a", medphy_activity)
                case 2:
                    hardphy_activity = random.choice(HardPhy)
                    print ("You have to do a", hardphy_activity)
        
        
        def mentalworkout():
            score = 0    
            match difficulty:
                case 1:
                    activity = random.sample(EasyMen, 4)
                case 2:
                    activity = random.sample(MedMen, 4)
                case 3:
                    activity = random.sample(HardMen, 4)
            for q, a in activity:
                user_input = input(q).lower()

                if user_input == a:
                      score += 1
                #else:
                    #print ("Wrong answer the correct answer is ", a)

            print ("Great job, Your total score is ", score)  

        type1 = input ("What type of activity would you like? (Physical or Mental) ").upper()
    
        if type1 == 'PHYSICAL':
                physicalworkout()
    
        elif type1 == 'MENTAL':
                mentalworkout()

        choice = input ("Have you completed the Exercise? (yes/no) ")

        if choice == 'yes':
            print ("Congratulations on finishing the workout")
            another = input("Do you want to do another one? (yes/no) ")
            if another == 'no':
                 print ("Goodbye!")
                 break
        elif choice == 'no':
            print ("Try Again")

repeat()
         
