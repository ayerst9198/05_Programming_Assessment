import random

num_1 = random.randint(1, 12)
num_2 = random.randint(1, 12)

big_num = num_1 * num_2

question = "{} / {}".format(big_num, num_2)
print(question)