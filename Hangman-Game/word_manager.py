import json
import os

class WordManager:
    def __init__(self, filename='words.json'):
        self.filename = filename
        self.load_words()
    
    def load_words(self):
        """Load words from JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.words = data.get('words', [])
                self.hints = data.get('hints', {})
        else:
            self.words = []
            self.hints = {}
    
    def save_words(self):
        """Save words to JSON file"""
        data = {
            'words': self.words,
            'hints': self.hints
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)
    
    def add_word(self, word, hint=""):
        """Add a new word with optional hint"""
        word = word.lower().strip()
        if word and word not in self.words:
            self.words.append(word)
            if hint:
                self.hints[word] = hint
            self.save_words()
            return True
        return False
    
    def remove_word(self, word):
        """Remove a word"""
        word = word.lower().strip()
        if word in self.words:
            self.words.remove(word)
            if word in self.hints:
                del self.hints[word]
            self.save_words()
            return True
        return False
    
    def get_words(self):
        """Get all words"""
        return self.words
    
    def get_hint(self, word):
        """Get hint for a word"""
        return self.hints.get(word.lower(), "No hint available")
    
    def manage_words(self):
        """Interactive word management"""
        while True:
            print("\n" + "=" * 40)
            print("         WORD MANAGER")
            print("=" * 40)
            print("1. View all words")
            print("2. Add word")
            print("3. Remove word")
            print("4. Back to main menu")
            
            choice = input("Choose option (1-4): ").strip()
            
            if choice == '1':
                if self.words:
                    print(f"\nWords ({len(self.words)}):")
                    for i, word in enumerate(self.words, 1):
                        hint = self.hints.get(word, "No hint")
                        print(f"{i}. {word.upper()} - {hint}")
                else:
                    print("\nNo words available.")
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                word = input("Enter new word: ").strip()
                hint = input("Enter hint (optional): ").strip()
                if self.add_word(word, hint):
                    print(f"Added '{word}' successfully!")
                else:
                    print("Word already exists or invalid.")
                input("Press Enter to continue...")
            
            elif choice == '3':
                word = input("Enter word to remove: ").strip()
                if self.remove_word(word):
                    print(f"Removed '{word}' successfully!")
                else:
                    print("Word not found.")
                input("Press Enter to continue...")
            
            elif choice == '4':
                break
            
            else:
                print("Invalid choice!")
                input("Press Enter to continue...")

if __name__ == "__main__":
    manager = WordManager()
    manager.manage_words()