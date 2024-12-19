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
        print(Flashcards)

        # Write updated flashcards to JSON file
        with open('flashcards.json', "w") as json_data:
            json.dump(Flashcards, json_data)

    #Review Questions
    score = 0
    if start == "2":
        print("Here are your current flashcards!")
        
        for i in range(len(Flashcards)):
            flashcard = Flashcards[i]
            input(f"Question {i+1}). {flashcard['question']}: ")
            correct = input(f"Answer {i+1}). {flashcard['answer']}\n Did you get it right? Type 'yes' to add to your score and see the next question! ")

            if correct.lower() == "yes":
                score += 1
        print(f"Your score is {score} out of {len(Flashcards)}")

    #Delete a flashcard
    if start == "3":
        print("Deleting a flashcard!")
        print("Here are your current flashcards!")
        for i, flashcard in enumerate(Flashcards):
            print(f"{i+1}. {flashcard['question']}")

        delete_index = int(input("Enter the number of the flashcard you want to delete: ")) - 1
        if 0 <= delete_index < len(Flashcards):
            del Flashcards[delete_index]
            print("Flashcard deleted.")
        else:
            print("Invalid index.")

    start = input("Please select an option from the list below by typing the number:\n 1. Create a Flashcard\n 2. Review Flashcards\n 3. Delete a Flashcard \n 4. Exit\n")

#Exit 
print("Exiting Anna's Flashcards")
