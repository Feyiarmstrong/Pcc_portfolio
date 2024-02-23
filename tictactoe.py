def print_board(board):
    for row in board:
        print (" | ".join(row))
        print ("-" *5)

def check_winner(board, player):
    for row in board:
        if all (cell ==player for cell in row):
            return True
        
    for col in range(3):
        if all (board[row][col]== player for row in range (3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range (3)):
        return True
    
    return False



def tic_tac_toe():
    board = [[" " for _ in range (3)] for i in range (3)]
    players = ['x', 'o']
    current_player = 0

    print ("welcome to tic tac toe! ")

    for _ in range (9):
        print_board(board) 
        print (f"player {players[current_player]}'s turn")

        while True:
            row = int (input("Enter row (0, 1, or 2):"))
            col = int(input("Enter colum (0, 1, or 2):"))


            if 0 <= row <= 2 and 0 <=col <= 2 and board [row][col] ==" ":
                board [row[col]] =players[current_player]
                break
            else:
                print ("invalid move. Try again")

        if check_winner(board, players[current_player]):
            print_board (board)
            print ("it's a tie")

if __name__ == "__main__":
    tic_tac_toe()