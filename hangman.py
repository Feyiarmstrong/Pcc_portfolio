import random

def choose_word():
    words = ['lion','elephent','tiger', 'giraffe', 'zebra', 'monkey', 'cheetah', 'hippopotamus']
    return random.choice(words)


def display_word (word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    print ("Welcome to Hangman!")
    secret_word =choose_word()
    guessed_letters = []
    attempts = 6


    while True:
        print ("\nAttempts left: ", attempts)
        print ("word:", display_word(secret_word, guessed_letters))
        guess = input ("guess a letter: ").lower()


        if guess in guessed_letters:
            print ("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)
        
        if guess not in secret_word:
            attempts -=1
            print ("Incorrect guess!")
            if attempts ==0:
                print ("Game over! The word was: ", secret_word)
                break
        else:
            print ("Correct guess!")

        if all( letter in guessed_letters for letter in secret_word):
            print ("Congratulation! You correctly guessed the word: ", secret_word)
            break


        print ( "Guessed letter:",guessed_letters)

if __name__ == "__main__":
        hangman()
