# import random
# list=["apple","banana","grapes","strawberry","mango"]

# selection = random.choice(list)
# print("Welcome  to the Hangman!.")

# i=1
# while(i<6):
    
#     name=input("enter the name of fruit that  you like").lower()
#     if name == selection:
#         print("You have enetered the right  name")
#         break
#     else:
#         print("Try another guess")
#         print("Attempts leftt : {6-i}")
#         i+=1

#     if(i==5):
#         print("Game over ! the correct  fruit was",selection)


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
        print("💀 Game Over! The correct fruit was:", selection)
