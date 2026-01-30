# Hangman Game

A feature-rich word guessing game with visual hangman display, hints, and custom word management.

## Features
- Visual ASCII hangman progression
- Hint system (one per game)
- Custom word management with JSON storage
- Clean terminal interface with menu system
- Multiple game modes (basic and enhanced)
- Save/load custom word lists

## Files
- `hangman.py` - Basic hangman game with built-in words
- `enhanced_hangman.py` - Advanced version with word manager integration
- `word_manager.py` - Custom word list management system

## How to Play
1. Run the game: `python enhanced_hangman.py`
2. Guess letters to reveal the hidden word
3. Use hints wisely (only one per game)
4. Avoid 6 wrong guesses or the hangman is complete!

## Word Management
- Add custom words with hints
- Remove unwanted words
- View all available words
- Words automatically saved in `words.json`

## Game Controls
- Enter single letters to guess
- Type 'hint' for a clue
- Type 'quit' to exit current game

## Installation
No external dependencies required - uses only Python standard library.

```bash
python hangman.py          # Basic version
python enhanced_hangman.py # Enhanced version with word manager
python word_manager.py     # Standalone word management
```

## Author
Created for Shadow Fox Internship Task