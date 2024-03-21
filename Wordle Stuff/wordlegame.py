import random
def load_dic(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words
def is_valid_guess(guess, guesses):
    return guess in guesses
def evaluate_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m"+guess[i]
        else:
            if guess[i] in word:
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i]
    return str + "\033[0m"

def wordle(guesses, answers):
    print("Welcome to Wordle! Get 6 chances to guess a 5-letter word")
    secret_word = random.choice(answers)

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter Guess # "+str(attempts)+":").lower()
        if not is_valid_guess(guess, guesses):
            print("That word is not in the word list, try again:")
            continue
        if guess == secret_word:
            print(("Congratulations you beat the wordle in {} attempts").format(attempts))
            break
        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)
    if attempts > max_attempts:
        print(f"Game over. The secret word was: {secret_word}")

guesses_dic = "possible.txt"
answers_dic = "answers.txt"

guesses = load_dic("Texts/possible.txt")
answers = load_dic("Texts/answers.txt")

if __name__ == "__main__":
    wordle(guesses, answers)