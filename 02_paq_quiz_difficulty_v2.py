def quiz_difficulty(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "easy":
            return response
        elif response == "medium":
            return response
        elif response == "nightmare":
            return response
        if response == "1":
            response = "easy"
            return response
        elif response == "2":
            response = "medium"
            return response
        elif response == "3":
            response = "nightmare"
            return response
        else:
            print(error)
            continue

# lists with every question in a difficulty go here
easy_questions = ["Easy", "questions", "go", "here"]
medium_questions = ["Medium", "questions", "go", "here"]
nightmare_questions = ["Hardest", "questions", "go", "here"]
# loop for testing
while 1 == 1:
    difficulty = quiz_difficulty("What difficulty do you want to use? ", "Please enter '1', '2' or '3")
    print()
    if difficulty == "easy":
        print(easy_questions)
    elif difficulty == "medium":
        print(medium_questions)
    else:
        print(nightmare_questions)
    print()