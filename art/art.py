"""

Some art for project
Start date: 2023-06-28
Author: MC

"""

logo = """
          |          |    /\\
          |          |   |  |
          |          |    \/
----------+----------+----------
          |   \ /    |
          |    x     |
          |   / \    |
----------+----------+----------
          |          |    /\\
          |          |   |  |
          |          |    \/
"""


def set_player_name(player_num=1):
    return f"""
+---------------------------------------------------------------------------------------------------------------------+
|                                               Player settings                                                       |
+---------------------------------------------------------------------------------------------------------------------+
|                                                                                                                     |
|                                            Please enter player {player_num} name:                                              |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
"""


def set_player_move(player_num=1,
                    player_symbol=None):
    return f"""
+---------------------------------------------------------------------------------------------------------------------+
{set_player_help(player_num, player_symbol)}
+---------------------------------------------------------------------------------------------------------------------+
|                                                                                                                     |
|                                      Please enter your move (from 0 to 8)                                           |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
"""


def win_player_and_scoreboard(win_player,
                              second_player):
    return f"""
+---------------------------------------------------------------------------------------------------------------------+
{set_player_help(win_player.name, 'Win this round', '->')}
+---------------------------------------------------------------------------------------------------------------------+
|                                                                                                                     |
{set_player_help('Scoreboard', '', '', '')}
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
|                                                                                                                     |
{set_player_help(win_player.name, f'wins {win_player.score}', '->')}
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
|                                                                                                                     |
{set_player_help(second_player.name, f'wins {second_player.score}', '->')}
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
"""


def set_player_help(player_name=None,
                    player_symbol=None,
                    sep=':',
                    title='Player'):
    # 119 max chars for one row
    max_row_len = 119 - 2
    sub_line = f"{title} {player_name}{sep} {player_symbol}"
    sub_line_len = len(sub_line)

    # start build end line
    line_to_return = "|"
    line_range = int(max_row_len/2 - sub_line_len/2)

    for n in range(line_range):
        line_to_return += ' '

    line_to_return += sub_line

    for n in range(line_range):
        line_to_return += ' '

    if len(line_to_return) == 118:
        line_to_return += '|'
    else:
        line_to_return += ' |'

    return line_to_return


if __name__ == '__main__':
    print(set_player_help('Marcin', 'X'))
