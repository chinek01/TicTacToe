"""

Gamer class logic
Start date: 2023-06-28
Author: MC

"""


class Gamer:

    def __init__(self,
                 name):
        if name is None or name == '':
            raise ValueError('The name must by set!')

        self.name = name
        self.score = 0
        self.symbol = 'X'

    def increase_score(self):
        self.score += 1

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



