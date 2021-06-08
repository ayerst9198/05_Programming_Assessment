import random

# Functions go here

# the instructions for the game are stored here
def instructions():
    statement_generator("Instructions", "|", "?")
    print()
    print("This is a randomly generated math quiz.")
    print()
    print("There are 4 difficulties:")
    print("-easy (1)")
    print("-medium (2)")
    print("-hard (3)")
    print("-nightmare (3) *The calculator cannot save you, The decimals are too long.")
    print()
    print("Try to answer as many questions as possible.")
    print("Every correct answer gets you 100 points,")
    print("Every incorrect question removes 10 points.")
    print()
    print("Enjoy!")
    print()
    return ""

# confines the users answer to yes or no
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

# allows the user to choose a difficulty
def quiz_difficulty(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "easy":
            return response
        elif response == "medium":
            return response
        elif response == "hard":
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
            response = "hard"
            return response
        elif response == "4":
            response = "nightmare"
            return response
        else:
            print(error)
            continue

# makes things look good
def statement_generator(statement, side_decoration, top_bottom_decoration):


    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# confines user answer to a set numbers without crashing
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


# Main routine goes here

# randomly generated operatives, depending on which mode user is playing
easy_questions = ["+", "-"]
medium_questions = ["*"]
hard_questions = ["*", "/"]
nightmare_questions = ["/", "**"]
play_again = "yes"

# Welcomes users to the game
statement_generator("Welcome to the Math Quiz", "|", "-")
print()

# asks user if they have played before for instructions
show_instructions = yes_no("Have you played my game before? ")
print()
if show_instructions == "no":
    instructions()

# loops game
while play_again == "yes":

    # keeps track of how many rounds you've played
    rounds_played = 1

    # keeps track of points
    points = 0
    max_points = 0

    # asks user for a difficulty
    difficulty = quiz_difficulty("What difficulty do you want to use? easy (1), medium (2), hard (3), nightmare (4) ", "Please enter 1 (easy), 2 (medium), 3 (hard), or 4 (nightmare)")
    print()

    # decides how many rounds you can play
    rounds = num_check("How many questions do you want to answer? ", int, "Please enter an int above 0", 1)
    print()

    # loops untill user has played all rounds
    while rounds + 1 != rounds_played:
        statement_generator("Question: {}".format(rounds_played), "*" ,"*")

        # randomly generates integers for math questions
        if difficulty == "easy":

            rand = random.randint(1,10)
            rand2 = random.randint(1,10)
            operation = random.choice(easy_questions)

        elif difficulty == "medium":

            rand = random.randint(1,10)
            rand2 = random.randint(1,10)
            operation = random.choice(medium_questions)
        
        elif difficulty == "hard":
            rand = random.randint(-10,10)
            rand2 = random.randint(1,10)
            operation = random.choice(hard_questions)

        if difficulty == "nightmare":
            rand = random.randint(1,100)
            rand2 = random.randint(1,30)
            operation = random.choice(nightmare_questions)

        # generates ans using the randomly generated stuff above
        ans = eval(str(rand) + operation + str(rand2))

        if operation == "*":
            operation = "x"
        elif operation == "**":
            operation = "^"

        # prints answer for testing
        print("ans: {}".format(ans))
        print()
        user_ans = num_check("What is {} {} {}? ".format(rand, operation ,rand2), float, "Please enter an integer", None, None, exit_code = "xxx")
        
        print()

        # compares users answer to ans
        if user_ans == "xxx":
            statement_generator("You Quit", "|", "*")
            print()
            break

        elif user_ans == ans:
            print("You got it right")
            print()
            points += 100
        
        else:
            print("WRONG")
            print()
            print("The answer is: {}".format(ans))
            print()
            points -= 10
        rounds_played += 1
        max_points += 100

    # shows final score
    statement_generator("Final Score: {} / {}".format(points, max_points), "|", "*")
    print()

    # asks user if they want to play again
    play_again = yes_no("Do you want to play again? ")
print()
print("See you next time")
print()