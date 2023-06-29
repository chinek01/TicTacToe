"""

Game logic
Start date: 2023-06-28
Author: MC

"""


class Game:

    area_win_conf = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6]]

    def __init__(self):
        self.area = ['-', '-', '-',
                     '-', '-', '-',
                     '-', '-', '-']

    def set_symbol_on_field(self,
                            symbol,
                            field):
        """
        Set symbol X or O on area field
        :param symbol: X or O
        :param field: field number from 0 to 8
        :return: OK - success set symbol on field , Not ok - field is not emoty
        """

        if symbol is None:
            raise ValueError("Symbol must be set!")

        try:
            symbol = symbol.__str__().upper()
        except Exception as e:
            print(f'Something bed happened: {e}')

        if not (symbol == 'X' or symbol == 'O'):
            raise ValueError("Symbol must be X or O")

        if self.check_field(field):
            self.area[field] = symbol
            self.check_win(symbol)
            return f"Success set field."
        else:
            return f"Field is not empty!"

    def check_field(self,
                    field):
        """
        Check the field is empty
        :param field: field number from 0 to 8
        :return: True - field is empty, False - field is'n empty
        """

        if field is None:
            raise ValueError('Field must be set!')

        if not (0 <= field <= 8):
            raise AttributeError('Field number must by from 0 to 8')

        # for f in self.area:
        #     if f != '-':
        #         return False
        #
        # return True

        if self.area[field] == '-':
            return True
        else:
            return False

    def print_area(self):
        """
        Print game area.
        """

        print('', self.area[0], '| ', self.area[1], '|', self.area[2])
        print("---+----+---")
        print('', self.area[3], '| ', self.area[4], '|', self.area[5])
        print("---+----+---")
        print('', self.area[6], '| ', self.area[7], '|', self.area[8])

    def check_win(self,
                  symbol):
        match_table = []

        for n in range(len(self.area)):
            if self.area[n] == symbol:
                match_table.append(n)

        result = False

        for n in range(len(self.area_win_conf)):
            win_count = 0
            for w in range(len(self.area_win_conf[n])):
                for i in range(len(match_table)):
                    if match_table[i] == self.area_win_conf[n][w]:
                        win_count += 1

            if win_count == 3:
                result = True

        # return result
        print(f"Win result {result}")


# some class test
if __name__ == '__main__':
    game = Game()
    print(f"7: {game.check_field(7)}")
    # print(f"19: {game.check_field(19)}")
    # print(f"-9: {game.check_field(-9)}")
    # print(game.check_field())
    print(f"{game.set_symbol_on_field(symbol='o', field=0)}")
    print(f"{game.set_symbol_on_field(symbol='x', field=2)}")
    print(f"{game.set_symbol_on_field(symbol='o', field=1)}")
    print(f"{game.set_symbol_on_field(symbol='x', field=7)}")
    print(f"{game.set_symbol_on_field(symbol='o', field=4)}")
    print(f"{game.set_symbol_on_field(symbol='x', field=3)}")
    print(f"{game.set_symbol_on_field(symbol='o', field=8)}")

    print(game.print_area())
