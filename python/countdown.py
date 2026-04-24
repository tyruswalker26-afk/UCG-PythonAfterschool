# Countdown timer program
#Program Description: This program count down from a user-given number to 1.

#importing time module to add 1 second delay
import time

# Ask the user to enter a number to start counting down from 
number = int(input("Enter a number to start the countdown: "))

# Keep looping as long as the number is greater than 0
while number > 0:
    print(number) # Print the current number 
    time.sleep(1) #Wait for 1 second before conting
    number -= 1    # Subtract 1 from number each time

    # Once the loop ends, print a message
    

print("🎉 Time's up !")