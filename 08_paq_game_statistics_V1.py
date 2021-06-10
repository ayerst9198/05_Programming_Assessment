# Checks for yes or no responses Imported From LU
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
            print("<error> Please say yes or no")
            print()

# main routine goes here
game_summary = []

questions_played = 0
questions_lost = 0
questions_won = 0

for item in range(0, 5):
    result = input("choose result: ")

    outcome = "Question {}: {}".format(item - 1, result)

    if result == "lost":
        questions_lost += 1
        questions_played += 1
    elif result == "won":
        questions_won += 1
        questions_played += 1

    # Adds Game result to a list for history
    game_summary.append("Question #{}: {}".format(questions_played, result))

# **** Calculate Game Stats ****
percent_win = questions_won / questions_played * 100
percent_lose = questions_lost / questions_played * 100

# Asks user if they want to see there history
show_history = yes_no("would you like to see game history? ")

# displays history if user says yes
if show_history == "yes":
    print()
    print("**** Game History ****")
    for game in game_summary:
        print(game)

    print()
    print("Thanks for playing")

# Doesnt display history if user says no
elif show_history == "no":
    print()
    print("Thanks for Playing")

# asks user if they want to see the game stats
game_results = yes_no("Do you want to see your game stats? ")

if game_results == "yes":

    # Displays game stats with % values to the nearest whole number
    print()
    print("**** Game Statistics ****")
    print("Win: {}: ({:.0f}%)\nLoss: {}: ({:.0f}%)".format(questions_won, percent_win, questions_lost, percent_lose))
    print()
