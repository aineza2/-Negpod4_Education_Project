# Import necessary modules
import random
from languages import supported_languages, language_problem_sets



# Define initial user level
user_level = 1

# Function to introduce the app and provide rules and guidelines
def introduce_app():
    print(f"Hello! Welcome to the Vocabulary Trainer. You are in Level {user_level}.")
    print("Press 0 to see other menu options.")
    menu_choice = input("Your choice: ")

    if menu_choice == "0":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        introduce_app()

# Function to display language learning problems to the user
def display_problem(language):
    problem_set = language_problem_sets[language]
    word, translation = random.choice(list(problem_set.items()))
    print(f"Translate the word '{word}' to English.")

    return translation

# Function to obtain user input and confirm its correct format
def get_user_input():
    user_input = input("Your answer: ").strip().lower()
    return user_input

# Main menu function
def main_menu():
    print("\nMain Menu:")
    print("1. Learn and Practice")
    print("2. Rules and Guidelines")
    print("3. View Level")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Learn and Practice
        learn_and_practice_menu()
    elif choice == "2":
        # Rules and Guidelines
        rules_and_guidelines()
    elif choice == "3":
        # View Level
        print(f"\nYou are currently in Level {user_level}.\n")
        main_menu()
    elif choice == "4":
        # Exit
        print("Exiting the Language Vocabulary Trainer. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# Function to allow users to choose a language
def choose_language():
    print("\nChoose a language:")
    for i, language in enumerate(supported_languages, start=1):
        print(f"{i}. {language}")

    language_choice = input("Enter the number of your choice: ")

    if language_choice.isdigit() and 1 <= int(language_choice) <= len(supported_languages):
        selected_language = supported_languages[int(language_choice) - 1]
        learn_and_practice(selected_language)
    else:
        print("Invalid choice. Please try again.")
        choose_language()

# Function to learn and practice a specific language
def learn_and_practice(language):
    print(f"\nYou have selected {language}.")
    while True:
        translation = display_problem(language)
        user_input = get_user_input()

        if user_input == "exit":
            print("Exiting the Language Vocabulary Trainer. Goodbye!")
            break

        is_correct = check_answer(user_input, translation)
        display_result(is_correct)
        track_user_level(is_correct)

# Function to handle Learn and Practice menu
def learn_and_practice_menu():
    print("\nLearn and Practice Menu:")
    print("1. Pick a Language")
    print("2. Start Practice")
    print("3. Back to Main Menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Pick a Language
        choose_language()

    elif choice == "2":
        # Start Practice
        selected_language = random.choice(supported_languages)
        learn_and_practice(selected_language)

    elif choice == "3":
        # Back to Main Menu
        main_menu()

    else:
        print("Invalid choice. Please try again.")
        learn_and_practice_menu()


# Function to display language learning problems to the user
def display_problem(language):
    problem_set = language_problem_sets[language]
    word, translation = random.choice(list(problem_set.items()))
    print(f"Translate the word '{word}' to English.")
    return translation

# Function to obtain user input and confirm its correct format
def get_user_input():
    user_input = input("Your answer: ").strip().lower()
    return user_input

# Function to check the correctness of the user's answers
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer.lower()

# Function to display the results to the user
def display_result(is_correct):
    if is_correct:
        print("Correct! Well done.")
    else:
        print("Incorrect. Keep practicing.")

# Function to keep track of the user's level in the language learning process
def track_user_level(is_correct):
    global user_level

    if is_correct:
        user_level += 1
        print(f"Your level has increased to {user_level}.\n")
    else:
        user_level = max(1, user_level - 1)
        print(f"Your level has decreased to {user_level}.\n")

# Function to display rules and guidelines
def rules_and_guidelines():
    print("\nRules and Guidelines:")
    print("- You will be presented with words in a foreign language.")
    print("- Input the English translation in the provided format.")
    print("- Your goal is to master as many words as possible.\n")
    main_menu()

# Run the main function when the script is executed
if __name__ == "__main__":
    introduce_app()
