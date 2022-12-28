def calculate_bank_score(total_score, round_score, current_round):
    total_score += round_score
    print(f'You banked {total_score} points in round {current_round}')
    print(f'Total score is {total_score} points')
    return total_score


class Banker:
    # banker is responsible for tracking points on the shelf and in the bank

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amount):
        self.shelved += amount

    def clear_shelf(self):
        self.shelved = 0
