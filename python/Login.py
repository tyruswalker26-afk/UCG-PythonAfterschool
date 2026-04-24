password = "python123"
attempt = ""
tries = 0
while attempt != password and tries < 3:
    attempt = input("Enter the password")    
    tries += 1 # Add 1 to the number of tries
    if attempt != password:
        print("Incorrect password:") 
if attempt == password:
    print("✅ Accsess granted")
else:
    print("🚫 Too many attempts. Try again") 
