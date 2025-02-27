import random

# Define two lists
list1 = ['lithium', 'sodium', 'potassium', 'calcium', 'copper (II)', 'magnesium', 'aluminium', 'iron (II)', 'iron (III)']
list2 = ['chloride', 'bromide', 'iodide', 'carbonate', 'sulfate']

# Randomly select one item from each list
item1 = random.choice(list1)
item2 = random.choice(list2)

# Function to answer questions about the items
def answer_question(item, category):
    if category == 'flame':
        flame = {
            'lithium': 'You observe a crimson flame',
            'sodium': 'You observe a yellow flame',
            'potassium': 'You observe a lilac flame',
            'calcium': 'You observe a brick-red flame',
            'copper (II)': 'You observe a blue-green flame',
        }
        return flame.get(item)

    elif category == 'sodium hydroxide':
        sodium_hydroxide = {
            'magnesium': 'A white precipitate forms',
            'calcium': 'A white precipitate forms',
            'aluminium': 'A white precipitate forms, then dissolves in solution',
            'copper (II)': 'A blue precipitate forms',
            'iron (II)': 'A dirty green precipitate forms',
            'iron (III)': 'A reddish brown precipitate forms'
        }
        return sodium_hydroxide.get(item)

    elif category == 'silver nitrate solution':
        silver_nitrate_solution = {
            'chloride': 'A white precipitate forms',
            'bromide': 'A cream precipitate forms',
            'iodide': 'A yellow precipitate forms',
        }
        return silver_nitrate_solution.get(item)

    elif category == 'dilute acid':
        dilute_acid = {
            'carbonate': 'CO₂ is produced',
        }
        return dilute_acid.get(item)

    elif category == 'barium chloride solution':
        barium_chloride_solution = {
            'sulfate': 'A white precipitate forms',
        }
        return barium_chloride_solution.get(item)
    else:
        return None  # Return None for invalid category or if no result

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

    # Display the answers only if they are not None or empty
    print(f"\nAnswers:")
    if answer1 or answer2:  # Check if at least one answer has a valid result
        if answer1:
            print(f"{answer1}")
        if answer2:
            print(f"{answer2}")
    else:
        print("You observe no changes.")  # Display this message if both answers are None


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
