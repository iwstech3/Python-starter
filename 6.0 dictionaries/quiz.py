from prettytable import PrettyTable
# import prettytable
# prettytable.

# table=PrettyTable()
# table.add_column("name", ["j1","j2", "j3"])
# table.add_column("age", [12,"j2", "j3"])



# pip install prettytable

import sys
print(sys.executable)

# A dictionary of 20 True/False questions about Python and general facts
quiz_questions = {
    "Python is an interpreted language.": "True",
    "Guido van Rossum created Python.": "True",
    "Python was first released in 1995.": "False",  # It was released in 1991
    "Python's name was inspired by 'Monty Python's Flying Circus.'": "True",
    "You must always declare the data type of variables in Python.": "False",
    "Lists in Python can contain elements of different data types.": "True",
    "The 'print' function can accept multiple arguments.": "True",
    "The standard file extension for Python files is '.pt'.": "False",  # It's .py
    "Python is case-sensitive.": "True",
    "Python supports multiple inheritance.": "True",
    "A tuple is mutable in Python.": "False",
    "Python's default recursion limit is around 1000.": "True",
    "A dictionary in Python was always guaranteed to be ordered.": "False",
    "PEP 8 is the official Python style guide.": "True",
    "Python uses curly braces '{}' for code blocks.": "False",
    "Python is open-source software.": "True",
    "You can use 'pip' to install Python packages.": "True",
    "The keyword 'elif' is used for multi-branch condition in Python.": "True",
    "The keyword 'def' is used to define a new class.": "False",  # It's for functions; 'class' is used for classes
    "Python uses indentation to define code blocks.": "True",
}


# Create a PrettyTable to store results
score_table = PrettyTable()
score_table.field_names = ["Player Name", "Score (out of 20)"]

play_again = True

while play_again:
    # Ask for the player's name
    player_name = input("Enter your name: ").strip()
    
    # Initialize score
    score = 0
    
    print("\nWelcome to the True/False Quiz! Answer 'True' or 'False' to each statement.\n")
    
    # Ask each question
    for question, correct_answer in quiz_questions.items():
        print(question)
        user_answer = input("Your answer (True/False): ").strip().capitalize()
        
        # Check correctness (case-insensitive)
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")
    
    # Add the player's name and score to the table
    score_table.add_row([player_name, score])
    
    # Ask if the user wants to play again
    choice = input("Do you want to play again? (y/n): ").lower()
    if choice != 'y':
        play_again = False

# Display the summary of results once the user finishes
print("\n===== Summary of All Results =====")
print(score_table)
