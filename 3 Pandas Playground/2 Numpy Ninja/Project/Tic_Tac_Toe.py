import numpy as np

def print_board(b):
    symbol = {0:" ",1:"X",-1:"O"}
    for  r in range(3):
        row = ' | '.join(symbol[val] for val in b[r])
        print(" "+row)
        if r < 2:
            print("---+---+---")
    print()

def winner_chk(b):
    if 3 in np.sum(b,axis=1) or 3 in np.sum(b,axis=0):
        return 'X'
    elif -3 in np.sum(b,axis=1) or -3 in np.sum(b,axis=0):
        return 'O'
    elif np.trace(b)==3 or np.trace(np.fliplr(b))==3:
        return 'X'
    elif np.trace(b)==-3 or np.trace(np.fliplr(b))==-3:
        return 'O'
    elif not 0 in b:
        return 'Draw'
    else:
        return None

print()
print('*'*80)
print("Welcome To Tic Tac Toe Game".center(80))
print('*'*80)
print('='*80)
print("Rule Of Game")
print('='*80)
print("1. Tic Tac Toe is a two-player game.")
print("2. Player 1 uses 'X' and Player 2 uses 'O'.")
print("3. The game is played on a 3 × 3 board.")
print("4. Players take turns placing their symbol in an empty cell.")
print("5. A symbol cannot be placed in a cell that is already occupied.")
print("6. The first player to form a horizontal, vertical, or diagonal line")
print("   of three matching symbols wins the game.")
print("7. If all nine cells are filled and no player has three in a row the game is declared a draw.")
print("8. Enter valid row and column numbers as prompted and enjoy the game!")
print('-'*80)
print()

p1_c = 0
p2_c = 0
p1 = input("Enter Player X Name :- ")
p2 = input("Enter Player O name :- ")
print()
while True:
    current = 1 
    board = np.zeros((3,3),dtype=int)
    while True:
        if current == 1:
            Player = 'X'
        else:
            Player = 'O'

        try:
            row = int(input(Player + " - Enter row (0,1,2) :- "))        
            col = int(input(Player + " - Enter Column (0,1,2) :- "))
        except ValueError:
            print("Invalid input! Please enter integers (0, 1, or 2).")
            continue
        
        if row<0 or row>2 or col<0 or col>2:
            print("Row & Column must be between 0 or 2...")
            continue

        if board[row,col] != 0:
            print("Cell is Already Taken...")
            continue

        board[row,col] = current
        print_board(board)

        result = winner_chk(board)

        if result is not None:
            if result == "Draw":
                print("\n🤝 The match ended in a draw!")
            else:
                if result == 'X':
                    print(f"\n🎉 Congratulations {p1}!")
                    print("You won the match.")
                    p1_c += 1
                else:
                    print(f"\n🎉 Congratulations {p2}!")
                    print("You won the match.")   
                    p2_c += 1
            break
        
        if current == 1:
            current = -1
        else:
            current = 1
    
    choice = input("\nDo you want to play again? (Y/N): ")
    
    if choice.lower() != "y":
        print("\nFinal Score")
        print(f"{p1}: {p1_c}")
        print(f"{p2}: {p2_c}")
        break
    else:
        continue
    