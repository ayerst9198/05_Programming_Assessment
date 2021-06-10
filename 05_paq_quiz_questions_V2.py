import random
import math

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an iten), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()

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
hard_questions = ["*", "/"]
nightmare_questions = ["/", "**"]
difficulty_options = ["easy", "e", "medium", "m", "hard", "h", "nightmare", "n"]

play_again = "yes"
while play_again == "yes":
    
    rounds = 5
    rounds_played = 1

    difficulty = choice_checker("What difficulty do you want to use? ", difficulty_options,"Please enter e, m, h, or n")
    print()
    
    while rounds + 1 != rounds_played:
        print("Round: {}".format(rounds_played))
        print()

        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            rand = random.randint(1,10)
            rand2 = random.randint(1,10)

            if difficulty == "easy":
                operation = random.choice(easy_questions)
                
                if operation == "-":
                    rand2 = random.randint(1, 10)
                    temp_rand = random.randint(1, 10)
                    rand = rand2 + temp_rand

            elif difficulty == "medium":
                rand = random.randint(1,10)
                rand2 = random.randint(1,10)
                operation = random.choice(medium_questions)

            elif difficulty == "hard":
                operation = random.choice(hard_questions)
                if operation == "/":
                    rand2 = random.randint(1,10)
                    temp_rand = random.randint(1,10)
                    rand = rand2 * temp_rand
                else:
                    rand = random.randint(-10,10)
                    rand2 = random.randint(1,10)

        if difficulty == "nightmare":
            rand = random.randint(1,100)
            rand2 = random.randint(1,30)
            operation = random.choice(nightmare_questions)

        ans = eval(str(rand) + operation + str(rand2))
        user_ans = num_check("What is {} {} {}? ".format(rand, operation ,rand2), float, "Please enter an integer", None, None, "xxx")
        print()

        if user_ans == ans:
            print("You got it right")
            print()
        else:
            print("WRONG")
            print()
            print("The answer is: {}".format(ans))
            print()
        rounds_played += 1

    play_again = yes_no("Do you want to play again? ")
    print()

