import random                                 

# Functions go here

# the instructions for the game are stored here
def instructions():
    statement_generator("Instructions", "|", "?")
    print()
    print("This is a randomly generated math quiz.")
    print()
    print("There are 4 difficulties:")
    print("-easy (e)")
    print("-medium (m)")
    print("-hard (h). Divisions in hard mode are rounded to nearest whole number.")
    print("-nightmare (n) *The calculator cannot save you, The decimals are too long.")
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
def quiz_difficulty(question, valid_list, error):
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

# loops code
play_again = "yes"


difficulty_options = ["easy", "e", "medium", "", "hard", "h", "nightmare", "n"]
# Welcomes users to the game
statement_generator("Welcome to the Math Quiz", "|", "-")
print()

# asks user if they have played before for instructions
show_instructions = yes_no("Have you used this quiz before? ")
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
    difficulty = quiz_difficulty("What difficulty do you want to use? easy (e), medium (m), hard (h), nightmare (n) ", difficulty_options, "please enter easy (e), medium (m), hard (h), nightmare (n) ")
    print()

    # decides how many rounds you can play
    rounds = num_check("How many questions do you want to answer? ", int, "Please enter an int above 0", 1)
    print()

    # loops untill user has played all rounds
    while rounds + 1 != rounds_played:
        statement_generator("Question: {}".format(rounds_played), "*" ,"*")

        # randomly generates integers for math questions
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard" or difficulty == "nightmare":
            rand = random.randint(1,10)
            rand2 = random.randint(1,10)

            if difficulty == "easy":
                operation = random.choice(easy_questions)
                if operation == "-":
                    temp_num = random.randint(1, 10)
                    rand = rand2 + temp_num
                else:
                    rand = random.randint(1,10)
                    rand2 = random.randint(1,10)

            elif difficulty == "medium":
                operation = random.choice(medium_questions)

            elif operation == "hard":
                operation = random.choice(hard_questions)

                if operation == "/":
                    rand2 = random.randint(1,10)
                    temp_num = random.randint(1,10)
                    rand = rand2 * temp_num
                    
                else:
                    rand = random.randint(-10,10)
                    rand2 = random.randint(1,10)
            else:
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
