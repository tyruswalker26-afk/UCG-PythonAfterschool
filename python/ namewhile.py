#Enter Name Program 
#Program Description: This program requires the user to types their name

#varibale to store user name
Name = input ("Enter your name: ") 

#while loop will run as the variable name has nothing stored in it
while Name == "" or not Name.isalpha():
    print("Name entered is invalid")
    #Asking the user name in case they didn't type
    Name =input("Enter your name: ")

#Exit out of loop once finished
print(f"Hello {Name}")