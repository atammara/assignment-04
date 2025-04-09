import random
import time

def determine_winner(player_choice, computer_choice):
    """Determine the winner of a round"""
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    else:
        return "computer"

def get_computer_choice():
    """Computer randomly selects an option"""
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    """Get and validate player input"""
    while True:
        choice = input("\nChoose rock, paper, or scissors (or 'quit'): ").lower()
        if choice in ["rock", "paper", "scissors", "quit"]:
            return choice
        print("Invalid choice. Please try again.")

def display_result(player_choice, computer_choice, result):
    """Show the round results with ASCII art"""
    # ASCII art representations
    choices = {
        "rock": """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """,
        "paper": """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """,
        "scissors": """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
    }
    
    print(f"\nYou chose: {player_choice}")
    print(choices[player_choice])
    print(f"Computer chose: {computer_choice}")
    print(choices[computer_choice])
    
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("🎉 You win this round!")
    else:
        print("💻 Computer wins this round!")

def play_game():
    """Main game loop"""
    player_score = 0
    computer_score = 0
    
    print("\nWelcome to Rock, Paper, Scissors!")
    print("First to 3 wins takes the match!")
    
    while player_score < 3 and computer_score < 3:
        player_choice = get_player_choice()
        
        if player_choice == "quit":
            print("\nThanks for playing!")
            return
        
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        display_result(player_choice, computer_choice, result)
        
        # Update scores
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        
        # Show current score
        print(f"\nScore: You {player_score} - Computer {computer_score}")
    
    # Match result
    print("\n" + "="*40)
    if player_score > computer_score:
        print("🏆 Congratulations! You won the match!")
    else:
        print("😢 Computer won the match. Better luck next time!")
    print("="*40)

def main():
    while True:
        play_game()
        
        # Play again?
        replay = input("\nPlay another match? (y/n): ").lower()
        if replay != 'y':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()