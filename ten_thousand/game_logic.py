import random
from collections import Counter

single_points = {1: 100, 5: 50}
triple_points = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(tuple):
        dice_counts = Counter(tuple)

        if len(dice_counts) == 6:
            return 1500

        total = 0

        if len(dice_counts) == 3 and all(value == 2 for value in dice_counts.values()):
            return 1500

        for number, count in dice_counts.items():
            if count < 3:
                total += count * single_points.get(number, 0)
            elif count == 3:
                total += triple_points[number]
            elif count == 4:
                total += triple_points[number] * 2
            elif count == 5:
                total += triple_points[number] * 3
            elif count == 6:
                total += triple_points[number] * 4
        return total

    @staticmethod
    def roll_dice(dice):
        number_list = []
        for num in range(dice):
            roll = random.randint(1, 6)
            number_list.append(roll)
        number_list = tuple(number_list)
        return number_list






