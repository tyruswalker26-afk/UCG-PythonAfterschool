#
#
#
#
#
#
# ASCII Title Screen
print("""
 ________   _____    _____________   _________   _____________   ___________   __________   __________  ___________    
|         | |    |  |            | |         | |     _       | |           | |          | |          | |          | 
|_       _| |    |  |            | |_       _| |    |_|      | |           | |_        _| |    _     | |       ___|
  |     |   |    |  |            |   |     |   |             | |           |  |      |    |   | |    | |      |___ 
  |     |   |    |  |           _|   |     |   |             | |          _|  |      |    |   |_|    | |       ___|
  |     |   |    |  |          |_    |     |   |     _       | |         |_   |      |    |          | |      |___
  |_____|   |____|  |____________|   |_____|   |____| |______| |___________|  |______|    |__________| |__________|
      
                            TIC   TAC     TOE
                       PLAYER (X) vs COMPUTER (0)
""") 


# Main Menu loop
while True:
    print("=" * 40)
    print("           MAIN MENU")
    print("=" * 40)
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")
    print("=" * 40)

    choice = input("choose an option (1-3): ")
    
    if choice == "1":
        break  # Start game
    elif choice == "2":
        print("\n" + "=" * 40)
        print("           INSTRUCTIONS")
        print("=" * 40)
        print(".  You are x,  Computer is 0")
        print(".  Enter a number 1-9 to place your mark")
        print(".  The board is numbered like this:")
        print("""
              1 | 2 | 3
              ---------
              4 | 5 | 6
              ---------
              7 | 8 | 9
          """)
        print(". First to get 3 in a row wins")
        print(". The computer will NEVER lose!")
        input("\npress Enter to return to menu...")
    elif choice == "3":
        print("\nThanks for playing!\n")
        exit()
    else:
        print("Invlid choice! Please enter 1, 2, or 3.")
        input("Press Enter to continue...")

# Game Board (using 9 var iab les)
b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b8 = b9 = " "

# Track used positions              
used = ""

