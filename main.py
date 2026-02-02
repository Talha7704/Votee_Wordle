import requests
import random
import time

BASE_URL = "https://wordle.votee.dev:8000"

WORDS = [
    "raise", "stone", "audio", "table", "plant",
    "grape", "crane", "light", "sound", "track",
    "money", "heart", "water", "brain", "smile"
]

def make_guess(word):
    """
    Sends a guess to the /random endpoint.
    """
    url = BASE_URL + "/random"
    params = {
        "guess": word,
        "size": 5
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def is_correct(results):
    """
    All letters must be 'correct' to solve the word.
    """
    return all(letter["result"] == "correct" for letter in results)

def main():
    print("Starting Votee Wordle Solver (Random Mode)\n")

    attempts = 0
    used_words = set()

    while attempts < 6:
        guess = random.choice(WORDS)
        while guess in used_words:
            guess = random.choice(WORDS)

        used_words.add(guess)
        attempts += 1

        print("Attempt", attempts, "- Guess:", guess)

        try:
            results = make_guess(guess)
        except Exception as e:
            print("API error:", e)
            return

        print("Response:", results, "\n")

        if is_correct(results):
            print(" Word solved successfully!")
            return

        time.sleep(1)

    print("Failed to solve within 6 attempts.")

if __name__ == "__main__":
    main()

