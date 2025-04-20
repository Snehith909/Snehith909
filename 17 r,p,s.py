import random
user_point = 0
computer_point = 0

print("     Rock")
print("     Paper")
print("     Scissors")
print("     Exit")
print("     If you entered wrong input Than you are Gayyyy!")

while True:
    option = ["rock","paper","scissors"]
    user_input = input("Enter Rock paper Scissors or Exit: ")
    computer_input = random.choice(option)
    if user_input == "rock":
        if computer_input == "rock":
            print("You got tie")
        elif computer_input == "paper":
            print("You Won!")
            user_point+=1
        elif computer_input == "scissors":
            print("Computer Won!")
            computer_point+=1
        

    elif user_input == "paper":
        if computer_input == "paper":
            print("You got tie")
        elif computer_input == "rock":
            print("You Won!")
            user_point+=1
        elif computer_input == "scissors":
            print("Computer Won!")
            computer_point+=1
         
    
    elif user_input == "scissors":
        if computer_input == "scissors":
            print("You got tie")
        elif computer_input == "paper":
            print("You Won!")
            user_point+=1
        elif computer_input == "rock":
            print("Computer Won!")
            computer_point+=1
         
             
    elif user_input == "exit":
        print("Goooood bye !")
        break
         
        
    elif user_input == "1":
      
     print("Your Score  ",user_point)
     print("Computer_Score",computer_point)
    
    else:
        print("Invalid user input")
         
     

        
 
