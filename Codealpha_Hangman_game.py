import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "development", "random", "game"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def play_game():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses. Good luck!")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            incorrect_guesses += 1
            print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")

        if incorrect_guesses == max_incorrect_guesses:
            print("Sorry, you've run out of guesses. The word was:", word)

if __name__ == "__main__":
    play_game()
