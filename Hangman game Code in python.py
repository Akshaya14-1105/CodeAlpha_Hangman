import random

# Step 1: List of predefined words
word_list = ["apple", "python", "code", "hangman", "alpha"]
chosen_word = random.choice(word_list)

# Step 2: Game setup
guessed_word = ["_"] * len(chosen_word)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")
print("You have 6 incorrect guesses. Good luck!\n")

# Step 3: Game loop
while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("Current word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    # Validate single alphabet input
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single alphabet letter.\n")
        continue

    # Check for repeated guess
    if guess in guessed_letters:
        print("🔁 You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct guess!\n")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! {max_guesses - incorrect_guesses} tries left.\n")

# Step 4: Game result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("😞 Game Over! The word was:", chosen_word)
