def sum(a,b):
 ans = a+b
 print(a,"+",b ,"=",ans)
def sub(a,b):
 ans = a-b
 print(a,"-",b ,"=", ans)
def mul(a,b):
 ans = a*b
 print(a,"*",b ,"=", ans)
def divi(a,b):
 ans = a/b
 print(a,"/",b ,"=", ans)
while True:
 print("1 Additon")
 print("2 Subtraction")
 print("3 Multiplication")
 print("4 Division")
 print("5 Exit")
 
 choice = int(input("Enter the choice :"))
 
 
 if choice == 1:
 a = int(input("Enter 1st Number :"))
 b = int(input("Enter 2st Number :"))
 sum(a,b)
 
 elif choice == 2:
 a = int(input("Enter 1st Number :"))
 b = int(input("Enter 2st Number :"))
 sub(a,b)
 elif choice == 3:
 a = int(input("Enter 1st Number :"))
 b = int(input("Enter 2st Number :"))
 mul(a,b)
 
 elif choice == 4:
 a = int(input("Enter 1st Number :"))
 b = int(input("Enter 2st Number :"))
 
 if b == 0:
 print("Zeroooooooo can't be divided motherfucker !!!!")
 continue
 divi(a,b)
 elif choice == 5:
 print("Bye Bye")
 break
 else:
 print("Invalid choice")