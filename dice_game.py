from datetime import datetime
import itertools
from random import randint, seed

seed(datetime.now())

dices = [
    [1, 1, 6, 6, 8, 8],
    [2, 2, 4, 4, 9, 9],
    [3, 3, 5, 5, 7, 7]
]


def compare_two_dices(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6

    num_rounds = 10**5
    num_dice1_wins = 0
    num_dice2_wins = 0

    for _ in range(num_rounds):
        dice1_result = dice1[randint(0, 5)]
        dice2_result = dice2[randint(0, 5)]

        if dice1_result > dice2_result:
            num_dice1_wins += 1
        elif dice2_result > dice1_result:
            num_dice2_wins += 1

    if num_dice1_wins > num_dice2_wins:
        print("The dice {} is better than {}: \nout of {} rounds it won {} times".format(dice1, dice2, num_rounds, num_dice1_wins))
    elif num_dice2_wins > num_dice1_wins:
        print("The dice {} is better than {}: \nout of {} rounds it won {} times".format(dice2, dice1, num_rounds, num_dice2_wins))
    else:
        print("A tie")


compare_two_dices(dices[0], dices[1])
compare_two_dices(dices[1], dices[2])
compare_two_dices(dices[2], dices[0])


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    combinations = list(itertools.product(dice1, dice2))
    for combo in combinations:
        if combo[0] > combo[1]:
            dice1_wins += 1
        elif combo[1] > combo[0]:
            dice2_wins += 1

    return dice1_wins, dice2_wins


print(count_wins([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))

from itertools import permutations
print(permutations("123456789", 4).__sizeof__())
