import random
from languages import supported_languages, language_problem_sets

# Define initial user level
user_level = 1

def handle_zero_input():
    while True:
        print("\nYou pressed 0. Choose an option:")
        print("1. Return to Main Menu")
        print("2. Exit the Application")
        choice = input("Enter your choice: ")

        if choice == "1":
            main_menu()
            break
        elif choice == "2":
            print("Exiting the Vocabulary Trainer. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def introduce_app():
    print(f"Hello! Welcome to the Vocabulary Trainer.")
    print("Press 0 to see other menu options.")
    menu_choice = input("Your choice: ")

    if menu_choice == "0":
        handle_zero_input()
    else:
        print("Invalid choice. Please try again.")
        introduce_app()

def display_problem(language, level):
    problem_set = language_problem_sets[language][level]
    word, translation = random.choice(list(problem_set.items()))
    print(f"Translate the word '{word}' to English.")
    return translation

def get_user_input():
    user_input = input("Your answer (press 0 to cancel): ").strip().lower()
    if user_input == "0":
        handle_zero_input()
    return user_input

def choose_language_and_level():
    print("\nChoose a language:")
    for i, language in enumerate(supported_languages, start=1):
        print(f"{i}. {language}")

    language_choice = input("Enter the number of your choice: ")

    if language_choice == "0":
        handle_zero_input()
    elif language_choice.isdigit() and 1 <= int(language_choice) <= len(supported_languages):
        selected_language = supported_languages[int(language_choice) - 1]
        selected_level = choose_level(selected_language)
        return selected_language, selected_level
    else:
        print("Invalid choice. Please try again.")
        return choose_language_and_level()

def choose_level(language):
    levels = list(language_problem_sets[language].keys())
    print(f"\nChoose a level for {language}:")
    for i, level in enumerate(levels, start=1):
        print(f"{i}. Level {level}")

    level_choice = input("Enter the number of your choice: ")

    if level_choice == "0":
        handle_zero_input()
    elif level_choice.isdigit() and 1 <= int(level_choice) <= len(levels):
        selected_level = levels[int(level_choice) - 1]
        return selected_level
    else:
        print("Invalid choice. Please try again.")
        return choose_level(language)

def main_menu():
    print("\nMain Menu:")
    print("1. Learn and Practice")
    print("2. Rules and Guidelines")
    print("3. View Level")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        learn_and_practice_menu()
    elif choice == "2":
        rules_and_guidelines()
    elif choice == "3":
        print(f"\nYou are currently in Level {user_level}.\n")
        main_menu()
    elif choice == "4":
        print("Exiting the Vocabulary Trainer. Goodbye!")
        exit()
    elif choice == "0":
        handle_zero_input()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def learn_and_practice_menu():
    print("\nLearn and Practice Menu:")
    print("1. Pick a Language")
    print("2. Start Practice")
    print("3. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        selected_language, selected_level = choose_language_and_level()
        learn_and_practice(selected_language, selected_level)
    elif choice == "3":
        main_menu()
    elif choice == "0":
        handle_zero_input()
    else:
        print("Invalid choice. Please try again.")
        learn_and_practice_menu()

def learn_and_practice(language, level):
    print(f"\nYou have selected {language} at Level {level}.")
    while True:
        correct_answer = display_problem(language, level)
        user_input = get_user_input()

        if user_input == "0":
            continue  # Continue will skip the rest of the loop and start over
        elif user_input == "exit":
            break

        is_correct = check_answer(user_input, correct_answer)
        display_result(is_correct, correct_answer)  # Pass the correct answer for feedback
        track_user_level(is_correct, correct_answer)  # Pass the correct answer for tracking

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer.lower()

def display_result(is_correct, correct_answer):
    if is_correct:
        print("Correct! Well done.")
    else:
        print(f"Incorrect, the correct answer is '{correct_answer}'. Keep practicing.")

def track_user_level(is_correct, correct_answer):
    global user_level

    if is_correct:
        user_level += 1
        print(f"Your level has increased to {user_level}.\n")
    else:
        user_level -= 1
        if user_level < 1:
            print(f"Game over! The correct answer was '{correct_answer}'.")
            print("Let's start over.")
            user_level = 1  # Reset level to 1
            introduce_app()  # Restart the game from the introduction
        else:
            print(f"Your level has decreased to {user_level}.\n")

def rules_and_guidelines():
    print("\t\tRules and Guidelines:\n")
    print("Welcome to the Vocabulary Trainer! Here are the rules and guidelines:\n")
    print("1. You will be presented with words in a foreign language.")
    print("2. Input the English translation in the provided format.")
    print("3. Your goal is to master as many words as possible.")
    print("4. You can choose a language and practice specific levels.")
    print("5. Each correct answer increases your level, while incorrect answers decrease it.")
    print("6. To exit at any time, type 'exit' as your answer.")
    print("7. Press 0 at any time to see the exit and main menu options.")
    print("\nLet's start learning! Choose 'Learn and Practice' from the main menu.\n")
    main_menu()

if __name__ == "__main__":
    introduce_app()
