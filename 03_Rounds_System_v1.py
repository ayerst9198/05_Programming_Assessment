# Functions go here
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

play_again = "yes"
while play_again == "yes":
    rounds = num_check("How many rounds do you want to play? ", int, "Please enter an int above 0", 1)
    print()
    rounds_played = 1
    while rounds + 1 != rounds_played:
        print("Round: {}".format(rounds_played))
        test = input("")
        rounds_played += 1
    play_again = yes_no("Do you want to play again? ")
    print()