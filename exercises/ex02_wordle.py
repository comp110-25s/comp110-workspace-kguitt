"""Let's Play a Game of Wordle!"""

__author__: str = "730567850"


def contains_char(any_length: str, character: str) -> bool:
    """Identify if the word contains a single character and return boolean value."""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(any_length):
        if any_length[idx] == character:
            return True  # Returns True if the value at the index in a word is the same as the single character
        else:
            idx += 1  # Proceeds to next index if does not match the value of character
    return False


def emojified(guess: str, secret: str) -> str:
    """Return a string of emojis with codified colors based on guess."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    display: str = ""
    idx: int = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            display += GREEN_BOX  # Displays green box if letter at index is in same position as in secret word
        elif contains_char(secret, guess[idx]) == True:
            display += YELLOW_BOX  # Displays yellow box if letter is in the secret word but not in the correct position
        else:
            display += (
                WHITE_BOX  # Displays a white box if letter is not in the secret word
            )
        idx += 1  # Moves to the next index position
    return display


def input_guess(expected_length: int) -> str:
    """Prompt the user for a guess until expected length is achieved."""
    guess = input(
        f"Enter a {expected_length} character word:"
    )  # Prints if the user's guess matches the expected length
    while len(guess) != expected_length:
        guess = input(
            f"That wasn't {expected_length} chars! Try again:"
        )  # Prints if the user's guess does not match the expected length
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")  # Prints the number of the user's turn
        guess: str = input_guess(
            len(secret)
        )  # Initializes guess as a string of the length of the secret word
        print(emojified(guess, secret))  # Prints the codified version of user's guess

        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1  # Moves on to next turn if secret word is not guessed
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
