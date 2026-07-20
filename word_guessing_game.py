# THE WORD GUESSING GAME
# Concepts used: lists & strings, random module, i/o handling, control flow statements

import random
word_bank = [
    "skibidi", "tung tung", "sybau", "football", "olivia",
    "ronaldo", "argentina", "colors", "espanol", "english", "python",
    "banana", "rainbow", "apple", "truck", "cars", "ELon Musk",
    "sigma", "rizz", "gyatt", "fanum", "ohio", "delulu", "copium", "hopium",
    "goober", "goofy", "npc", "yeet", "sheesh", "mog", "mogged", "aura",
    "based", "cringe", "mid", "peak", "lore", "canon", "brainrot", "nocap",
    "bet", "blud", "unc", "goated", "drip", "glazing", "zaza", "bussin",
    "sus", "lockin", "cook", "cooked", "crashout", "fumble", "ratio",
    "yapping", "gremlin", "goblin", "bingus", "skrunkly", "goob", "floof",
    "blorp", "meow", "eepy", "lullaby", "Odyssey", "Panther",
    "blud", "stonks", "bonk", "beepboop", "baka", "jonkler", "gigachad",
    "chad", "alpha", "beta", "lilbro", "subway", "wompwomp", "touchgrass",
    "nahidwin", "sukuna", "gojo", "silly", "goose", "quantum",
    "pickle", "waffle", "microwave", "toaster", "cactus", "mango", "kiwi",
    "pineapple", "coconut", "potato", "cheese", "nugget", "cookie",
    "pancake", "pretzel", "croissant", "donut", "muffin",
    "penguin", "capybara", "axolotl", "platypus", "hamster", "otter",
    "pigeon", "raccoon", "frog", "shark", "dinosaur", "wizard", "pirate",
    "alien", "robot", "spaceship", "galaxy", "comet", "meteor", "volcano",
    "thunder", "lightning", "tornado", "nebula", "pixel", "keyboard",
    "monitor", "internet", "discord", "minecraft", "roblox", "fortnite"
]

print("\n--- Word Chosen! Start Guessing ---")

word = random.choice(word_bank)
secretWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(secretWord))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                secretWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in secretWord:
        print('\nCongratulations!! You guessed the word: ' + word + '\n')
        break

    if attempts == 0 and '_' in secretWord:
        print('\n💀 Game over! The secret word was: ' + word + '\n')