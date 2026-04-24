#Program Description: The purpose of this program is to reverse the number entered by the user





n = input("Enter a number: ")

rev = ""
i = len(n) - 1 

while i >= 0:
    rev = rev + n [i]
    i -= 1

    print(f"The number reversed is : {rev}")