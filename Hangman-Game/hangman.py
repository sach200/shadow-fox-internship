import random
import os

class HangmanGame:
    def __init__(self):
        self.words = [
            'python', 'programming', 'computer', 'algorithm', 'function',
            'variable', 'database', 'software', 'hardware', 'internet',
            'keyboard', 'monitor', 'processor', 'memory', 'network'
        ]
        self.hints = {
            'python': 'A popular programming language',
            'programming': 'Writing code to create software',
            'computer': 'Electronic device for processing data',
            'algorithm': 'Step-by-step problem solving method',
            'function': 'Reusable block of code',
            'variable': 'Storage location with a name',
            'database': 'Organized collection of data',
            'software': 'Computer programs and applications',
            'hardware': 'Physical components of a computer',
            'internet': 'Global network of computers',
            'keyboard': 'Input device with keys',
            'monitor': 'Display screen for computer',
            'processor': 'Brain of the computer',
            'memory': 'Storage for data and programs',
            'network': 'Connected group of computers'
        }
        self.hangman_stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            =========
            """
        ]
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_game_state(self, word, guessed_letters, wrong_guesses):
        self.clear_screen()
        print("=" * 50)
        print("           HANGMAN GAME")
        print("=" * 50)
        
        print(self.hangman_stages[len(wrong_guesses)])
        
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word}")
        print(f"Wrong guesses: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"Remaining attempts: {6 - len(wrong_guesses)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    
    def get_hint(self, word):
        return self.hints.get(word, "No hint available")
    
    def play_game(self):
        word = random.choice(self.words).lower()
        guessed_letters = set()
        wrong_guesses = []
        hint_used = False
        
        while len(wrong_guesses) < 6:
            self.display_game_state(word, guessed_letters, wrong_guesses)
            
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You won!")
                print(f"The word was: {word.upper()}")
                return True
            
            print("\nOptions:")
            print("1. Guess a letter")
            if not hint_used:
                print("2. Get a hint")
            print("3. Quit game")
            
            choice = input("Choose an option (1-3): ").strip()
            
            if choice == '1':
                guess = input("Enter a letter: ").lower().strip()
                
                if len(guess) != 1 or not guess.isalpha():
                    input("Please enter a single letter. Press Enter to continue...")
                    continue
                
                if guess in guessed_letters:
                    input("You already guessed that letter. Press Enter to continue...")
                    continue
                
                guessed_letters.add(guess)
                
                if guess not in word:
                    wrong_guesses.append(guess)
            
            elif choice == '2' and not hint_used:
                print(f"\nHint: {self.get_hint(word)}")
                hint_used = True
                input("Press Enter to continue...")
            
            elif choice == '3':
                print("Thanks for playing!")
                return False
            
            else:
                input("Invalid choice. Press Enter to continue...")
        
        self.display_game_state(word, guessed_letters, wrong_guesses)
        print("\nGame Over! You ran out of attempts.")
        print(f"The word was: {word.upper()}")
        return False
    
    def main_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("           HANGMAN GAME")
            print("=" * 50)
            print("1. Start New Game")
            print("2. How to Play")
            print("3. Exit")
            
            choice = input("Choose an option (1-3): ").strip()
            
            if choice == '1':
                self.play_game()
                play_again = input("\nPlay again? (y/n): ").lower().strip()
                if play_again != 'y':
                    break
            
            elif choice == '2':
                self.show_instructions()
            
            elif choice == '3':
                print("Thanks for playing Hangman!")
                break
            
            else:
                input("Invalid choice. Press Enter to continue...")
    
    def show_instructions(self):
        self.clear_screen()
        print("=" * 50)
        print("           HOW TO PLAY")
        print("=" * 50)
        print("1. A random word is selected")
        print("2. Guess letters one at a time")
        print("3. Wrong guesses add parts to the hangman")
        print("4. You have 6 wrong guesses before game over")
        print("5. Use hints wisely (only one per game)")
        print("6. Win by guessing all letters before hangman is complete")
        print("\nGood luck!")
        input("\nPress Enter to return to menu...")

def main():
    game = HangmanGame()
    game.main_menu()

if __name__ == "__main__":
    main()