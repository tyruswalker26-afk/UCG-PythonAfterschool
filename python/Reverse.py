# Program Description:
# This program takes a number as input from the user and reverses its digits.
# It does this by repeatedly extracting the last digit of the number and building
# the reversed number digit-by-digit.

# Take input from the user and convert it to an integer
n = int(input("Enter a number: "))

# Variable to store the reversed number
rev = 0

# Loop until all digits are processed
while n != 0:
    r = n % 10          # Get the last digit of the number
    rev = rev * 10 + r  # Add the digit to the reversed number
    n = n // 10         # Remove the last digit from the original number

# Print the final reversed number
print("Reversed number:", rev)
