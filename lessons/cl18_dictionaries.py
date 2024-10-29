"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
    }

# Access values by their key using subscription
print(ice_cream["chocolate"])

# Re-assign values by their key using assigning
ice_cream["vanilla"] += 10

# Romove items by key using the pop method
ice_cream.pop("strawberry")

# Test if a key is in the dictionary:
has_pbj: bool = "pbj" in ice_cream
print(has_pbj)


# Loop through items using for-in loops
total_orders: int = 0
for flavor in ice_cream:
    # The variable (e.g. flavor) iterates over
    # each key one-by-one in the dictionary
    print(flavor)
    total_orders += ice_cream[flavor]

# When attempt to access a key that is not in a dictionary, shows KeyError
print(ice_cream["pecan"])
