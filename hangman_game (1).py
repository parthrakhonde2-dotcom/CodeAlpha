import random

# Hangman Game

# Predefined words
words = ["python", "computer", "college", "student", "program"]

# Select random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
max_attempts = 6
wrong_attempts = 0

print("=" * 40)
print("🎮 WELCOME TO HANGMAN GAME 🎮")
print("=" * 40)

# Create hidden word display
display_word = ["_"] * len(secret_word)

# Game Loop
while wrong_attempts < max_attempts and "_" in display_word:

    print("\nWord: ", " ".join(display_word))
    print("Guessed Letters:", guessed_letters)
    print("Remaining Attempts:", max_attempts - wrong_attempts)

    # User input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("✅ Correct Guess!")

        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess

    # Wrong guess
    else:
        print("❌ Wrong Guess!")
        wrong_attempts += 1


# Final Result
print("\n" + "=" * 40)

if "_" not in display_word:
    print("🎉 Congratulations! You Won!")
    print("The word was:", secret_word)

else:
    print("💀 Game Over!")
    print("The correct word was:", secret_word)

print("=" * 40)
