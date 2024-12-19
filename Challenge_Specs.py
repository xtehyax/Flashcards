# ### *Challenge: Flashcard Study App*
# Create a console-based flashcard app where users can create, review, and manage flashcards.

# ---

# #### *Features to Implement*

# 1. *Main Menu*
#    - Display a menu to the user with options:
#      - *1. Create a Flashcard*
#      - *2. Review Flashcards*
#      - *3. Delete a Flashcard*
#      - *4. Exit*

# 2. *Create a Flashcard*
#    - Allow the user to enter a *question* and an *answer*.
#    - Save these in a dictionary (or JSON file for persistence).

# 3. *Review Flashcards*
#    - Randomly select a flashcard and display its question.
#    - Wait for the user to press Enter to reveal the answer.
#    - Ask the user if they got it correct or not and keep track of their score.

# 4. *Delete a Flashcard*
#    - List all flashcards by question.
#    - Allow the user to delete a flashcard by selecting its number.

# 5. *Exit*
#    - Save flashcards to a file (e.g., JSON) so they persist between sessions.
#    - Allow the user to quit the app.

# ---

# #### *Example Workflow*

# plaintext
# Welcome to Flashcard Study App!
# 1. Create a Flashcard
# 2. Review Flashcards
# 3. Delete a Flashcard
# 4. Exit

# Choose an option: 1

# Enter the question: What is the capital of France?
# Enter the answer: Paris

# Flashcard created successfully!

# Choose an option: 2

# Question: What is the capital of France?
# Press Enter to reveal the answer...
# Answer: Paris
# Did you get it correct? (y/n): y

# Choose an option: 4
# Goodbye!

# ---

# #### *Extra Challenges*
# - Add categories for flashcards (e.g., "Geography", "Math").
# - Implement a spaced repetition algorithm for reviewing cards.
# - Build a GUI version using tkinter or PyQt.
# - Add user authentication to save flashcards per user.

# ---