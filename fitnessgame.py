import random

print ("Welcome Students")
def repeat():
    while True:
    
        difficulty = random.randint(1, 3)
        #List for Physical Activities
        EasyPhy = ['5 Pushups', '5 Situps', '30 Second Plank']
        MedPhy = ['10 Pushups', '10 Situps', '1 Minute Plank']
        HardPhy = ['10 Pushups 3 Sets', '10 Sit Ups 3 Sets', '1 Minute Plank 2 Sets']
        #List for Mental Activities
        EasyMen = [
                ("What is 1 + 1? ", "2"),
                ("What is the opposite of white? ", "black"),
                ("How many sides is a Triangle? ", "3"),
                ("What is the closest planet to the sun? ", "mercury"),
                ("What is the largest planet in the Solar System? ", "jupiter"),
                ("What is the name of the planet that we live in? ", "earth")
        ]
        MedMen = [
                ("What is 15 × 6? ", "90"),
                ("Who wrote Romeo and Juliet? ", "william shakespeare"),
                ("What is the largest ocean on Earth? ", "pacific ocean"),
                ("What color do you get when you mix blue and yellow? ", "green")
        ]
        HardMen = [
                ("What is the square root of 81? ", "9"),
                ("Who proposed the theory of relativity? ", "albert einstein"),
                ("If you have ₱1,000 and spend 35% of it, how much is left? ", "650"),
                ("Solve: (25 ÷ 5) × (12 – 7) ", "25"),
        ]
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
                user_input = input(q + "").lower()

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
         
