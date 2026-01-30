import random
import os
from word_manager import WordManager

class EnhancedHangman:
    def __init__(self):
        self.word_manager = WordManager()
        self.default_words = [
            'python', 'programming', 'computer', 'algorithm', 'function',
            'variable', 'database', 'software', 'hardware', 'internet'
        ]
        self.default_hints = {
            'python': 'A popular programming language',
            'programming': 'Writing code to create software',
            'computer': 'Electronic device for processing data',
            'algorithm': 'Step-by-step problem solving method',
            'function': 'Reusable block of code',
            'variable': 'Storage location with a name',
            'database': 'Organized collection of data',
            'software': 'Computer programs and applications',
            'hardware': 'Physical components of a computer',
            'internet': 'Global network of computers'
        }
        
        self.hangman_art = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
        ]
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_word_list(self):
        """Get words from word manager or use defaults"""
        custom_words = self.word_manager.get_words()
        return custom_words if custom_words else self.default_words
    
    def get_hint(self, word):
        """Get hint from word manager or defaults"""
        custom_hint = self.word_manager.get_hint(word)
        if custom_hint != "No hint available":
            return custom_hint
        return self.default_hints.get(word, "No hint available")
    
    def display_game(self, word, guessed, wrong_guesses, hint_used):
        self.clear_screen()
        print("ENHANCED HANGMAN")
        print("=" * 30)
        
        print(self.hangman_art[len(wrong_guesses)])
        
        display = " ".join([letter if letter in guessed else "_" for letter in word])
        print(f"\nWord: {display}")
        print(f"Wrong: {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"Attempts left: {6 - len(wrong_guesses)}")
        
        if hint_used:
            print(f"Hint: {self.get_hint(word)}")
    
    def play_round(self):
        words = self.get_word_list()
        if not words:
            print("No words available! Add some words first.")
            return False
            
        word = random.choice(words).lower()
        guessed_letters = set()
        wrong_guesses = []
        hint_used = False
        
        while len(wrong_guesses) < 6:
            self.display_game(word, guessed_letters, wrong_guesses, hint_used)
            
            if all(letter in guessed_letters for letter in word):
                print(f"\nYOU WIN! The word was: {word.upper()}")
                return True
            
            print(f"\nGuessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
            
            action = input("Enter letter, 'hint' for clue, or 'quit': ").lower().strip()
            
            if action == 'quit':
                return False
            elif action == 'hint' and not hint_used:
                hint_used = True
                continue
            elif len(action) == 1 and action.isalpha():
                if action in guessed_letters:
                    input("Already guessed! Press Enter...")
                    continue
                
                guessed_letters.add(action)
                if action not in word:
                    wrong_guesses.append(action)
            else:
                input("Invalid input! Press Enter...")
        
        self.display_game(word, guessed_letters, wrong_guesses, hint_used)
        print(f"\nGAME OVER! The word was: {word.upper()}")
        return False
    
    def main_menu(self):
        while True:
            self.clear_screen()
            print("ENHANCED HANGMAN")
            print("=" * 30)
            print("1. Play Game")
            print("2. Manage Words")
            print("3. Instructions")
            print("4. Exit")
            
            choice = input("\nSelect option (1-4): ").strip()
            
            if choice == '1':
                won = self.play_round()
                if input(f"\n{'Play again' if won else 'Try again'}? (y/n): ").lower() != 'y':
                    continue
            elif choice == '2':
                self.word_manager.manage_words()
            elif choice == '3':
                self.show_instructions()
            elif choice == '4':
                print("Thanks for playing!")
                break
            else:
                input("Invalid choice! Press Enter...")
    
    def show_instructions(self):
        self.clear_screen()
        print("HOW TO PLAY")
        print("=" * 20)
        print("• Guess the hidden word letter by letter")
        print("• 6 wrong guesses = game over")
        print("• Type 'hint' for a clue (once per game)")
        print("• Type 'quit' to exit current game")
        print("• Manage custom words in Word Manager")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    game = EnhancedHangman()
    game.main_menu()