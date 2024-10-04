"""To concate two strings"""

__author__ = "730774129"


def concat(word1: str, word2: str) -> str:
    """To concat the two word inputs"""
    return word1 + word2


if __name__ == "__main__":  # suppress the function call when importing
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
