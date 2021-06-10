points = 0
while 1 == 1:
    rounds = 5
    while rounds != 0:
        result = input("correct or incorrect? ")
        print()

        if result == "correct":
            print("+100 points")
            points += 100
            print()
            print("Score: {}".format(points))
        elif result == "incorrect":
            print("-10 point")
            points -= 10
            print()
            print("Score: {}".format(points))
        else:
            print("please enter correct or incorrect")
            print()
            continue
        rounds -= 1
    print("Final Score: {}".format(points))