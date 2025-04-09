import random
import math

def computer_guesses():
    print("\nWelcome to the Reverse Guess the Number Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")
    
    # Initialize game variables
    low = 1
    high = 100
    attempts = 0
    max_attempts = math.ceil(math.log2(100))  # Binary search max attempts (7 for 1-100)
    
    while low <= high and attempts < max_attempts:
        attempts += 1
        guess = random.randint(low, high) if attempts == 1 else (low + high) // 2
        
        print(f"\nMy guess #{attempts}: Is it {guess}?")
        response = input("(C)orrect, Too (H)igh, or Too (L)ow? ").lower()
        
        if response == 'c':
            print(f"\n🎉 I guessed your number {guess} in {attempts} attempts!")
            return
        elif response == 'h':
            high = guess - 1
            print("Okay, I'll guess lower next time.")
        elif response == 'l':
            low = guess + 1
            print("Okay, I'll guess higher next time.")
        else:
            print("Please enter 'C', 'H', or 'L'.")
            attempts -= 1  # Don't count invalid responses
    
    if low > high:
        print("\nWait a minute... you must have changed your number!")
    else:
        print(f"\nI couldn't guess your number in {max_attempts} attempts. Did you follow the rules?")

def main():
    while True:
        computer_guesses()
        
        # Play again?
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()