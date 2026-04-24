# Ask the user to enter a number (So create a variable called "number")
number = int(input("Enter a number between 1-26: " ))
# Create a list of letters (create a list, this is an example of a list mylist = ["apple", "banana", "cherry"])
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
# Start counting from 0 (Hint: i = 0)
i = 0


# Repeat while the counter is less than the number: 

while i < number:

#error handling
    if number > 26: 
        print("Don't enter a number greater than 26." )
        break
        
    # Extra Hint: (use: while i < n)
       
    # Pick a letter from the list
    letter = letters[i]
    # (use the counter as the position → letters[i])
    
    # Print the letter multiple times (one more each time)
    # (first time 1, second time 2, third time 3 → use i + 1)
    print(letter * (i+1)) 
    # Move to the next number

 # (add 1 to the counter → i += 1) 
    i +=1 

