import random                                 

# Functions go here

# the instructions for the game are stored here
def instructions():
    statement_generator("Instructions", "|", "?")
    print()
    print("This is a randomly generated math quiz.")
    print()
    print("There are 4 difficulties:")
    print("- easy (e)")
    print("- medium (m)")
    print("- hard (h). Divisions in hard mode are rounded to nearest whole number.")
    print("- nightmare (n) *The calculator cannot save you, The decimals are too long.")
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

# confines user answer to set words
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

# Main routine goes here

# randomly generated operatives, depending on which mode user is playing
easy_questions = ["+", "-"]
medium_questions = ["*"]
hard_questions = ["*", "/"]
nightmare_questions = ["/", "**"]

# Result for if the user quits before doing anything
result = "You Quit"

# lists for game statistics
game_summary = []

questions_lost = 0
questions_won = 0

# thing for loop
play_again = "yes"

# list for difficulty
difficulty_options = ["easy", "e", "medium", "m", "hard", "h", "nightmare", "n"]

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
    questions_played = 0

    # keeps track of points
    points = 0
    max_points = 0

    # asks user for a difficulty
    game_difficulty = choice_checker("What difficulty do you want to use? easy (e), medium (m), hard (h), nightmare (n) ", difficulty_options,"Please enter e (easy), m (medium), h (hard), or n (nightmare)")
    print()

    # decides how many rounds you can play
    questions = num_check("How many questions do you want to answer? ", int, "Please enter an int above 0", 1)
    print()

    # loops untill user has played all rounds
    while questions != questions_played:
        statement_generator("Question: {}".format(questions_played + 1), "*" ,"*")

        # randomly generates integers for math questions
        if game_difficulty == "easy" or game_difficulty == "medium" or game_difficulty == "hard":
            rand = random.randint(1,10)
            rand2 = random.randint(1,10)

            if game_difficulty == "easy":
                operation = random.choice(easy_questions)
                
                if operation == "-":
                    rand2 = random.randint(1, 10)
                    temp_rand = random.randint(1, 10)
                    rand = rand2 + temp_rand

            elif game_difficulty == "medium":
                operation = random.choice(medium_questions)

            elif operation == "hard":
                operation = random.choice(hard_questions)
                
                if operation == "/":
                    rand2 = random.randint(1,10)
                    temp_rand = random.randint(1,10)
                    rand = rand2 * temp_rand
                else:
                    rand = random.randint(-10,10)
                    rand2 = random.randint(1,10)

        if game_difficulty == "nightmare":
            rand = random.randint(1,100)
            rand2 = random.randint(1,30)
            operation = random.choice(nightmare_questions)

        # generates ans using the randomly generated stuff above
        ans = eval(str(rand) + operation + str(rand2))

        if operation == "*":
            operation = "x"
        elif operation == "**":
            operation = "^"


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
            questions_won += 1
            points += 100
            result = "correct"
        
        else:
            print("WRONG")
            print()
            print("The answer is: {}".format(ans))
            print()
            result = "incorrect"
            points -= 10
            questions_lost += 1

        questions_played += 1
        max_points += 100
        game_summary.append("Question #{}: {}".format(questions_played, result))

    # shows final score
    statement_generator("Final Score: {} / {}".format(points, max_points), "|", "*")
    print()

    show_history = yes_no("would you like to see game history? ")

    if show_history == "yes":
        if result == "You Quit":
            print()
            print("Question 1: {}".format(result))
            print()
        else:
            # **** Calculate Game Stats ****
            percent_win = questions_won / questions_played * 100
            percent_lose = questions_lost / questions_played * 100

            # shows statistics
            print()
            statement_generator("Game History", "|", "*")
            for game in game_summary:
                print(game)
            print()
            statement_generator("Game Statistics", "%", "-")
            print("Correct: {}: ({:.0f}%)\nIncorrect: {}: ({:.0f}%)".format(questions_won, percent_win, questions_lost, percent_lose))
            print()

    # asks user if they want to play again
    play_again = yes_no("Do you want to play again? ")
print()
print("See you next time")
print()
