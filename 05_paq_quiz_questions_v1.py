import random
import math

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

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Unknown Answer "
                  "Detected. Please Input Yes/No")

def num_check(question, num_type, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()


            if response == exit_code:
                return response

            else:
                response = num_type(response)
 
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif high is not None:
                if response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()

# lists with every question in a difficulty go here
easy_questions = ["+", "-"]
medium_questions = ["*"]
nightmare_questions = ["/", "**"]
play_again = "yes"
while play_again == "yes":
    
    rounds = 5
    rounds_played = 1

    difficulty = quiz_difficulty("What difficulty do you want to use? ", "Please enter 1, 2, or 3")
    print()
    
    while rounds + 1 != rounds_played:
        print("Round: {}".format(rounds_played))
        if difficulty == "easy":
            rand = random.randint(1,10)
            rand2 = random.randint(1,10)
            operation = random.choice(easy_questions)
        elif difficulty == "medium":
            rand = random.randint(1,10)
            rand2 = random.randint(1,10)
            operation = random.choice(medium_questions)
        if difficulty == "nightmare":
            rand = random.randint(1,100)
            rand2 = random.randint(1,30)
            operation = random.choice(nightmare_questions)

        ans = eval(str(rand) + operation + str(rand2))
        print(ans)
        print()
        user_ans = num_check("What is {} {} {}? ".format(rand, operation ,rand2), float, "Please enter an integer", None, None, "xxx")
        print()

        if user_ans == ans:
            print("You got it right")
            print()
        else:
            print("WRONG")
            print()
        rounds_played += 1

    play_again = yes_no("Do you want to play again? ")
    print()

