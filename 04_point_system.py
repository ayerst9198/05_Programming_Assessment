points = 0
while 1 == 1:
    rounds = 5
    while rounds != 0:
        result = input("Win or lose? ")
        print()

        if result == "win":
            points += 100
        elif result == "lose":
            points -= 10
        else:
            print("please enter win or lose")
            print()
            continue
        rounds -= 1
    print("Final Score: {}".format(points))