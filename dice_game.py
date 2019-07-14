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
print(count_wins([1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9]))


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    index = 0
    while index < len(dices):
        dice = dices[index]
        is_best_dice = True
        inner_index = 0
        while inner_index < len(dices):
            if index == inner_index:
                inner_index += 1
                continue
            dice_wins, comp_dice_wins = count_wins(dice, dices[inner_index])
            if dice_wins <= comp_dice_wins:
                is_best_dice = False
                break
            inner_index += 1
        if is_best_dice:
            return index
        index += 1
    return -1


print(find_the_best_dice([[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]))
print(find_the_best_dice([[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]))
print(find_the_best_dice([[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]))
print(find_the_best_dice([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0

    best_dice = find_the_best_dice(dices)
    if best_dice > -1:
        strategy["first_dice"] = best_dice
    else:
        strategy["choose_first"] = False
        for index in range(len(dices)):
            dice = dices[index]
            inner_index = 0
            while inner_index < len(dices):
                if index == inner_index:
                    inner_index += 1
                    continue
                dice_wins, comp_dice_wins = count_wins(dice, dices[inner_index])
                if dice_wins < comp_dice_wins:
                    strategy[index] = inner_index
                    break
                inner_index += 1

    return strategy


print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
print(compute_strategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))
print(compute_strategy([[1, 4, 5, 6, 9, 10], [2, 2, 3, 7, 11, 11], [3, 4, 4, 5, 6, 12]]))
