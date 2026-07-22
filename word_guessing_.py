# THE WORD GUESSING GAME
# Concepts used: lists & strings, random module, i/o handling, control flow statements

import random

# word_bank = ["skibidi", "tung tung", "sybau", "bomabardino", "football", "olivia",
#               "ronaldo", "argentina", "colors", "espanol", "english", "python",
#               "banana", "rainbow", "apple", "truck", "cars", "ELon Musk"]

word_bank = {
    "celebrity": ["Brad Pitt", "Zendaya", "Lionel Messi", "Ronaldo", "Elon Musk"],
    "meme": ["Skibidi", "Sybau", "Son", "Balerrina Cappucina", "Tralalero Tralala", "Tung Tung Sahur", "Bombardino"],
    "random": ["Apple", "Banana", "Mango", "Strawberry", "Rainbow", "Cucumber", "Ghost", "Bike"]
    #movie song 
}
# For this example, let's pretend the player typed these two:
available_categories = ", ".join(word_bank.keys())
print(f"Available categories: {available_categories}")

# .strip() removes accidental spaces, .lower() ensures case-insensitivity
user_input = input("Enter categories you want to mix (separated by commas): ")
player_choices = [choice.strip().lower() for choice in user_input.split(",")]

# 4. Combine chosen categories into active game list
active_words = []
for category in player_choices:
    if category in word_bank:
        active_words.extend(word_bank[category])

# word = random.choice(word_bank)
secret_word = random.choice(active_words)
print("\n--- Word Chosen! Start Guessing ---")
# guessed_word = ["_"] * len(word)

      
attempts = 9
while attempts > 0:
    print("\nCurrent word " + "".join(guessed_word))
    guess = input("Enter a letter : ").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Great guess ! ")
    else:
        attempts -= 1
        print("Wrong Guess! .. Attempts left: " + str(attempts))

    if "_" not in guessed_word:
        print("\nCongratulations!! You guessed the word : " + word)
        break
    if attempts == 0 and "_" in guessed_word:
        print("\n💀 Game over! The secret word was: : " + word)
