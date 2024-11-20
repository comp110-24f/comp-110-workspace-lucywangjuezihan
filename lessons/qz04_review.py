"""Reviewing dogs' performance in daycare."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Determine if all dogs were good in daycare."""

    num_dogs: int = len(scores)

    # Edge cases
    if thresh < 0 or thresh > 10:
        raise ValueError("Threshold not between 0 and 10")
    elif idx >= num_dogs:
        raise IndexError("idx too high!")

    # Base case
    # If score isn't high enough, return False for all fn calls
    elif int((scores[idx]["scores"])) < thresh:
        return False

    # Recursive case
    else:
        if num_dogs == idx + 1:
            return True
        else:
            print(f"Good dog, {scores[idx]["names"]}!")
            return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "8"},
    {"name": "Pep", "score": "7"},
]

all_good(pack, 8, 0)
