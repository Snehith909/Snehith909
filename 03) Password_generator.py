import random
user_option = [1,2]
while True:
    print("\t1 Password_Generator")
    print("\t2 Exit")
    a = "ABCDEFGHIJKLMNOPRSTUVWXYZ1234567890abcdefghijkmnloprstuvwxyz!@#$%^&*()_+"
    user_input = int(input("Enter your option: "))
    if user_input == 1:

        length = int(input("Enter the length of the password "))
        if length >= 20:
            print("Please Enter length of the password below 20")
            continue
    elif user_input == 2:
        print("Good Bye!!")
        break     
    
    elif user_option != user_input:
        print("Please enter either 1 or 2")
        continue
 
    b = "".join(random.sample(a,length))
    print(f"Your genarated password is: {b}")
