"""Guess the Word in the Structured Wordle"""

__author__ = "730774129"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    guess_num: int = 1  # code the number of guess and increase after each turn

    while guess_num <= 6:
        print(f"=== Turn {guess_num}/6 ===")  # the first statement using f-string
        guess = input_guess(secret_word_len=len(secret))
        emoji_result = emojified(guess=guess, secret=secret)
        print(emoji_result)

        if guess == secret:
            print(f"You won in {guess_num}/6 turns!")
            return None
        guess_num += 1

    print("X/6 - Sorry, try again tomorrow!")
    return None


def input_guess(secret_word_len: int) -> str:
    # the user inputs the length of the secret word
    """To match the length of the inputs"""
    secret_word: str = input(f"Enter a {secret_word_len} character word: ")

    while len(secret_word) != secret_word_len:
        secret_word = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return secret_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """To test if each index of the secret word matches the character"""
    assert len(char_guess) == 1
    index = 0

    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Use emojis to visualize the end result"""
    assert len(guess) == len(secret)
    index = 0
    result = ""  # create an empty place to add the visualized result

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            # use the key-word argument from the previous "contains_char" function
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1

    return result


if __name__ == "__main__":  # this needs to be put at the end of a file
    main(secret="codes")
