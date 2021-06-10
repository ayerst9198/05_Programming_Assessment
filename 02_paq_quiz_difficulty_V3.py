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

while 1 == 1:
    difficulty = ["easy", "e", "medium", "m", "hard", "h", "nightmare", "n"]
    user_choice = choice_checker("What difficulty do you want?", difficulty, "please chhoose a valid difficulty")
    print