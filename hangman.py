import random

word_list = [
    ("apple", "🍎 A common fruit"),
    ("tiger", "🐅 A big wild cat"),
    ("chair", "🪑 You sit on it"),
    ("python", "🐍 A popular programming language"),
    ("brave", "🦁 Opposite of scared")
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def play_hangman():
    
    secret_word, hint = random.choice(word_list)
    guessed_letters = []
    attempts_left = 6
    display_word = ["_"] * len(secret_word)

    print("=" * 40)
    print("🎮 Welcome to HANGMAN!".center(40))
    print("=" * 40)
    print("💡 Hint:", hint)
    print()

    
    while attempts_left > 0 and "_" in display_word:
        print(HANGMAN_PICS[6 - attempts_left])
        print("Word: ", " ".join(display_word))
        print("Guessed letters:", " ".join(guessed_letters))
        guess = input("🔤 Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️  Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Good guess!\n")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            attempts_left -= 1
            print(f"❌ Wrong guess. Attempts left: {attempts_left}\n")

    
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word.upper())
    else:
        print(HANGMAN_PICS[6])
        print("💀 You're out of guesses.")
        print("The word was:", secret_word.upper())
        print("Better luck next time!")

play_hangman()