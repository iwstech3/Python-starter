# TASK 1: GUESSING A LETTER IN A CHOSEN WORD
import random
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
# words=["cat", "play", "swim"]

print(words)

chosen_word = random.choice(words)
print(f"The word chosen is {chosen_word}")

guess=input("Guess a letter...: ")

# TASK 2: Replacing blanks with correct guessed letters
display=[]
for i in range(len(chosen_word)):
    display+="_"

print(display)
for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=guess
        print("yes")
    else:
        print("No")

# create an empty list called display , for each letter in the chosen word add a "_" to display
# if chosen word is cat=> display should be ['_','','']
# loop through each position in the chosen word, if the letter at position matches 'guess' then reveal that letter in the 

# TASK 3: CHECK IF USER HAS WON  and allow looping

# TASK4: KEEP TRACK OF PLAYER'S LIVE