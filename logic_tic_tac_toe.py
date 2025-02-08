import random
board =[" " for _ in range(9)]

player_symbol='x'
computer_symbol='o'


#function to draw board
def draw_board():
    
    print(board[0] , '|' , board[1] , '|' , board[2])
    print("--------------")
    print(board[3] , '|' , board[4] , '|' , board[5])
    print("--------------")
    print(board[6] , '|' , board[7] , '|' , board[8])


#check for winner

def check_winner(symbol):
    #horizontal
    for i in range(0,9,3):
        if(board[i] == board[i+1] == board[i+2] == symbol):
            return True
    #vetical
    for i in range(3):
        if(board[i] == board[i+3] == board[i+6] == symbol):
            return True 
    #diognal
    if(board[0]==board[4]==board[8]== symbol or board[2]==board[4]==board[6]== symbol):
        return True
    return False
def player_turn():
    try:
       position = int(input("Enter the position from 1-9: "))
       if position < 1 or position > 9 or board[position - 1] != ' ':
             print("Invalid move! Try again.")
             player_turn()
             return
    except ValueError:
           print("Invalid input! Enter a number between 1 and 9.")
           player_turn()
           return

    if board[position -1]==' ':
        board[position -1]=player_symbol
        draw_board()
        if check_winner(player_symbol):
            print("congratulations you won")
        else:
            computer_turn()

#function to access the computer turn 

def computer_turn():
    available_moves=[i for i in range(9) if board[i]== ' ']
    if len(available_moves) > 0:
        position = random.choice(available_moves)
        board[position] = computer_symbol
        draw_board()
        if check_winner(computer_symbol):
             
             print("Sorry, you lost.")
             return 
        player_turn()  

    else:
        print("its a tie")
print("tic tac toe")
draw_board()
player_turn()


