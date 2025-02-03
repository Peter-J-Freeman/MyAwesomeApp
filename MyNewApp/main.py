import random

def tell_bad_joke():
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call cheese that isn’t yours? Nacho cheese!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What’s brown and sticky? A stick!"
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    # This section of code calls the function tell_bad_joke
    print(tell_bad_joke())

