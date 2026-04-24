#Program Description: This program checks the user age and confirms their driving eligiblity


#Variable to store age of user and recieve input
age = int(input("Enter your age: "))

#if else statements to evaluate if user can drive

if(age >= 16):
    print("Your age is eligible to drive. ")
else:
    print("Your age is ineligible to drive. ")
