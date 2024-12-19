#Import
import json

#Flashcard dictionaries. List of dictionaries
Flashcards = [{"question": "Test Question",
               "answer": "Test Answer"}]

#Create JSON file to store my flashcards
try:
    with open('flashcards.json', "r") as json_data:
        Flashcards = json.load(json_data)
except FileNotFoundError:
    Flashcards = []

start = input("Hello! Welcome to Anna's Flashcard Study Guide.\nPlease select an option from the list below by typing the number:\n 1. Create a Flashcard\n 2. Review Flashcards\n 3. Delete a Flashcard \n 4. Exit\n")

while start != "4":
    #Create a flashcard
    if start == "1":
        print("Creating a new flashcard!")
        question = input("Please type in your new flashcard's Question here: ")
        answer = input("Please type in your new flashcard's Answer here: ")

        flashcard = {"question": question, "answer": answer}
        Flashcards.append(flashcard)

        # Write updated flashcards to JSON file
        with open('flashcards.json', "w") as json_data:
            json.dump(Flashcards, json_data)

    #Review Questions
    if start == "2":
        if len(Flashcards) == 0:
            print("You have no flashcards to review.")
            start = input("Please select an option from the list below by typing the number:\n 1. Create a Flashcard\n 2. Review Flashcards\n 3. Delete a Flashcard \n 4. Exit\n")
            continue

        print("Here are your current flashcards!")
        for i in range(len(Flashcards)):
            flashcard = Flashcards[i]
            input(f"Question {i+1}). {flashcard['question']}\n Press Enter to see the Answer.")
            input(f"Answer {i+1}). {flashcard['answer']}\n Did you get it right? Press enter to see next question.")

    if start == "3":
        print("Deleting a flashcard!")
        for i in range(len(Flashcards)):
            flashcard = Flashcards[i]
            print(f"Question {i+1}). {flashcard['question']}")
            print(f"Answer {i+1}). {flashcard['answer']}")

        delete = int(input("Enter the number of the question you would like to delete: ")) - 1
        if 0 <= delete < len(Flashcards):
            del Flashcards[delete]
            print("Flashcard deleted.")
        else:
            print("Invalid selection.")

            # Write updated flashcards to JSON file
        with open('flashcards.json', "w") as json_data:
            json.dump(Flashcards, json_data)

    start = input("Please select an option from the list below by typing the number:\n 1. Create a Flashcard\n 2. Review Flashcards\n 3. Delete a Flashcard \n 4. Exit\n")
   
print("Exiting Anna's Flashcards")
