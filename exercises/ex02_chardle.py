"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = 730774129


def main() -> None:
    """handles all the function calls and variable assignments needed"""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """gather the user's input to determine a word input"""
    word: str = input("Enter a 5-character word: ")
    # the name of the local variable should not be "input"

    if len(word) != 5:  # if-else condition to test the length first
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return word


def input_letter() -> str:
    """gather the user's input to determine a letter input"""
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    """take and compare the two inputs to see if they match"""
    index: int = 0
    count: int = 0  # the count starts at 0 if no matches
    print("Searching for " + letter + " in " + word)

    while index < 5:
        if word[index] == letter:
            count = count + 1
            print(letter + str(" found at index ") + str(index))
        index = index + 1  # index increase should be outside of if statement

    if count == 0:
        print("No" + str(" instances of ") + letter + " found in " + word)
    else:
        print(str(count) + str(" instances of ") + letter + " found in " + word)
        # no need to return anything, but only to print


if __name__ == "__main__":  # Function 1: enable to run the Python program as a module
    main()  # Function 2: enable other modules to import your functions and reuse them
