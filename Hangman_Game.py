import random

def get_random_word():
    words = ["python", "JavaScript", "HTML", "CSS"]
    return random.choice(words) # Make sure the word is lowercase for case consistency

def display_word(word, guessed_letters):
    # For each letter in the word, display the letter if it has been guessed, otherwise display '_'
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    word = get_random_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")

    while attempts > 0:
        # Display the word with correctly guessed letters and underscores
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts remaining: {attempts}")

        # Get the user's guess
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")

        # Check if the player has guessed all the letters in the word
        if set(word) <= set(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you ran out of attempts. The word was: {word}")

# Entry point of the program
if __name__ == "__main__":
    hangman()

