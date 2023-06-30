"""

Gamer class logic
Start date: 2023-06-28
Author: MC

"""


class Gamer:

    max_score_value = 999

    def __init__(self,
                 name):
        if name is None or name == '':
            raise ValueError('The name must by set!')

        self.name = name
        self.score = 0
        self.symbol = 'X'
        self.is_max_score = False

    def increase_score(self):
        self.score += 1

        if self.score == self.max_score_value:
            self.is_max_score = True

    def get_score(self):
        return f"{self.symbol}->{self.name} : {self.score}"

    def set_symbol(self,
                   symbol="X"):
        self.symbol = symbol.__str__().upper()

    def get_symbol(self):
        return f"{self.symbol}"


if __name__ == '__main__':
    p1 = Gamer('Marcin')
    print(p1.get_symbol())
    p1.set_symbol('o')
    print(p1.get_symbol())
    print(p1.get_score())
    p1.increase_score()
    print(p1.get_score())



