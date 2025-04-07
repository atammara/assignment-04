import random

def print_board(board):
    """Print the current game board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    """Check if there's a winner or if the game is a draw"""
    # All possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # Return the winning player
    
    if " " not in board:
        return "Draw"
    
    return None

def player_move(board, player):
    """Handle player's move"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9!")

def computer_move(board):
    """Simple AI for computer's move"""
    # First check for winning move
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = "O"
            if check_winner(board_copy) == "O":
                return i
    
    # Then block player's winning move
    for i in range(9):
        if board[i] == " ":
            board_copy = board.copy()
            board_copy[i] = "X"
            if check_winner(board_copy) == "X":
                return i
    
    # Try to take center
    if board[4] == " ":
        return 4
    
    # Take any available corner
    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for corner in corners:
        if board[corner] == " ":
            return corner
    
    # Take any available edge
    edges = [1, 3, 5, 7]
    random.shuffle(edges)
    for edge in edges:
        if board[edge] == " ":
            return edge

def play_game():
    """Main game loop"""
    while True:
        print("\nWelcome to Tic-Tac-Toe!")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "3":
            print("Thanks for playing!")
            return
        
        if choice not in ["1", "2"]:
            print("Invalid choice! Please try again.")
            continue
        
        # Initialize game
        board = [" "] * 9
        current_player = "X"
        game_mode = "PvP" if choice == "1" else "PvC"
        
        while True:
            print_board(board)
            
            if current_player == "X" or game_mode == "PvP":
                move = player_move(board, current_player)
            else:
                print("Computer's turn...")
                move = computer_move(board)
            
            board[move] = current_player
            result = check_winner(board)
            
            if result:
                print_board(board)
                if result == "Draw":
                    print("It's a draw!")
                else:
                    winner = "Player " + result if game_mode == "PvP" or result == "X" else "Computer"
                    print(f"{winner} wins!")
                break
            
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()