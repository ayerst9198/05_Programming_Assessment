import random                                 

# Functions go here

# the instructions for the game are stored here
def instructions():
    # prints instructions
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

# makes things look good
def statement_generator(statement, side_decoration, top_bottom_decoration):

    # makes the deco on the sides 3 times length
    sides = side_decoration * 3
    # makes the final mid part of the statement, with sides attatched
    statement = "{} {} {}".format(sides, statement, sides)

    # makes the deco on tope the length of the statement with the sides
    top_bottom = top_bottom_decoration * len(statement)

    # prints the statement with all the deco, in the correct order
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# confines user answer to a set numbers without crashing
def num_check(question, num_type, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            # gets the user to input something
            response = input(question).lower()

            # if the response is the same as the exit code, it closes the funtion, skipping the error.
            if response == exit_code:
                return response

            # makes sure response is a number
            else:
                response = num_type(response)

            # IF there is a min and max number, make sure it is within the boundaries
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue
            
            # if there is a minimum number, make sure it is above the minimum
            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue
            # if there is a max number, make sure it is below the max
            elif high is not None:
                if response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue
            # otherwise accept the response
            else:
                return response
            
        # if the result is not the exit code or a number, it prints error
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
yes_no = ["yes", "no"]

# Result for if the user quits before doing anything
result = "You Quit"

# lists for game statistics
game_summary = []

questions_lost = 0
questions_won = 0

# thing for loop
play_again = "yes"

# list for difficulty
difficulty_options = ["easy", "medium", "hard", "nightmare"]

# Welcomes users to the game
statement_generator("Welcome to the Math Quiz", "|", "-")
print()

# asks user if they have played before for instructions
show_instructions = choice_checker("Have you used this quiz before? ", yes_no, "Please enter yes or no")
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
    quiz_difficulty = choice_checker("What difficulty do you want to use? easy (e), medium (m), hard (h), nightmare (n) ", difficulty_options,"Please enter e (easy), m (medium), h (hard), or n (nightmare)")
    print()

    # decides how many rounds you can play
    questions = num_check("How many questions do you want to answer? ", int, "Please enter an int above 0", 1)
    print()

    # loops untill user has played all rounds
    while questions != questions_played:
        statement_generator("Question: {}".format(questions_played + 1), "*" ,"*")

        # randomly generates integers for math questions
        if quiz_difficulty != "nightmare":
            rand = random.randint(1,10)
            rand2 = random.randint(1,10)

            # changes operation depending of difficulty
            if quiz_difficulty == "easy":
                operation = random.choice(easy_questions)
            elif quiz_difficulty == "medium":
                operation = random.choice(medium_questions)
            elif quiz_difficulty == "hard":
                operation = random.choice(hard_questions)   

        # creates seperate scenario for nightmare mode
        else:
            rand = random.randint(1,100)
            rand2 = random.randint(1,30)
            operation = random.choice(nightmare_questions)

        # Changes first random number so that no negative or negative numbers appear
        if operation == "-":
            temp_rand = random.randint(1, 10)
            rand = rand2 + temp_rand
        elif operation == "/":
            rand2 = random.randint(1,10)
            temp_rand = random.randint(1,10)
            rand = rand2 * temp_rand

        # generates ans using the randomly generated stuff above
        ans = eval(str(rand) + operation + str(rand2))

        # changes how the operation looks to user so it is less confusing
        if operation == "*":
            operation = "x"
        elif operation == "**":
            operation = "^"

        # changes between int and float depending if it is nightmare difficulty or not, for the sake of appearances in the results
        if quiz_difficulty != "nightmare":
            user_ans = num_check("What is {} {} {}? ".format(rand, operation ,rand2), int, "Please enter an integer", None, None, exit_code = "xxx")
        else:
            user_ans = num_check("What is {} {} {}? ".format(rand, operation ,rand2), float, "Please enter an number", None, None, exit_code = "xxx")
        print()

        # compares users answer to ans
        if user_ans == "xxx":
            statement_generator("You Quit", "|", "*")
            print()
            break
        
        # if user gets it right, get awarded 100 points, and result is added to lists for history
        elif user_ans == ans:
            print("You got it right")
            print()
            questions_won += 1
            points += 100
            result = "correct"
        
        # if user gets it wrong, get deduct 10 points, and result is added to lists for history
        else:
            print("WRONG")
            print()
            print("The answer is: {}".format(ans))
            print()
            result = "incorrect"
            points -= 10
            questions_lost += 1

        # adds number to rounds and adds 100 points to max points 
        questions_played += 1
        max_points += 100
        game_summary.append("Question #{}: {} {} {} = {}: {}".format(questions_played, rand, operation, rand2, user_ans, result))

    # shows final score
    statement_generator("Final Score: {} / {}".format(points, max_points), "|", "*")
    print()

    # asks user if they want to see history
    show_history = choice_checker("would you like to see quiz history? ", yes_no, "Please enter yes or no")

    # if user says yes, show the history
    if show_history == "yes":
        
        # if the result is quit, use a different system to avoid errors
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
            statement_generator("Quiz History", "|", "*")
            for game in game_summary:
                print(game)
            print()
            # prints the statistics
            statement_generator("Quiz Statistics", "%", "-")
            print("Correct: {}: ({:.0f}%)\nIncorrect: {}: ({:.0f}%)".format(questions_won, percent_win, questions_lost, percent_lose))
            print()

    # asks user if they want to play again
    game_summary = []
    play_again = choice_checker("Do you want to use the quiz again? ", yes_no, "Please enter yes or no")
print()
print("See you next time")
print()
