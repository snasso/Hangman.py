import os
import random
import json


# Array of words to be guessed
data = [
    "hey",
    "person",
    "you",
    "think",
    "youre",
    "better",
    "than",
    "me"
]

# Specify the folder where you want to save the file
folder_path = "/Users/sandro/VSCodeProjects/Hangman"
# os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

# Write the data to a JSON file in the specified folder
file_path = os.path.join(folder_path, "data.json")
with open(file_path, mode="w") as file:
    json.dump(data, file)


def start_game(nWrong):
    headSpot = "O" if nWrong > 0 else " "
    bodySpot = "|" if nWrong > 1 else " "
    leftArm = "/" if nWrong > 2 else " "
    rightArm = "\\" if nWrong > 3 else " "
    leftLeg = "/" if nWrong > 4 else " "
    rightLeg = "\\" if nWrong > 5 else " "

    print("Hangman")
    print(" ___ ")
    print(" |  | ")
    print(f" |  {headSpot}")
    print(f" | {leftArm}{bodySpot}{rightArm}")
    print(f" | {leftLeg} {rightLeg}")
    print("\n")

def get_random_word(words):
    index = random.randint(0, len(words) - 1)
    return words[index]

def check_guess(pastGuesses):
    guess = input("Guess a letter (a-z): ").lower()

    if len(guess) > 1:
        print("Please enter only 1 letter at a time.")
        return check_guess(pastGuesses)
    elif guess in pastGuesses:
        print("You have already tried this letter.")
        return check_guess(pastGuesses)
    else:
        return guess

def play_game():
    # Reading the Array of words from a JSON file
    with open(file_path, mode="r") as file:
        words = json.load(file)

    answer = get_random_word(words)
    nWrong = 0
    pastGuesses = []


    while nWrong < 6:
        os.system('clear')
        start_game(nWrong)

        str = ""
        for i in range(len(answer)):
            if answer[i] in pastGuesses:
                str += answer[i] + " "
            else:
                str += "_ "

        print(f"{str}\n")

        # Remove spaces and underscores from the string
        stripped_str = str.replace(" ", "").replace("_", "")
        if stripped_str == answer:
            print("Success")
            break

        if pastGuesses:
            print(f"Past Guesses: {pastGuesses}")

        print(f"You have {6-nWrong} guesses remaining")

        guess = check_guess(pastGuesses)
        pastGuesses.append(guess)

        if guess not in answer:
            nWrong += 1

    if nWrong == 6:
        os.system('clear')
        start_game(nWrong)
        print(f"Past Guesses: {pastGuesses}")
        print(f"Answer: {answer}")
        print("Game Over")


while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

