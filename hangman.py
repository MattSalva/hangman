# Write your code here
import random

words = ('python', 'kotlin', 'java', 'javascript')
word = random.choice(words)
letters = set(word)
guesses = []
indices = []
ordered_letters = []
secret_temp = list(word)
replace = "-"
tries = 1
runs = 0
for index, letter in enumerate(word):
    indices.append(index)
    secret_temp[index] = replace

secret_word = "".join(secret_temp)
print("H A N G M A N")
while tries < 9:
    if runs == 0:
        print('Type "play" to play the game, "exit" to quit: ')
        option = input()
        if option == 'exit':
            break
        elif option == 'play':
            pass

    runs += 1
    if word == secret_word:
        print("You guessed the word!")
        print("You survived!")
        break
    print(f'''

    {secret_word}
    "Input a letter: "
    ''')
    guess = input()

    if len(guess) > 1:
        print("You should input a single letter")
        continue

    if not guess.islower():
        print("Please enter a lowercase English letter")
        continue

    if guess in guesses:
        print("You've already guessed this letter")
        continue

    guesses.append(guess)

    if guess in letters and word.count(guess) < 2:
        secret_word = list(secret_word)
        secret_word[word.find(guess)] = guess
        letters.remove(guess)
        secret_word = "".join(secret_word)

    elif guess in letters and word.count(guess) >= 2:
        secret_word = list(secret_word)
        for index in indices:
            if word[index] == guess:
                secret_word[index] = guess
        secret_word = "".join(secret_word)
        letters.remove(guess)

    elif word == secret_word:
        print("You guessed the word!")
        print("You survived!")
        break

    elif word.count(guess) >= 1 and guess not in letters:
        print("No improvements")
        tries += 1
        if tries == 9:
            print("You lost!")
            break

    else:
        print("That letter doesn't appear in the word")
        tries += 1
        if tries == 9:
            print("You lost!")
            print('Type "play" to play the game, "exit" to quit: ')
            option = input()
            if option == 'exit':
                break
            elif option == 'play':
                continue
