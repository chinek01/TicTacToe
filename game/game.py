"""

Game logic
Start date: 2023-06-28
Author: MC

"""


class Game:

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
        :return: True - , False -
        """

        if symbol is None:
            raise ValueError("Symbol must be set!")

        if field is None:
            raise ValueError("Field must be set!")

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

        for f in self.area:
            # print(f)
            if f != '-':
                return False

        return True


# some class test
if __name__ == '__main__':
    game = Game()
    print(f"7: {game.check_field(7)}")
    # print(f"19: {game.check_field(19)}")
    # print(f"-9: {game.check_field(-9)}")
    # print(game.check_field())
