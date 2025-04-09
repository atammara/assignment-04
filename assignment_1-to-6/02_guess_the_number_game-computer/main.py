import random
import math

def guess_the_number():
    print("\nWelcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Game setup
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = math.ceil(math.log2(100))  # Binary search max attempts (7 for 1-100)
    
    while True:
        try:
            # Get player's guess
            guess = int(input("\nYour guess (1-100): "))
            attempts += 1
            
            # Check guess
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The secret number was {secret_number}.")
                break
            
            # Hint system
            if attempts == max_attempts // 2:
                if secret_number % 2 == 0:
                    print("💡 Hint: The number is even!")
                else:
                    print("💡 Hint: The number is odd!")
            
            # Game over check
            if attempts >= max_attempts:
                print(f"\nGame over! The number was {secret_number}.")
                print(f"You used all {max_attempts} attempts.")
                break
                
        except ValueError:
            print("Please enter a valid number between 1 and 100.")

def main():
    while True:
        guess_the_number()
        
        # Play again?
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()