# Game Loop
while True:
    game_over = False

    # Reset board
    b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = " "

    
    # Player always starts 
    current_Player = "x"

    # Main game loop (max 9 moves)
    for move in range(9):
        # Display board using for loops
        print("\n" + " " * 10 + "CURRENT BOARD")
        print(" " * 10 + "=" * 17)
        print(f"          {b1 if b1 != ' ' else '1'} | {b2 if b2 != ' ' else '2'} | {b3 if b3 != ' ' else '3'}")
        print("         -----------")
        print(f"          {b4 if b4 != ' ' else '4'} | {b5 if b5 != ' ' else '5'} | {b6 if b6 != ' ' else '6'}")
        print("         -----------")
        print(f"          {b7 if b7 != ' ' else '7'} | {b8 if b8 != ' ' else '8'} | {b9 if b6 != ' ' else '6'}")
        print(" " * 10 + "=" * 17 + "\n")
        

        #Check for win after move 5+
        if move >= 5:
            #Check rows
            if b1 == b2 == b3 and b1 != " ":
                winner = b1
                game_over = True
            elif b4 == b5 == b6 and b4 != " ":
                winner = b4
                game_over = True
            elif b7 == b8 == b9 and b7 != " ":
                winner = b7
                game_over = True
            #Check columns 
            elif b1 == b4 == b7 and b1 != " ":
                winner = b2
                game_over = True
            elif b2 == b5 == b8 and b2 != " ":
                winner = b2
                game_over = True
            elif b3 == b6 == b9 and b3 != " ":
                winner = b3
                game_over = True
            #Check Diagonals
            elif b1 == b5 == b9 and b1 != " ":
                winner = b1
                game_over = True
            elif b3 == b5 == b7 and b3 != " ":
                winner = b3
                game_over = True

            if game_over:
                #Final board 
                print(" " * 10 + "FINAL BOARD")
                print(" " * 10 + "=" * 17)
                print(f"         {b1} | {b2} | {b3} ")
                print(f"         {b4} | {b5} | {b6} ")
                print(f"         {b7} | {b8} | {b9} ")
                print(" " * 10 + "=" * 17 + "\n")

                if winner == "X":
                    print(""" 
    🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉
         YOU WIN!
          🏆🏆🏆
    """)
                else:
                    print(""" 
    😔😔😔 GAME OVER 😔😔😔
        COMPUTER WINS!
        😭😭💻😭😭
""")
                    break
        #Draw Check

        if move == 8 and not game_over: 
            print(" "* 10 + "IT'S A DRAW")
            print(""" 
            🤝🤝🤝
            DRAW!
            🤝🤝🤝
            """)
            game_over = True

            if game_over == True:
                break
            
            # Player's turn (X)
            if current_Player == "X":
                while True:
                    try:
                        pos = int (input("Your turn (X). Enter 1-9: "))
                        if pos < 1 or pos > 9:
                            print("Please enter a numder ")
                            continue
                    except:
                        print("Invalid input! Enter number 1-9")
                        continue
                    
                    # Check if spot taken
                    taken = False
                    for i in range(len(used)):
                        if int(used[i])== pos:
                            taken = True
                            break
                        if taken:
                            print("That spot is already taken!")
                            continue
                        
                        # Place X
                        if pos == 1: b1 = "X"
                        elif pos == 2 : b2 = "X"
                        elif pos == 3 : b3 = "X"
                        elif pos == 4 : b4 = "X"
                        elif pos == 5 : b5 = "X"
                        elif pos == 6 : b6 = "X"
                        elif pos == 7 : b7 = "X"
                        elif pos == 8 : b8 = "X"
                        elif pos == 9 : b9 = "X"

                        used += str(pos)
                        current_Player = "0"
                        break

                    else:
                        print("Computer's turn (0)")        
    placed = False

    for test in range (1,10):
                        if placed: break
                        temp_b1, temp_b2, temp_b3, = b1, b2, b3 
                        temp_b4, temp_b5, temp_b6, = b4, b5, b6
                        temp_b7, temp_b8, temp_b9, = b7, b8, b9
                        if test == 1 and b1 == " ": temp_b1 = "0"
                        elif test == 2 and b2 == " ": temp_b2 = "0"
                        elif test == 3 and b3 == " ": temp_b3 = "0"
                        elif test == 4 and b4 == " ": temp_b4 = "0"
                        elif test == 5 and b5 == " ": temp_b5 = "0"
                        elif test == 6 and b6 == " ": temp_b6 = "0"
                        elif test == 7 and b7 == " ": temp_b7 = "0"
                        elif test == 8 and b8 == " ": temp_b8 = "0"
                        elif test == 9 and b9 == " ": temp_b9 = "0"
                        else: continue

                        if(temp_b1 == temp_b2 == temp_b3 == "0" or
                           temp_b4 == temp_b5 == temp_b6 == "0" or
                           temp_b7 == temp_b8 == temp_b9 == "0" or
                           temp_b1 == temp_b4 == temp_b7 == "0" or
                           temp_b1 == temp_b2 == temp_b3 == "0" or
                           temp_b1 == temp_b2 == temp_b3 == "0" or
                           temp_b1 == temp_b2 == temp_b3 == "0" or
                           temp_b1 == temp_b2 == temp_b3 == "0"):
                            if test == 1: b1 = "0"
                            elif test == 2: b2 = "0"
                            elif test == 3: b3 = "0"
                            elif test == 4: b4 = "0"
                            elif test == 5: b5 = "0"
                            elif test == 6: b6 = "0"
                            used += str(test)
                            placed = True
                if not placed:
                    for test in  range(1, 10):
                         if placed: break
                         temp_b1,  temp_b2, temp_b3, temp_b4, temp_b5, 




















                        















































































































                        