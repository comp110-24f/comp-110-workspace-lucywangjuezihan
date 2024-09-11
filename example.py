# def sum(number_1: int, number_2: int) -> int:
#     return number_1 + number_2


# print(sum(5, 6))

# total = sum(5, 6)
# print(total)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no march!"


print(check_first_letter("happy", "h"))
print(check_first_letter("happy", "s"))
