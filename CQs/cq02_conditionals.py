__author__ = 730774129
"""Practice with Conditionals, Local Variables, and User Input"""


def guess_a_number() -> None:
    """the following variables are local variables"""
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x) + ".")

    if x == 7:
        print("You got it!")
    elif x < 7:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
