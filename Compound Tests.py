import random
import tkinter as tk
from tkinter import messagebox

# Define two lists
list1 = ['lithium', 'sodium', 'potassium', 'calcium', 'copper (II)', 'magnesium', 'aluminium', 'iron (II)', 'iron (III)']
list2 = ['chloride', 'bromide', 'iodide', 'carbonate', 'sulfate']

# Randomly select one item from each list
item1 = random.choice(list1)
item2 = random.choice(list2)

# Function to answer questions about the items
positive_false = False
negative_false = False
def answer_question(item, category):
    if category == 'flame':
        flame = {
            'lithium': 'crimson',
            'sodium': 'yellow',
            'potassium': 'lilac',
            'calcium': 'brick-red',
            'copper (II)': 'blue-green',
        }
        return flame.get(item, 'Unchanged flame')
        positive_false = True

    elif category == 'sodium hydroxide':
        sodium_hydroxide = {
            'magnesium': 'white precipitate',
            'calcium': 'white precipitate',
            'aluminium': 'white precipitate, then dissolved',
            'copper (II)': 'blue precipitate',
            'iron (II)': 'dirty green precipitate',
            'iron (III)': 'reddish brown precipitate'
        }
        return sodium_hydroxide.get(item, 'No reaction')
        positive_false = True

    elif category == 'silver nitrate solution':
        silver_nitrate_solution = {
            'chloride': 'white precipitate',
            'bromide': 'cream precipitate',
            'iodide': 'yellow precipitate',
        }
        return silver_nitrate_solution.get(item, 'No reaction')
        negative_false = True

    elif category == 'dilute acid':
        dilute_acid = {
            'carbonate': 'CO2 produced',
        }
        return dilute_acid.get(item, 'No CO2 produced')
        negative_false = True

    elif category == 'barium chloride solution':
        barium_chloride_solution = {
            'sulfate': 'white precipitate',
        }
        return barium_chloride_solution.get(item, 'No reaction')
        negative_false = True
    else:
        return 'Invalid category'

# Initialize question count
question_count = 0

# Allow the user to ask multiple questions
while True:
    print("\nWhat test?")
    print("Options: flame, sodium hydroxide, silver nitrate solution, dilute acid, barium chloride solution")
    user_question = input("Enter your choice (or type 'exit' to stop): ").strip().lower()

    if user_question == 'exit':
        break

    # Increment question count
    question_count += 1

    # Get answers for both items
    answer1 = answer_question(item1, user_question)
    answer2 = answer_question(item2, user_question)

    # Display the answers
    print(f"\nAnswers:")
    if not positive_false:
        print(f"Positive ion - {answer1}")
    if not negative_false:
        print(f"Negative ion - {answer2}")
    positive_false = False
    negative_false = False

# Ask the user to guess the items
print("\nCan you guess the compound?")
guess1 = input(f"What was the positive ion?").strip().lower()
guess2 = input(f"What was the negative ion?").strip().lower()

# Check the user's guesses
correct_count = 0

if guess1 == item1:
    print(f"Correct! The positive ion is indeed {item1}.")
    correct_count += 1
else:
    print(f"Incorrect. The positive ion was {item1}.")

if guess2 == item2:
    print(f"Correct! The negative ion is indeed {item2}.")
    correct_count += 1
else:
    print(f"Incorrect. The negative ion was {item2}.")

# Calculate score
score = correct_count * 10 - question_count
score = max(score, 0)  # Ensure the score doesn't go negative

print(f"\nYour score is: {score}/20")
