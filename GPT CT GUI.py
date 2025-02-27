import random
import tkinter as tk
from tkinter import messagebox

# Define two lists
list1 = ['lithium', 'sodium', 'potassium', 'calcium', 'copper (II)', 'magnesium', 'aluminium', 'iron (II)', 'iron (III)']
list2 = ['chloride', 'bromide', 'iodide', 'carbonate', 'sulfate']

# Randomly select one item from each list
item1 = random.choice(list1)
item2 = random.choice(list2)

# Initialize question count
question_count = 0
correct_count = 0

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

def ask_question():
    global question_count
    category = category_entry.get().strip().lower()
    if not category:
        messagebox.showwarning("Input Error", "Please enter a test category.")
        return

    # Increment question count
    question_count += 1

    # Get answers for both items
    answer1 = answer_question(item1, category)
    answer2 = answer_question(item2, category)

    # Display the answers only if they are not None or empty
    response = "Answers:\n"
    if answer1 or answer2:  # Check if at least one answer has a valid result
        if answer1:
            response += f"{answer1}\n"
        if answer2:
            response += f"{answer2}\n"
    else:
        response += "You observe no changes."  # Display this message if both answers are None

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, response)

def check_guesses():
    global correct_count
    guess1 = positive_entry.get().strip().lower()
    guess2 = negative_entry.get().strip().lower()

    if guess1 == item1:
        response = f"Correct! The positive ion is indeed {item1}.\n"
        correct_count += 1
    else:
        response = f"Incorrect. The positive ion was {item1}.\n"

    if guess2 == item2:
        response += f"Correct! The negative ion is indeed {item2}.\n"
        correct_count += 1
    else:
        response += f"Incorrect. The negative ion was {item2}.\n"

    # Calculate score
    score = correct_count * 10 - question_count
    score = max(score, 0)  # Ensure the score doesn't go negative

    response += f"\nYour score is: {score}/20"
    messagebox.showinfo("Results", response)

# Create the main window
root = tk.Tk()
root.title("Chemical Test GUI")

# Create input fields for test category
tk.Label(root, text="Enter Test Category:").pack(pady=5)
category_entry = tk.Entry(root)
category_entry.pack(pady=5)

# Button to ask the question
ask_button = tk.Button(root, text="Ask Question", command=ask_question)
ask_button.pack(pady=10)

# Text box to display results
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# Input fields for guesses
tk.Label(root, text="Guess the Positive Ion:").pack(pady=5)
positive_entry = tk.Entry(root)
positive_entry.pack(pady=5)

tk.Label(root, text="Guess the Negative Ion:").pack(pady=5)
negative_entry = tk.Entry(root)
negative_entry.pack(pady=5)

# Button to check guesses
check_button = tk.Button(root, text="Check Guesses", command=check_guesses)
check_button.pack(pady=10)

# Available tests label
available_tests_label = tk.Label(root, text="Available Tests:\n- flame\n- sodium hydroxide\n- silver nitrate solution\n- dilute acid\n- barium chloride solution")
available_tests_label.pack(pady=10)

# Run the application
root.mainloop()

