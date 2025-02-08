import random

print('''
      
      88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
             
      
      ''')


print(''' 
      
       ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
      
      ''')


stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



lives=0


# TASK 1: GUESSING A LETTER IN A CHOSEN WORD


# TASK 2: Replacing blanks with correct guessed letters
# create an empty list called display , for each letter in the chosen word add a "_" to display
# if chosen word is cat=> display should be ['_','','']
# loop through each position in the chosen word, if the letter at position matches 'guess' then reveal that letter in the 

# TASK 3: CHECK IF USER HAS WON  and allow looping

# TASK4: KEEP TRACK OF PLAYER'S LIVE

#TASK 3: CHECK IF USER HAS WON  and allow looping
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

print(words)

chosen_word = random.choice(words)
print(f"The word chosen is {chosen_word}")
game_end=False
display=[]
for _ in chosen_word:
    display+="_"
# print(display)

while not game_end:
    

    guess=input("Enter a letter: ").lower() 


   


    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            print("yes")
            display[position]=letter
    if guess not in chosen_word:
        lives+=1
        if lives==6:
            game_end=True
            print("you lose")
    print(display)

    if "_" not in display:
        game_end=True
        print("you won")
    print(stages[lives])

