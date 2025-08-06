import random

# 🔸 List of strings (fruits)
words = ["apple", "banana", "grapes", "strawberry", "mango"]

# 🔸 Randomly select one string
selection = random.choice(words)

# 🔸 Strings in print statements
print("🎮 Welcome to Hangman!")
print("Guess the correct fruit name. You have 6 tries.")

attempts = 0
while attempts < 6:
    # 🔸 This input returns a string
    name = input("Enter the name of a fruit: ").lower()
    
    # 🔸 String comparison
    if name == selection:
        print("✅ You have entered the right name! 🎉")
        break
    else:
        attempts += 1
        print("❌ Try another guess.")
        print(f"Attempts left: {6 - attempts}")  # f-string

    if attempts == 6:
        print(" Game Over! The correct fruit was:", selection)

